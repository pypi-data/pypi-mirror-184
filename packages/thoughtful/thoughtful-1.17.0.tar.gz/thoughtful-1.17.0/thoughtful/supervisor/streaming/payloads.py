"""
Defines json payloads to be delivered to the streaming endpoint
"""
import datetime
from dataclasses import dataclass

import thoughtful
from thoughtful.supervisor.manifest import Manifest
from thoughtful.supervisor.reporting.step_report import StepReport
from thoughtful.supervisor.streaming.action import Action


@dataclass
class StreamingPayload:
    """
    Base payload format for all streaming messages.
    """

    run_id: str
    action: Action
    client: str = "supervisor"
    version: str = thoughtful.__version__

    def __json__(self) -> dict:
        return {
            "run_id": self.run_id,
            "client": self.client,
            "version": self.version,
            "action": self.action.value,
            "payload": {"timestamp": datetime.datetime.utcnow().isoformat()},
        }


class StepReportStreamingPayload(StreamingPayload):
    """
    Payload for sending a step report action.
    """

    def __init__(self, step_report: StepReport, run_id: str):
        super().__init__(run_id=run_id, action=Action.STEP_REPORT)
        self.step_report = step_report

    def __json__(self) -> dict:
        _json = super().__json__()
        _json["payload"]["step_report"] = self.step_report.__json__()
        return _json


class BotManifestStreamingPayload(StreamingPayload):
    """
    Payload for sending the manifest.
    """

    def __init__(self, manifest: Manifest, run_id: str):
        self.manifest = manifest
        super().__init__(run_id=run_id, action=Action.BOT_MANIFEST)

    def __json__(self) -> dict:
        _json = super().__json__()
        _json["payload"]["bot_manifest"] = self.manifest.__json__()
        return _json


class ArtifactsUploadedPayload(StreamingPayload):
    """
    Payload for notifying the stream consumer that artifacts have been uploaded
    to S3.
    """

    def __init__(self, run_id: str, output_artifacts_uri: str):
        self.output_artifacts_uri = output_artifacts_uri
        super().__init__(run_id, action=Action.ARTIFACTS_UPLOADED)

    def __json__(self) -> dict:
        _json = super().__json__()
        _json["payload"]["output_artifacts_uri"] = self.output_artifacts_uri
        return _json
