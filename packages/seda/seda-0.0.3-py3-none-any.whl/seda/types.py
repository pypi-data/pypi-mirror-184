import sys
import typing as t

if sys.version_info < (3, 8):  # pragma: no cover
    from typing_extensions import Literal, Protocol, TypedDict
else:  # pragma: no cover
    from typing import Literal, Protocol, TypedDict

if sys.version_info < (3, 11):
    from typing_extensions import NotRequired
else:
    from typing import NotRequired

LambdaEvent = t.Dict[str, t.Any]
Lifespan = Literal["auto", "on", "off"]
PolicyVersion = Literal["2012-10-17", "2012-10-17", "2008-10-17"]
SNSSubscriptionProtocol = Literal[
    "http",
    "https",
    "email",
    "email-json",
    "sms",
    "sqs",
    "application",
    "lambda",
    "firehose",
]


class LambdaContext(Protocol):
    aws_request_id: str
    function_name: str
    function_version: str
    invoked_function_arn: str
    memory_limit_in_mb: int
    log_group_name: str
    log_stream_name: str
    identity: t.Optional[t.Type]
    client_context: t.Optional[t.Type]
    get_remaining_time_in_millis: t.Callable[[], int]


class Statement(TypedDict):
    Effect: Literal["Allow", "Deny"]
    Id: NotRequired[str]
    Sid: NotRequired[str]
    Action: NotRequired[t.Union[str, t.Sequence]]
    NotAction: NotRequired[t.Union[str, t.Sequence]]
    Principal: NotRequired[t.Dict[str, t.Any]]
    NotPrincipal: NotRequired[t.Dict[str, t.Any]]
    Resource: NotRequired[t.Union[str, t.Sequence]]
    NotResource: NotRequired[t.Union[str, t.Sequence]]
    Condition: NotRequired[t.Dict[str, t.Any]]


class Policy(TypedDict):
    Version: NotRequired[PolicyVersion]
    Statement: t.Sequence[Statement]


class ScheduleTimeWindow(TypedDict):
    Mode: Literal["OFF", "FLEXIBLE"]
    MaximumWindowInMinutes: NotRequired[int]
