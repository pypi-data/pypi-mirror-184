"""Provides mixin classes for component customization.

Examples:

    * Add examples.

Todos:
    * Implement mixins for custom component.
"""
from typing import Optional

from sweetpotato.core.base_components import RootComponent


class ComponentMixin(RootComponent):
    """External component wrapper."""


class PropsMixin:
    """Mixin customization methods.

    Meant to be subclassed with RootComponent class.

    Examples:

        from sweetpotato.core.base import RootComponent
        from sweetpotato.mixins import CustomMixin

        class CustomComponent(ComponentMixin, PropsMixin):
            extra_props = {"custom_prop"}
    """

    extra_attributes: set[
        str
    ] = set()  #: Set of extra allowed props for component, set by user.

    def __init__(self) -> None:
        if self.extra_attributes:
            # noinspection PyUnresolvedReferences
            self.allowed_attributes.update(self.extra_attributes)


class JsComponentMixin:
    """Allows a user to use a component within a .js file or string.

    Args:
        file_name: Name of component file.
        component_string: JS string representation of component.

    Todos:
        * Finish class/methods/typings.
    """

    component_internals: dict = {}

    def __init__(
        self,
        file_name: Optional[str] = None,
        component_string: Optional[str] = None,
    ) -> None:
        if file_name and component_string:
            raise KeyError(
                "Only one of file_name, component_string may be passed, not both."
            )
        self.read_file(file_name=file_name) if file_name else self.read_string(
            component_string=component_string
        )

    def read_file(self, file_name: str) -> None:
        """

        Args:
            file_name:
        """
        with open(file_name, "r") as file:
            component_string = [
                line for line in file.readlines() if not self._is_commented(line)
            ]
        self._make_component(component_string=component_string)

    def read_string(self, component_string: str) -> None:
        """

        Args:
            component_string:
        """
        component_string = component_string.strip().split()
        self._make_component(component_string=component_string)

    def _make_component(self, component_string: list[str]) -> None:
        raise NotImplementedError

    @staticmethod
    def _is_commented(line: str) -> bool:
        line = line.strip().split()
        if line and line[0] == "//":
            return True
        return False

    @staticmethod
    def _add_component_name(lines: list[str]) -> Optional[str]:
        for line in lines:
            if "export" in line:
                line_split = line.split()
                for value in line_split:
                    if value.istitle() and not value.startswith("React"):
                        return value.replace("()", "")
        raise ValueError("Improperly formatted React component. Check your .js file.")

    @staticmethod
    def _add_is_functional(line: str) -> bool:
        if "class" not in line:
            return True
        return False

    @staticmethod
    def _add_class_children(line: list[str]) -> None:
        raise NotImplementedError

    @staticmethod
    def _add_functional_children(line: list[str]) -> None:
        raise NotImplementedError

    @staticmethod
    def _add_imports(lines: list[str]) -> dict[str, set]:
        """Adds imports.

        Args:
            lines:

        Returns:

        Todos:
            * Add checks for varying import statements.
        """
        import_strings = [line for line in lines if "import" in line]
        import_dict: dict = {}
        for string in import_strings:
            if '"react"' not in string:
                split_string = "".join(
                    package.replace('"', "").replace(";", "")
                    for package in string.split()
                    if package.startswith('"')
                )
                if split_string not in import_dict and split_string != '"react";':
                    import_dict[split_string] = set()
                imports = (
                    string[1 + string.find("{") : string.rfind("}")]
                    .replace(",", "")
                    .split()
                )
                for val in imports:
                    import_dict[split_string].add(val)

        return import_dict
