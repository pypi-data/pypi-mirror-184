"""Provides base functionality for State and Props classes.

Todos:
    * Cleanup + add docstrings, typing
"""
import json
from typing import Any, Optional

from sweetpotato.core import js_utils
from sweetpotato.core.interfaces import (
    BaseContext,
    BaseEffect,
    BaseFunction,
    BaseProps,
    BaseState,
)
from sweetpotato.core.js_utils import (
    add_class_props,
    add_class_state,
    add_curls,
    add_props,
    add_this,
    const,
)


class Function(BaseFunction):
    """Public class representation of .js functions."""

    def __init__(self, value: str, name: str, is_functional: bool) -> None:
        self.value = value
        self.name = name
        self.type = "" if is_functional else add_this()

    def __repr__(self) -> str:
        return js_utils.inline_function(
            name=f"{self.type}{self.name}", value=f"{self.value}"
        )


class Context(BaseContext):
    """Public class representation of Context."""


class Effect(BaseEffect):
    """Public class representation of React effect."""


class State(BaseState):
    """Public class representation of React state.

    The State class allows for dynamic data within application (button title value changes, etc.)
    components. State is accessed within a respective component; to be accessed in an external component,
    a Prop instance with the state object as an argument must be passed to the external component.

    Examples:
        `state = State({"isAuthenticated": False})`
        `set_pressed, pressed = state.use_state(name="pressed", default_value=False)`

    Todos:
        * Implement State.use_effect (React.useEffect) method.
        * Add increment and decrement operations.
    """

    parent = None

    def __init__(
        self,
        values: Optional[dict[str, Any]] = None,
        name: Optional[str] = None,
        is_functional: bool = False,
    ) -> None:
        self.name = name
        self.is_functional = is_functional
        self.values = values if values else {}
        self.functions = []
        self.type = self.__class__.__name__.lower()

    def as_json(self) -> str:
        """Return dict as json."""
        return json.dumps(self.values)

    def use_state(
        self, name: str, change: Optional[int] = None
    ) -> tuple[Function, str]:
        """Wrapper around React useState hook.

        Args:
            name: Name of state value.
            change: Value to increment/decrement state value.

        Returns:
            Tuple of values.

        See Also:
            https://reactjs.org/docs/hooks-state.html

        Todos:
            * Add better docstring for this method.
            * Add increment and decrement operations.
        """

        if self.is_functional:
            return self.set_functional_state(
                name=name,
                default_value=self.values[name],
                change=change,
            )
        return self.set_class_state(name, change=change)

    def use_effect(
        self, name: str, default_value: Optional[Any] = None
    ) -> tuple[str, str]:
        """Wrapper around React useEffect hook.

        Args:
            name: Name of state value.
            default_value: Default of state value.

        Returns:
            Tuple of values.

        See Also:
            https://reactjs.org/docs/hooks-effect.html

        Todos:
            * Add better docstring for this method + complete logic.
        """
        raise NotImplementedError

    def set_class_state(self, name: str, change: str) -> tuple[Function, str]:
        """Sets state in class format.

        Args:
            change: Increment or decrement by specific value, if either enabled.
            name: Name of state value.
        """
        if change:
            change = f" + {change}" if change >= 0 else change
        state_output = f"set{name.title()}"
        change = change if change else ""
        set_state_dict = add_curls(f"{name} : {name}New {change}")
        state_function = add_this(f"setState({set_state_dict});")
        class_state = add_class_state(name)
        function = Function(
            value=class_state,
            name=state_output,
            is_functional=self.is_functional,
        )
        self.functions.append(f"{state_output} = ({name}New) => {state_function}")
        return function, f"${add_curls(class_state)}"

    def set_functional_state(
        self, name: str, default_value: Any, change: str
    ) -> tuple[Function, str]:
        """Sets state in functional format.

        Args:
            change: Increment or decrement by specific value, if either enabled.
            name: Name of state value.
            default_value: default for passed state key.
        """
        if change:
            change = f" + {change}" if change >= 0 else change
        function_name = f"set{name.title()}"
        state_function = f"React.useState({json.dumps(default_value)});"
        function_repr = const(f"[{name}, {function_name}]", state_function)
        change = f"{name} {change}" if change else name
        function = Function(
            value=change,
            name=function_name,
            is_functional=self.is_functional,
        )
        self.functions.append(function_repr)
        return (
            function,
            f"{add_curls(name)}",
        )

    def __getitem__(self, item: Any) -> Any:
        return self.values[item]


class Props(BaseProps):
    """Public class representation of React props.

    Expected value is a state object.

    Examples:
        `props = Props(state)`
    """

    def __init__(
        self,
        state: Optional[State] = None,
        is_functional: Optional[bool] = False,
    ) -> None:
        self.state = state
        self.is_functional = is_functional
        self.values = state.values if state else {}
        self.type = self.__class__.__name__.lower()

    def as_json(self) -> str:
        """Return dict as json."""
        return json.dumps(self.values)

    def __getitem__(self, item: Any) -> str:
        if not self.is_functional:
            return add_curls(add_class_props(item))

        return add_curls(add_props(item))
