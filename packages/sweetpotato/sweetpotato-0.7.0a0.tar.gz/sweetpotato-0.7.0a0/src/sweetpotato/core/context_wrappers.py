"""
Todo:
    * Add docstrings for all classes & methods.
    * Add typing.
"""
from abc import ABC, abstractmethod
from typing import Any, Optional

from sweetpotato.components import SafeAreaProvider
from sweetpotato.config import settings
from sweetpotato.core.base_components import RootComponent
from sweetpotato.core.base_management import State
from sweetpotato.core.interfaces import BaseComposite
from sweetpotato.core.js_objects import Object
from sweetpotato.navigation import NavigationContainer
from sweetpotato.plugins.authentication import AuthenticationProvider
from sweetpotato.ui_kitten import ApplicationProvider


class Wrapper(ABC):
    """Wrapping interface for components."""

    @abstractmethod
    def wrap(self, component: BaseComposite, **kwargs: Any) -> BaseComposite:
        """Abstract component wrapping."""
        return component


class UIKittenWrapper(Wrapper):
    """Adds UI Kitten support to app."""

    def wrap(self, component: BaseComposite, **kwargs) -> BaseComposite:
        """Wraps component in UI Kitten if enabled.

        Args:
            component: ...

        Returns:
            Composite.
        """
        if settings.USE_UI_KITTEN:
            theme = kwargs.pop("theme", None)
            if not theme:
                raise KeyError("UI Kitten must be provided a theme.")
            component = ApplicationProvider(
                children=[component], theme={f"...eva.{theme}"}
            )
        return super().wrap(component, **kwargs)


class AuthenticationWrapper(Wrapper):
    """Adds authentication plugins to app.

    Todo:
        * Add docstrings.
    """

    def wrap(self, component: BaseComposite, **kwargs) -> BaseComposite:
        """Wraps component in AuthenticationProvider if enabled.

        Args:
            component (Composite): ...

        Returns:
            Composite.
        """
        if settings.USE_AUTHENTICATION:
            component = AuthenticationProvider(children=[component])
        return super().wrap(component, **kwargs)


class NavigationWrapper(Wrapper):
    """Adds NavigationContainer component to app and gives navigation capability.

    Todo:
        * Add docstrings.
    """

    def wrap(self, component: BaseComposite, **kwargs) -> BaseComposite:
        """Wraps component in NavigationContainer if enabled.

        Args:
            component (Composite): ...

        Returns:
            Composite.
        """
        if settings.USE_NAVIGATION:
            component = NavigationContainer(
                children=[component],
                ref=Object(item="RootNavigation"),
            )
        return super().wrap(component, **kwargs)


class SafeAreaWrapper(Wrapper):
    """Adds react-native-safe-area-context SafeAreaProvider component to app.


    Todo:
        * Add docstrings
    """

    def wrap(self, component: BaseComposite, **kwargs) -> BaseComposite:
        """Wraps component in SafeAreaProvider.

        Args:
            component (Composite): ...

        Returns:
            Composite.
        """
        if settings.USE_SAFE_AREA:
            component = SafeAreaProvider(children=[component])
        return super().wrap(component, **kwargs)


class ContextWrapper(
    AuthenticationWrapper, SafeAreaWrapper, UIKittenWrapper, NavigationWrapper
):
    """Checks for and adds navigation, authentication, and ui-kitten contexts.

    Todo:
        * Add docstrings
    """

    def wrap(
        self,
        component: Optional[BaseComposite],
        state: Optional[State] = None,
        is_functional: Optional[bool] = False,
        **kwargs,
    ) -> RootComponent:
        """Checks and wraps component in provided wrappers, if configured.

        Args:
            is_functional: ...
            state: ...
            component (Composite): ...
            kwargs: ...

        Returns:
            Composite.
        """
        if not state and settings.USE_AUTHENTICATION:
            state = State(
                {
                    "isAuthenticated": False,
                }
            )
        extra_imports = {}
        if settings.USE_NAVIGATION:
            extra_imports.update(
                {
                    "react-native-gesture-handler": "",
                    "./src/components/RootNavigation": "* as RootNavigation",
                }
            )
        if settings.USE_UI_KITTEN:
            extra_imports.update(
                {
                    "@eva-design/eva": "* as eva",
                    "@ui-kitten/eva-icons": {"EvaIconsPack"},
                }
            )
        state.is_functional = is_functional
        if not kwargs.get("component_name"):
            kwargs["component_name"] = settings.APP_COMPONENT
        if not kwargs.get("package_root", ""):
            kwargs["package_root"] = f"{settings.REACT_NATIVE_PATH}/"
        theme = kwargs.pop("theme")
        component = RootComponent(
            children=[super().wrap(component, theme=theme)],
            state=state,
            extra_imports=extra_imports,
            **kwargs,
        )
        component.is_functional = is_functional
        return component
