import dataclasses
import enum
import json
import urllib.request

import lib.pass_client as pass_client


def get_gitlab_token() -> str:
    account_name: str = "gitlab_token"
    return pass_client.get_pass(account_name)


class GitlabTransport:
    def __init__(self, token: str):
        self.instance = "https://gitlab.com"
        self.pat = token

    def get_call(self, url):
        url = f"{self.instance}/api/v4/{url}"
        request = urllib.request.Request(url)
        request.add_header("PRIVATE-TOKEN", self.pat)

        try:
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:
            print("Error code: ", e.code)
            print(f"Failed to get todos from {self.instance}")
            exit(1)
        except urllib.error.URLError as e:
            print("Error reason: ", e.reason)
            print("Failed to reach {instance}")
            exit(1)
        else:
            data_text = response.read().decode("utf-8")
            return json.loads(data_text)


class PipelineStatus(enum.Enum):
    SUCCESS = "SUCCESS"
    IN_PROGRESS = "IN_PROGRESS"
    FAIL = "FAIL"
    UNKNOWN = "UNKNOWN"

    def to_view(self) -> str:
        if self.value == "SUCCESS":
            return "🟢"
        elif self.value == "FAIL":
            return "🔴"
        elif self.value == "IN_PROGRESS":
            return "🟡"
        elif self.value == "UNKNOWN":
            return "⚫️"
        else:
            raise NotImplementedError


@dataclasses.dataclass
class Mr:
    title: str
    web_url: str
    pipeline_status: PipelineStatus


class GitlabClient:
    def __init__(self, token: str, name: str) -> None:
        self.transport = GitlabTransport(token)
        self.name = name

    @staticmethod
    def _convert_pipeline_status(raw_status: str) -> PipelineStatus:
        if raw_status == "success":
            return PipelineStatus.SUCCESS
        elif raw_status == "running":
            return PipelineStatus.IN_PROGRESS
        elif raw_status == "failed":
            return PipelineStatus.FAIL
        else:
            return PipelineStatus.UNKNOWN

    def get_mrs(self) -> list[Mr]:
        mrs_raw = self.transport.get_call(f"merge_requests?state=opened&author_username={self.name}")
        mrs: list[Mr] = []
        for mr_raw in mrs_raw:
            project_id = mr_raw["project_id"]
            iid = mr_raw["iid"]
            mr_more_info = self.transport.get_call(f"projects/{project_id}/merge_requests/{iid}")
            print(mr_more_info["pipeline"]["status"])
            pipeline_status = self._convert_pipeline_status(mr_more_info["pipeline"]["status"])
            mr = Mr(
                title=mr_raw["title"],
                web_url=mr_raw["web_url"],
                pipeline_status=pipeline_status,
            )
            mrs.append(mr)
        return mrs
