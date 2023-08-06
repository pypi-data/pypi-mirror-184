"""Provides access to javascript objects.

Todos:
    * Add docstrings to classes, methods & module.
    * Add typing.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Iterable, Union, final

from sweetpotato.core.interfaces import BaseType
from sweetpotato.core.js_utils import add_curls


@final
@dataclass
class String(BaseType):
    """String implementation"""

    name: str
    item: str

    def as_js(self) -> str:
        """Add docstring."""
        return json.dumps(self.item)


@final
@dataclass
class Integer(BaseType):
    """Integer implementation"""

    name: str
    item: int

    def as_js(self) -> int:
        """Add docstring."""
        return self.item


@final
@dataclass
class Boolean(BaseType):
    """Bool implementation"""

    name: str
    item: bool

    def as_js(self) -> str:
        """Add docstring."""
        return json.dumps(self.item)


@final
@dataclass
class Object(BaseType):
    """The Object class is a Javascript object abstraction.

    Pass string values and access individual named objects (:class:~`sweetpotato.js_objects.String`,
    :class:~`sweetpotato.js_objects.Integer`, etc.) through dictionary retrieval.

    Examples:
        `obj = Object([Boolean(name="isAuthenticated", item=False)])`
        `print(obj["isAuthenticated"])`
        `true`
    """

    item: str
    name: str = ""

    def as_js(self) -> str:
        """Add docstring."""
        return f"{self.item}"


@final
@dataclass
class JsObject(BaseType):
    """The JsObject class is a Javascript object abstraction.

    Pass a list of :class:`sweetpotato.core.interfaces.BaseType` objects or
    string values and access individual named objects (:class:~`sweetpotato.js_objects.String`,
    :class:~`sweetpotato.js_objects.Integer`, etc.) through dictionary retrieval.

    Examples:
        `js_object = JsObject([Boolean(name="isAuthenticated", item=False)])`
        `print(js_object["isAuthenticated"])`
        `true`
    """

    item: list[BaseType]
    name: str = ""

    def as_js(self) -> Union[dict[str, str], str]:
        """Add docstring."""
        return {k.name: k.item if k.name else k.item for k in self.item}

    def __repr__(self) -> str:
        return self.name


@final
@dataclass
class Attributes(BaseType):
    """The Attributes class is a Javascript key:value pair abstraction.

    Pass a list of :class:`sweetpotato.core.interfaces.BaseType` objects or a string.
    Objects will be rendered as their respective types, while a string will present
    as an inline object value.

    Examples:
        `items = ["...eva", "Boolean("bar", True), Integer("num", 1), String("key", "value")]`
        `attributes = Attributes([Boolean(name="isAuthenticated", item=False)])`
        `print(attributes)`
        `{...eva} bar={true} num={1} foo={"...eva"}`
    """

    item: list[BaseType]
    name: str = ""

    def as_js(self) -> str:
        """Add docstring."""
        return " ".join(
            [
                f"{k.name}={add_curls(k.as_js())}" if k.name else add_curls(k.item)
                for k in self.item
            ]
        )


@final
@dataclass
class State(BaseType):
    """Public class representation of React state.

    The State class allows for dynamic data within application (button title value changes, etc.)
    components. State is accessed within a respective component; to be accessed in an external component,
    a Prop instance with the state object as an argument must be passed to the external component.

    Examples:
        `state = State(Boolean("isAuthenticated", False))`

    Todos:
        * Implement use_effect,use_state (React.useEffect,useState) methods.
        * Add increment and decrement operations.
    """

    item: Iterable[BaseType]
    name: str = ""

    def as_js(self) -> str:
        """Add docstring."""
        return json.dumps(asdict(self))
