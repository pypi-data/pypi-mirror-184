"""Wrappers around React hooks.

Todos:
    * Complete all functions.
    * Add function typing + docstrings.
    * Complete module docstrings.
"""
from __future__ import annotations

from typing import Any, Optional, Union

from sweetpotato.core.base_components import Composite
from sweetpotato.core.base_management import Effect, Function, State
from sweetpotato.core.js_utils import const, react_function


class Context(Composite):
    """Experimental context."""

    is_context = True
    is_composite = True
    context_collection: dict[str, Context] = {}

    def __init__(self, name=None, **kwargs):
        super().__init__(**kwargs, component_name=name)

    def add_context(self) -> Context:
        """

        Returns:

        """
        if self.component_name in self.context_collection:
            raise KeyError("Context exists.")
        self.context_collection[self.component_name] = self
        return self

    def get_context(self, name) -> "Context":
        """

        Args:
            name:

        Returns:

        """
        return self.context_collection[name]

    def __call__(self, children, *args, **kwargs):
        self._children.extend([children])
        return self


def use_state(
    name: str,
    state_obj: State,
    increment: Optional[Union[int, str]] = None,
    decrement: Optional[Union[int, str]] = None,
) -> tuple[Function, str]:
    """Wrapper around React useState hook.

    Args:
        name: Name of state value.
        state_obj:
        increment: Value to increment state value.
        decrement: Value to decrement state value.

    Returns:
        Tuple of values.

    See Also:
        https://reactjs.org/docs/hooks-state.html

    Todos:
        * Add better docstring for this method.
        * Add increment and decrement operations.
    """
    increment_or_decrement = state_obj.set_incremental_or_decremental(
        increment=increment,
        decrement=decrement,
        default_value=state_obj.values[name],
    )
    if state_obj.is_functional:
        return state_obj.set_functional_state(
            name,
            state_obj.values[name],
            change=increment_or_decrement,
        )
    return state_obj.set_class_state(name, change=increment_or_decrement)


def use_effect(
    effect_obj: Effect, name: str, default_value: Optional[Any] = None
) -> tuple[str, str]:
    """Wrapper around React useEffect hook.

    Args:
        effect_obj:
        name: Name of state value.
        default_value: Default of state value.

    Returns:
        Tuple of values.

    See Also:
        https://reactjs.org/docs/hooks-effect.html

    Todos:
        * Add better docstring for this method + complete logic.
    """
    raise NotImplementedError(effect_obj, name, default_value)


def use_context(name: str) -> Context:
    """Wrapper around React useContext hook.

    Args:
        name:
    """
    return Context().get_context(name)


def create_context(name: str) -> Context:
    """Wrapper around React createContext hook."""
    context_func = const(name, react_function())
    return Context(name=name, variables=[context_func]).add_context()
