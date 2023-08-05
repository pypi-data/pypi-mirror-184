"""
The step context is a context manager that is used to supervise a single step
of a digital worker. It is used in lieu of the ``@step`` decorator for
situations when you do not want to write a function for a step. For example,
it is very useful when iterating over a list of items:

.. code-block:: python

    from thoughtful.supervisor import supervise, step_scope

    def times_two(integers: list) -> None:
        return integers * 2

    def times_three(integer: int) -> None:
        return integer * 3

    def main():
        num_list = [1, 2, 3, 4, 5]

        with step_scope("1.1"):
            num_list = times_two(num_list)

        for num in num_list:
            with step_scope("1.2"):
                num = times_three(num)

    if __name__ == '__main__':
        with supervise():
            main()

Aside: There are a few scenarios where this is actually more convenient than
using the decorator on a lower level. Thanks to the fact that we can yield
the ``self`` object from a context manager, we can use this to update
attributes such as the record status, the step status, and is even a bit
cleaner when setting the record ID.
"""

from __future__ import annotations

import warnings
from types import TracebackType
from typing import Optional, Type, Union

from thoughtful.supervisor.recorder import Recorder
from thoughtful.supervisor.reporting.record import Record
from thoughtful.supervisor.reporting.report_builder import ReportBuilder
from thoughtful.supervisor.reporting.report_builder import StepReportBuilder
from thoughtful.supervisor.reporting.status import Status
from thoughtful.supervisor.reporting.timer import Timer
from thoughtful.supervisor.streaming.callback import StreamingCallback


class StepContext:
    """
    A context manager for a step that is running inside another step.
    This is an alternative to ``@step`` decorator when you don't want
    to write an entire function for a step.
    """

    def __init__(
        self,
        builder: ReportBuilder,
        recorder: Recorder,
        *step_id,
        record_id: Optional[str] = None,
        streaming_callback: Optional[StreamingCallback] = None,
    ):
        """
        Args:
            builder: Where the step report will be written.
            recorder: Where messages and data logs will be written.
            *step_id: The step id of this step, ie `"1.1"`
            record_id: An optional ID of the record being actively processed
            streaming_callback (StreamingCallback, optional): If set, streams
                the status of work report steps to that callback handler.
                Defaults to `None`.
        """
        if len(step_id) > 1:
            warnings.warn(
                "Passing multiple step ids to StepContext is deprecated. "
                "Instead, pass a single step id string with dots, ie '1.1'",
                DeprecationWarning,
            )

        self.uuid = ".".join([str(n) for n in step_id])
        self.report_builder = builder
        self.recorder = recorder
        self.timer = Timer()
        self._status_override: Optional[Status] = None
        self.record_id: Optional[str] = record_id
        self._record_status_override: Optional[Status] = None
        self._streaming_callback = streaming_callback
        self.step_report_builder: StepReportBuilder

    def __enter__(self):
        """
        Logic for when this context is first started.

        Returns:
            MainContext: This instance.
        """
        start_time = self.timer.start()
        record = Record(self.record_id, Status.RUNNING) if self.record_id else None
        self.step_report_builder = StepReportBuilder(
            step_id=self.uuid,
            start_time=start_time,
            status=Status.RUNNING,
            message_log=self.recorder.messages,
            data_log=self.recorder.data,
            record=record,
        )
        if self._streaming_callback:
            self._streaming_callback.post_step_update(
                self.step_report_builder.to_report()
            )
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> bool:
        """
        Runs when the context is about to close, whether caused
        by a raised Exception or now.

        Returns:
            bool: True if the parent caller should ignore the
                Exception raised before entering this function
                (if any), False otherwise.
        """
        timed_info = self.timer.end()
        if self._status_override:
            step_status = self._status_override
        else:
            step_status = Status.FAILED if exc_type else Status.SUCCEEDED

        if self._record_status_override:
            record_status = self._record_status_override
        else:
            record_status = Status.FAILED if exc_type else Status.SUCCEEDED
        record = Record(self.record_id, record_status) if self.record_id else None

        self.step_report_builder = StepReportBuilder(
            step_id=self.uuid,
            start_time=timed_info.start,
            end_time=timed_info.end,
            status=step_status,
            message_log=self.recorder.messages,
            data_log=self.recorder.data,
            record=record,
        )
        self.report_builder.workflow.append(self.step_report_builder)
        if self._streaming_callback:
            self._streaming_callback.post_step_update(
                self.step_report_builder.to_report()
            )

        # Return False so that any exceptions inside this context
        # are still raised after this function ends
        return False

    def error(self) -> None:
        """
        Sets the status of this step to `Status.FAILED` in its `StepReport`.

        .. code-block:: python

            with step_scope("1.1") as s:
                ...  # do some stuff
                s.error()

        .. code-block:: json

            {
                "workflow": [
                    {
                        "step_id": "1.1",
                        "step_status": "failed"
                    }
                ]
            }
        """
        self.set_status(Status.FAILED)

    def set_status(self, status: Union[str, Status]) -> None:
        """
        Override the step context's status to be in the status of ``status``

        Args:
            status (str, Status): The status to set the step to

        .. code-block:: python

            with step_scope("1.1") as s:
                ...  # do some stuff
                s.set_status("warning")

        .. code-block:: json

            {
                "workflow": [
                    {
                        "step_id": "1.1",
                        "step_status": "warning"
                    }
                ]
            }
        """
        # Convert the status to the correct type if necessary
        safe_status = Status(status)
        self._status_override = safe_status

    def set_record_status(self, status: Union[str, Status]) -> None:
        """
        Override a step context's record to be in the status of ``status``

        Args:
            status (str, Status): The status to set the record to

        .. code-block:: python

            with step_scope("1.1", record_id="kaleb_cool_guy") as s:
                ...  # do some stuff
                s.set_record_status("warning")

        .. code-block:: json

            {
                "workflow": [
                    {
                        "step_id": "1.1",
                        "step_status": "succeeded",
                        "record": {
                            "id": "kaleb_cool_guy",
                            "status": "warning"
                        }
                    }
                ]
            }

        """
        # Convert the status to the correct type if necessary
        if not self.record_id:
            warnings.warn(
                "Setting a record status for a step without "
                "a record ID will have no effect",
                UserWarning,
            )
        safe_status = Status(status)
        self._record_status_override = safe_status


if __name__ == "__main__":
    report_builder = ReportBuilder()
    r = Recorder()

    substep = StepContext

    with substep(report_builder, r, 1) as s:
        print("hello world")

        with substep(report_builder, r, 1, 1) as s2:
            print("inner step")

    print(report_builder.workflow)
