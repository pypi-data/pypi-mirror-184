"""Core functionality of React Native class based components."""
import json
import os
import pathlib
import pickle
import sys
from functools import singledispatchmethod
from typing import Any, ClassVar, Literal, Optional, Type, Union

from sweetpotato.config import settings
from sweetpotato.core import js_utils
from sweetpotato.core.base_management import Function, Props, State
from sweetpotato.core.interfaces import (
    BaseComponent,
    BaseComposite,
    BaseProps,
    BaseRootComponent,
    BaseState,
    BaseType,
)
from sweetpotato.core.js_objects import JsObject, Object
from sweetpotato.core.js_utils import camelize

component_registry: dict[str, BaseRootComponent] = {}


class Component(BaseComponent):
    """Base React Native component.

    Args:
        children: Inner content for component.
        variables: Contains variables (if any) belonging to given component.
        kwargs: Arbitrary keyword arguments.

    Attributes:
        _children: Inner content for component.
        _attrs: String of given attributes for component.
        _variables: Contains variables (if any) belonging to given component.
        allowed_attributes: Allowed allowed_attributes for component.
        parent: Name of parent component, defaults to `'App'`.

    Example:
        component = Component(children="foo")
    """

    package: str = "react-native"  #: Default package for component.
    allowed_attributes: set[
        str
    ] = (
        set()
    )  #: Set of allowed props for component, default `'state'`, `'props'`, `'style'`.
    base_attributes: set[str] = {
        "state",
        "props",
        "style",
        "_",
    }  #: Set of allowed props for component, default `'state'`, `'props'`, `'style'`.
    is_composite: bool = False  #: Indicates whether component may have inner content.

    def __init__(
        self,
        component_name: Optional[str] = None,
        children: Optional[str] = None,
        state: State = State(),
        props: Props = Props(),
        variables: Optional[list[str]] = None,
        *args: Union[BaseType, str, None],
        **kwargs: Union[BaseType, Function, str, bool, int, Type[None]],
    ) -> None:

        component_name = (
            self._set_default_name() if not component_name else component_name
        )
        if len(component_name.split(" ")) > 1:
            component_name = "".join(
                [word.title() for word in component_name.split(" ")]
            )
        self.allowed_attributes |= self.base_attributes
        self.component_name = component_name
        self.parent = settings.APP_COMPONENT
        self.import_name = component_name
        self._children = children
        self._state = state
        self._props = props
        self._variables = variables if variables else []
        self._attrs = self._check_and_camelize_attributes(component_name, **kwargs) | {
            "state": self._state,
            "props": self._props,
        }

    @property
    def children(self) -> Optional[str]:
        """Property returning inner content."""
        return self._children

    @property
    def variables(self) -> str:
        """Property returning string of variables (if any) belonging to given component."""
        return "\n".join(self._variables)

    @property
    def attrs(self) -> str:
        """Property string of given attributes for component"""
        return " ".join([self._format_attr(v, k) for k, v in self._attrs.items()])

    def _make_state_or_prop_attrs(self, attr: Union[BaseState, BaseProps]) -> str:
        placeholder = "" if self.parent.is_functional else js_utils.add_this()
        attr_type = f"{placeholder}{attr.type}"
        return " ".join(
            [
                self._make_key_with_attr(k, f"{attr_type}.{k}")
                for k, v in attr.values.items()
            ]
        )

    @singledispatchmethod
    def _format_attr(self, attr, key) -> None:
        """Generic method for formatting state, props & style.

        A keyword is '_', this will be represented as value only.

        Args:
            key: ...
            attr: ...
        """
        raise AttributeError(
            f"{attr} {key} not in allowed types for {self.component_name}"
        )

    @_format_attr.register(State)
    @_format_attr.register(Props)
    def _(self, attr: Union[State, Props], __: Any) -> str:
        return self._make_state_or_prop_attrs(attr)

    @_format_attr.register(JsObject)
    @_format_attr.register(Object)
    def _(self, attr: Union[JsObject, Object], key: str) -> str:
        if key == "_":
            return f"{js_utils.add_curls(attr.item)}"
        return self._make_key_with_attr(key, attr.item)

    @_format_attr.register(dict)
    @_format_attr.register(Function)
    def _(self, attr: Union[dict[str, Union[str, int]], Function], key: str) -> str:
        return self._make_key_with_attr(key, attr)

    @_format_attr.register(str)
    @_format_attr.register(type(None))
    def _(self, attr: str, key: str) -> str:
        if key == "_":
            return js_utils.add_curls(attr)
        return self._make_key_with_attr(key, f"{attr!r}")

    @_format_attr.register(set)
    def _(self, attr: set[Union[str, int]], key: str) -> str:
        return self._make_key_with_attr(key, js_utils.add_curls(list(attr)[0]))

    @_format_attr.register(bool)
    def _(self, attr: bool, key: str) -> str:
        return self._make_key_with_attr(key, json.dumps(attr))

    @staticmethod
    def _make_key_with_attr(
        key: str, attr: Union[str, dict[str, Union[str, int]], Function]
    ) -> str:
        return f"{key}={js_utils.add_curls(attr)}"

    def _set_default_name(self) -> str:
        return self.__class__.__name__

    def _check_and_camelize_attributes(
        self,
        component_name: str,
        **kwargs: Union[BaseType, Function, str, bool, int, Type[None]],
    ) -> dict:
        """

        Args:
            component_name:
            **kwargs:

        Returns:

        """
        kwargs = {camelize(k): v for k, v in kwargs.items()}

        if prohibited_attrs := set(kwargs.keys()).difference(self.allowed_attributes):
            attributes = ", ".join(prohibited_attrs)
            raise AttributeError(
                f"{component_name} component does not have attribute(s): {attributes}"
            )
        return {k: v for k, v in kwargs.items() if v}

    def render(self) -> str:
        """Renders a .js formatted string of the component."""
        if self._children:
            return f"<{self.component_name} {self.attrs}>{self.children}</{self.component_name}>"
        return f"<{self.component_name} {self.attrs}/>"


class Composite(Component, BaseComposite):
    """Base React Native component with MetaComponent metaclass.

    Args:
        children: Inner content for component.
        state: Dictionary of allowed state values for component.
        functions: Functions for component, passed to top level component.
        kwargs: Arbitrary keyword arguments.

    Attributes:
        _children: Inner content for component.
        _functions: Functions for component, passed to top level component.

    Example:
        composite = Composite(children=[])
    """

    is_context: bool = False  #: Indicates whether component is a context, similar to an inline if-else.
    is_composite: bool = True  #: Indicates whether component may have inner components.
    is_root: bool = False  #: Indicates whether component is a top level component.

    def __init__(
        self,
        children: list[Union[BaseComponent, BaseComposite]] = None,
        functions: Optional[list[str]] = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self._children = children if children else []
        self._functions = functions if functions else []

    @property
    def children(self) -> str:
        """Property returning a string rendition of child components"""
        return "".join(map(lambda x: x.render(), self._children))

    @property
    def functions(self) -> str:
        """Property returning string of variables (if any) belonging to given component."""
        return "".join(self._functions)

    @singledispatchmethod
    def function_formatter(self, functions) -> Any:
        """Generic method for setting functions.

        Args:
            functions: List of functions or a string representing a file name.

        Todos:
            * Finish function_formatter methods.
        """
        raise KeyError("Argument for functions not in allowed types.")

    @function_formatter.register(list)
    def _(self, functions: list[str]) -> None:
        """

        Todos:
            * Implement function formatting.
        Args:
            functions:

        Returns:

        """

    @function_formatter.register(str)
    def _(self, functions: str) -> list[str]:
        path = pathlib.Path().resolve()
        with open(f"./{path}/{functions}", "r", encoding="utf-8") as file:
            content = file.read()
        return content.split("\n")

    def check_functions(self, functions: list[str]) -> None:
        """Checks .js functions for errors.

        Args:
            functions: List of .js functions represented as strings.
        """


class RootComponent(Composite, BaseRootComponent):
    """Root component.

    Args:
        component_name: Name of .js class/function/const for component.
        kwargs: Arbitrary keyword arguments.
    """

    is_composite: bool = False  #: Indicates whether component is represented as composite inside parent component.
    package_root: ClassVar[
        str
    ] = f"./{settings.SOURCE_FOLDER}/components"  #: Default package for component.
    is_root: bool = True  #: Indicates whether component is a top level component.
    is_functional: bool = (
        False  #: Indicates whether component a functional or class component.
    )

    def __init__(
        self,
        children: Optional[list[Union[BaseRootComponent, BaseComposite, None]]] = None,
        extra_imports: Optional[dict[str, Union[str, set[str]]]] = None,
        package_root: Optional[str] = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self._children = children if children else []

        if not package_root:
            package_root = self.package_root
        self.package = f"{package_root}/{self.import_name}.js"
        self._imports: dict[str, Union[str, set]] = {"react": "React"}
        if extra_imports:
            self._imports.update(extra_imports)
        self._set_parent(self)
        # self._state.parent = self
        # self._functions.extend(self._state.functions)
        if self._check_packages():
            bad_dependencies = self._check_packages()
            for dependency in bad_dependencies:
                if not self._install_package(dependency):
                    raise ImportError(f"Package {dependency} must be installed.")
        component_registry[self.component_name] = self

    @property
    def imports(self) -> str:
        """Property returning string of imports (if any) belonging to given component."""
        import_string = ""
        for key, value in self._imports.items():
            if key and "RootNavigation" not in list(value):
                import_string += (
                    f'import {value} from "{key}";\n'.replace("'", "")
                    if value
                    else f'import "{key}"\n'
                )

        return import_string

    @property
    def state(self) -> str:
        """Property returning json string of state (if any) belonging to given component.

        Accesses underlying State instance, if available.
        """
        return self._state.as_json() if self._state else []

    def _set_parent(self, obj: Union[BaseComposite, BaseComponent]) -> None:
        """Sets top level component as root and sets each parent to self.

        Args:
            obj: Component.

        Todos:
            * Refactor + don't access _children attribute for child.
        """

        for child in obj._children:

            child.parent = self

            if (child.is_composite and not child.is_context) or not child.is_composite:
                if child.package not in self._imports:
                    self._imports[child.package] = set()
                self._imports[child.package].add(child.import_name)
            if child.is_composite and not child.is_root:
                self._functions.append(child.functions)
                self._variables.append(child.variables)
                self._set_parent(child)

    def serialize(
        self, as_format: Literal["dict", "json", "pickle"] = "dict"
    ) -> Union[dict[str, object], bytes, str]:
        """Returns component as specified serialization format.

        Args:
            as_format: Specified format, one of `json`, `dict`, or `pickle`. `dict` is default.

        Returns:
            Serialized component.
        """
        if as_format not in ["dict", "json", "pickle"]:
            raise KeyError(
                f"{as_format} not in available formats, pass 'dict', 'json', or 'pickle'."
            )
        serialized_component = {
            "state": self.state,
            "variables": self.variables,
            "functions": self.functions,
            "children": self.children,
            "imports": self.imports,
            "package": self.package,
            "functional": self.is_functional,
            "props": self.allowed_attributes,
            "rendition": self.render(),
        }

        if as_format == "json":
            return json.dumps(serialized_component)
        elif as_format == "pickle":
            return pickle.dumps(serialized_component)
        else:
            return serialized_component

    @classmethod
    def register(cls, management_obj: Union[BaseState, BaseProps]) -> None:
        """Registers state/prop object as functional or class based.

        Args:
            management_obj: State or Prop object.
        """
        management_obj.is_functional = cls.is_functional

    def _check_packages(self) -> list[str]:
        with open(f"{settings.REACT_NATIVE_PATH}/package.json", "r") as file:
            dependencies = json.load(file)["dependencies"]

        return [
            key
            for key in self._imports
            if key not in dependencies
            and not (key.startswith("./") or key.startswith("/"))
        ]

    @staticmethod
    def _install_package(package: str) -> bool:
        sys.stdout.write(f"Dependency package {package} not found.\n")
        install = input("Would you like to install? (y/n): ") == "y"
        if install:
            os.chdir(settings.REACT_NATIVE_PATH)
            os.system(f"expo add {package}")
            return True

        return False

    def render(self) -> str:
        """Renders a .js formatted string of the component."""
        return f"<{self.component_name} {self.attrs}/>"

    def _make_state_or_prop_attrs(self, attr: Union[BaseState, BaseProps]) -> str:
        placeholder = (
            ""
            if self._state and self._state.is_functional
            else f"{js_utils.add_this()}"
        )
        attr_type = f"{placeholder}{attr.type}"
        return " ".join(
            [
                self._make_key_with_attr(k, f"{attr_type}.{k}")
                for k, v in attr.values.items()
            ]
        )
