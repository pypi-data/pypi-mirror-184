"""Provides custom protocols for typing.

Todo:
    * Add docstrings for all classes & methods.
    * Add typing.
"""
from __future__ import annotations

from abc import abstractmethod
from typing import Any, ClassVar, Literal, Optional, Protocol, Union, runtime_checkable


@runtime_checkable
class BaseType(Protocol):
    """Base interface."""

    name: str
    item: Any

    @abstractmethod
    def as_js(self) -> Any:
        """Interface method."""
        raise NotImplementedError


class BaseFunction(Protocol):
    """Function protocol."""


class BaseState(Protocol):
    """Protocol interface for State."""

    name: str
    type: str
    is_functional: bool
    functions: list[str]
    values: Optional[dict[str, Any]]

    @abstractmethod
    def use_state(
        self,
        name: str,
        increment: Optional[Union[int, str]] = None,
        decrement: Optional[Union[int, str]] = None,
    ) -> tuple[BaseFunction, str]:
        """Protocol method wrapper around React useState hook."""
        ...

    @abstractmethod
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
            * Add better docstring for this method.
        """
        ...

    @abstractmethod
    def set_class_state(
        self, name: str, incr_or_decr_val: str
    ) -> tuple[BaseFunction, str]:
        """Protocol method sets state in class format."""
        ...

    @abstractmethod
    def set_functional_state(
        self, name: str, default_value: Any, incr_or_decr_val: str
    ) -> tuple[BaseFunction, str]:
        """Protocol method sets state in functional format."""
        ...

    @abstractmethod
    def as_json(self) -> str:
        """Protocol method for json rendering."""
        ...


class BaseProps(Protocol):
    """Props protocol."""


class BaseEffect(Protocol):
    """Effect protocol."""


class BaseContext(Protocol):
    """Context protocol."""


class BaseJsObject(Protocol):
    """JsObject protocol."""

    objects: dict[str, str]
    values: list[BaseState]
    item: Any
    name: str


class BaseComponent(Protocol):
    """Base React Native component protocol."""

    package: str  #: Default package for component.
    allowed_attributes: set[
        str
    ]  #: Set of allowed props for component, default `'state'`, `'props'`, `'style'`.
    base_attributes: set[
        str
    ]  #: Set of allowed props for component, default `'state'`, `'props'`, `'style'`.
    is_composite: bool = False  #: Indicates whether component may have inner content.
    import_name: str

    @property
    @abstractmethod
    def children(self) -> str:
        """Property returning inner content."""
        raise NotImplementedError

    @property
    @abstractmethod
    def variables(self) -> str:
        """Property returning string of variables (if any) belonging to given component."""
        raise NotImplementedError

    @property
    @abstractmethod
    def attrs(self) -> str:
        """Property string of given attributes for component"""
        raise NotImplementedError

    @abstractmethod
    def _make_state_or_prop_attrs(self, attr: Union[BaseState, BaseProps]) -> str:
        raise NotImplementedError

    @abstractmethod
    def _format_attr(self, attr, key) -> None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def _make_key_with_attr(key, attr) -> str:
        raise NotImplementedError

    @abstractmethod
    def _set_default_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def render(self) -> str:
        """Renders a .js formatted string of the component."""
        raise NotImplementedError


class BaseComposite(BaseComponent, Protocol):
    """Base React Native component protocol."""

    is_context: bool = False  #: Indicates whether component is a context, similar to an inline if-else.
    is_root: bool = False  #: Indicates whether component is a top level component.

    _functions: Union[list[str], str]
    _children: Union[list[Union[BaseComponent, BaseComposite]]]
    is_composite: bool = True  #: Indicates whether component may have inner content.

    @property
    @abstractmethod
    def functions(self) -> str:
        """Property returning inner content."""
        raise NotImplementedError

    @abstractmethod
    def function_formatter(self, functions) -> None:
        """Generic method for setting functions."""
        raise NotImplementedError

    @abstractmethod
    def check_functions(self, functions: list[str]) -> None:
        """Checks .js functions for errors."""
        raise NotImplementedError


class BaseRootComponent(BaseComposite, Protocol):
    """Root component."""

    _functions: Union[list[str], str]
    is_root: bool = True  #: Indicates whether component is a top level component.
    _children: list[BaseComposite]

    package_root: ClassVar[str]  #: Default package for component.
    is_functional: bool = (
        False  #: Indicates whether component a functional or class component.
    )
    is_composite: bool = False  #: Indicates whether component may have inner content.

    @property
    @abstractmethod
    def imports(self) -> str:
        """Property returning string of imports (if any) belonging to given component."""
        raise NotImplementedError

    @property
    @abstractmethod
    def state(self) -> str:
        """Property returning json string of state (if any) belonging to given component."""
        raise NotImplementedError

    @abstractmethod
    def _set_parent(self, obj: Union[BaseComposite, BaseComponent]) -> None:
        """Sets top level component as root and sets each parent to self."""
        raise NotImplementedError

    @abstractmethod
    def serialize(
        self,
        as_format: Literal["dict", "json", "pickle"] = "dict",
    ) -> Union[dict[str, BaseRootComponent], bytes, str]:
        """Returns component as specified serialization format."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def register(cls, management_obj: Union[BaseState, BaseProps]) -> None:
        """Registers state/prop object as functional or class based."""
        raise NotImplementedError

    @abstractmethod
    def _check_packages(self) -> list[str]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def _install_package(package: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def render(self) -> str:
        """Renders a .js formatted string of the component."""
        raise NotImplementedError

    @abstractmethod
    def _make_state_or_prop_attrs(self, attr: Union[BaseState, BaseProps]) -> str:
        raise NotImplementedError
