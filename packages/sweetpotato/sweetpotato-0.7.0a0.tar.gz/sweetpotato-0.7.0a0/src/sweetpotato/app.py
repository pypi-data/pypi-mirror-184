"""Provider for React Native entry.

Todos:
    * Add module docstrings
"""
from typing import Literal, Optional

from sweetpotato.components import View
from sweetpotato.core.base_management import State
from sweetpotato.core.build import Build
from sweetpotato.core.context_wrappers import ContextWrapper
from sweetpotato.core.interfaces import BaseComposite, BaseRootComponent


def default_screen() -> BaseComposite:
    """Default welcome screen for application.

    Returns:
        Welcome screen for application.

    Todo:
        * Add actual welcome screen.
    """
    return View()


class App:
    """Provides methods for interacting with underlying :class:`sweetpotato.core.build.Build` class.

    Args:
        component: Top level component, default is the sweetpotato welcome screen.
        context: Context wrapper for application.
        build: Build tools for application.
        theme: Theme of @eva-design/eva, one of dark, light.
        kwargs: Arbitrary keyword arguments.

    Examples:
        `app = App()`
    """

    def __init__(
        self,
        component: BaseComposite = default_screen(),
        context: ContextWrapper = ContextWrapper(),
        build: Build = Build(),
        state: State = State(),
        theme: Optional[Literal["dark", "light"]] = None,
        is_functional: bool = False,
        **kwargs: dict[str, str],
    ) -> None:
        self._context = context.wrap(
            component=component,
            theme=theme,
            state=state,
            is_functional=is_functional,
            **kwargs,
        )
        self._build = build

    def run(
        self, platform: Optional[Literal["ios", "android", "web", ""]] = ""
    ) -> None:
        """Starts a React Native expo client through a subprocess.

        Args:
            platform: Platform for expo to run application on, one of ios, android, and web.
        """
        self._build.run(platform=platform)

    def publish(
        self,
        platform: Literal["ios", "android", "web"],
        staging: Literal["production", "preview"] = "preview",
    ) -> None:
        """Publishes app to specified platform / application store.

        Args:
            staging: Staging environment for app, default preview.
            platform: Platform for app to be published on.

        """
        self._build.publish(platform=platform, staging=staging)

    def write_files(self) -> None:
        """Writes js files without running the application."""
        self._build.write_files()

    def show(self) -> BaseRootComponent:
        """Returns string .js rendition of application.

        Returns:
            String rendition of application in .js format.
        """
        return self._build.show()

    def __repr__(self) -> str:
        """
        Todos:
            * complete repr logic.

        Returns:

        """
        return f"App({self.show()},)"
