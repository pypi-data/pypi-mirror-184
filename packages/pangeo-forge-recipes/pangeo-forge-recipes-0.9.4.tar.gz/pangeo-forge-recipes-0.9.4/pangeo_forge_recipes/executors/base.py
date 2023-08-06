from __future__ import annotations

import enum
from dataclasses import dataclass
from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

from mypy_extensions import NamedArg

Config = Any  # TODO: better typing for config
SingleArgumentStageFunction = Callable[[Any, NamedArg(type=Any, name="config")], None]  # noqa: F821
NoArgumentStageFunction = Callable[[NamedArg(type=Any, name="config")], None]  # noqa: F821
StageFunction = Union[NoArgumentStageFunction, SingleArgumentStageFunction]


class StageAnnotationType(enum.Enum):
    CONCURRENCY = enum.auto()
    RETRIES = enum.auto()


StageAnnotations = Dict[StageAnnotationType, Any]


@dataclass(frozen=True)
class Stage:
    function: StageFunction
    name: str
    mappable: Optional[Iterable] = None
    annotations: Optional[StageAnnotations] = None


@dataclass(frozen=True)
class Pipeline:
    stages: Iterable[Stage]
    config: Optional[Config] = None


T = TypeVar("T")


class PipelineExecutor(Generic[T]):
    @staticmethod
    def compile(pipeline: Pipeline) -> T:
        raise NotImplementedError

    @staticmethod
    def execute(plan: T):
        raise NotImplementedError
