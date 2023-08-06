"""Contains classes based on UI Kitten components.

See `UI Kitten <https://akveo.github.io/react-native-ui-kitten/docs/components/components-overview>`_
"""
from typing import Optional, Union

from sweetpotato.core.base_components import Component, Composite
from sweetpotato.core.interfaces import BaseComponent, BaseComposite
from sweetpotato.core.js_objects import Object
from sweetpotato.props.ui_kitten_props import (
    APPLICATION_PROVIDER_PROPS,
    BUTTON_PROPS,
    ICON_REGISTRY_PROPS,
    INPUT_PROPS,
    LAYOUT_PROPS,
    TEXT_PROPS,
)


class IconRegistry(Component):
    """Implementation of ui-kitten IconRegistry component.

    See `<https://akveo.github.io/react-native-ui-kitten/docs/components/icon/overview#icon>`_
    """

    package: str = "@ui-kitten/components"  #: Default package for component.
    allowed_attributes: set[
        str
    ] = ICON_REGISTRY_PROPS  #: Set of allowed allowed_attributes for component.


class ApplicationProvider(Composite):
    """Implementation of ui-kitten ApplicationProvider component.

    See https://akveo.github.io/react-native-ui-kitten/docs/components/application-provider

    Args:
        kwargs: Arbitrary keyword arguments.
    """

    package: str = "@ui-kitten/components"  #: Default package for component.
    allowed_attributes: set[
        str
    ] = APPLICATION_PROVIDER_PROPS  #: Set of allowed allowed_attributes for component.

    def __init__(
        self,
        children: list[Union[BaseComponent, BaseComposite]],
        theme: set[str],
        **kwargs,
    ) -> None:
        super().__init__(theme=theme, **kwargs)
        eva = Object(item="...eva")
        eva_icons = Object(item="EvaIconsPack")
        self._children = [IconRegistry(icons=eva_icons, _=eva), children[0]]


class Text(Component):
    """Implementation of ui-kitten Text component.

    See https://akveo.github.io/react-native-ui-kitten/docs/components/text.
    """

    package: str = "@ui-kitten/components"  #: Default package for component.
    allowed_attributes: set[
        str
    ] = TEXT_PROPS  #: Set of allowed allowed_attributes for component.

    def __init__(self, text: Optional[str] = None, **kwargs) -> None:
        super().__init__(children=text, **kwargs)


class Button(Composite):
    """Implementation of ui-kitten Button component.

    See https://akveo.github.io/react-native-ui-kitten/docs/components/button.
    """

    package: str = "@ui-kitten/components"  #: Default package for component.
    allowed_attributes: set[
        str
    ] = BUTTON_PROPS  #: Set of allowed allowed_attributes for component.

    def __init__(self, **kwargs) -> None:
        super().__init__(children=[Text(text=kwargs.pop("title"))], **kwargs)


class Input(Component):
    """Implementation of ui-kitten Input component.

    See https://akveo.github.io/react-native-ui-kitten/docs/components/input.
    """

    package: str = "@ui-kitten/components"  #: Default package for component.
    allowed_attributes: set[
        str
    ] = INPUT_PROPS  #: Set of allowed allowed_attributes for component.


class Layout(Composite):
    """Implementation of ui-kitten Layout component.

    See https://akveo.github.io/react-native-ui-kitten/docs/components/layout.
    """

    package: str = "@ui-kitten/components"  #: Default package for component.
    allowed_attributes: set[str] = LAYOUT_PROPS  #: Set of allowed props for component.
