from dataclasses import dataclass


@dataclass
class GcpProject:
    id: str
    number: int


class GCP_PROJECTS:
    MY_PROJECT = GcpProject('your-project', 123456)
