from typing import Dict, Any, Optional, MutableSequence, Type

from kilroy_module_pytorch_py_sdk.optimizers import Optimizer, AdamOptimizer
from kilroy_module_pytorch_py_sdk.regularizations.policy import (
    PolicyRegularization,
)
from kilroy_module_pytorch_py_sdk.schedulers import Scheduler
from kilroy_module_pytorch_py_sdk.trainers.vanilla.reinforced.methods import (
    Method,
    ReinforceMethod,
)
from kilroy_module_pytorch_py_sdk.trainers.vanilla.reinforced.state import (
    State,
)
from kilroy_server_py_utils import (
    CategorizableBasedParameter,
    CategorizableBasedOptionalParameter,
    MultipleCategorizableBasedOptionalParameter,
    classproperty,
)


class OptimizerParameter(CategorizableBasedParameter[State, Optimizer]):
    @classmethod
    async def _get_params(cls, state: State, category: str) -> Dict[str, Any]:
        policy = await state.models.policy.loader.get()
        return {
            "parameters": policy.model.parameters(),
            **state.models.policy.optimizer.params.get(category, {}),
        }

    @classmethod
    async def _get_categorizable(cls, state: State) -> Optimizer:
        return state.models.policy.optimizer.optimizer

    @classmethod
    async def _set_categorizable(cls, state: State, value: Optimizer) -> None:
        state.models.policy.optimizer.optimizer = value
        if state.models.policy.scheduler.scheduler is not None:
            optimizer = await value.get()
            await state.models.policy.scheduler.scheduler.change_optimizer(
                optimizer
            )

    # noinspection PyMethodParameters
    @classproperty
    def default_categorizable(cls) -> Type[Optimizer]:
        return AdamOptimizer


class SchedulerParameter(
    CategorizableBasedOptionalParameter[State, Scheduler]
):
    @classmethod
    async def _get_params(cls, state: State, category: str) -> Dict[str, Any]:
        return {
            "optimizer": await state.models.policy.optimizer.optimizer.get(),
            **state.models.policy.scheduler.params.get(category, {}),
        }

    @classmethod
    async def _get_categorizable(cls, state: State) -> Optional[Scheduler]:
        return state.models.policy.scheduler.scheduler

    @classmethod
    async def _set_categorizable(
        cls, state: State, value: Optional[Scheduler]
    ) -> None:
        state.models.policy.scheduler.scheduler = value


class MethodParameter(CategorizableBasedParameter[State, Method]):
    @classmethod
    async def _get_params(cls, state: State, category: str) -> Dict[str, Any]:
        return state.method.params.get(category, {})

    @classmethod
    async def _get_categorizable(cls, state: State) -> Method:
        return state.method.method

    @classmethod
    async def _set_categorizable(cls, state: State, value: Method) -> None:
        state.method.method = value

    # noinspection PyMethodParameters
    @classproperty
    def default_categorizable(cls) -> Type[Method]:
        return ReinforceMethod


class RegularizationsParameter(
    MultipleCategorizableBasedOptionalParameter[State, PolicyRegularization]
):
    @classmethod
    async def _get_categorizables(
        cls, state: State
    ) -> Optional[MutableSequence[PolicyRegularization]]:
        return state.regularizations.regularizations

    @classmethod
    async def _set_categorizables(
        cls,
        state: State,
        value: Optional[MutableSequence[PolicyRegularization]],
    ) -> None:
        state.regularizations.regularizations = value

    @classmethod
    async def _get_params(cls, state: State, category: str) -> Dict[str, Any]:
        return state.regularizations.params.get(category, {})
