"""Contains plugins for authentication.

Todo:
    * Need to refactor the entire module to reflect current functionality.
"""
from typing import Any, Callable, Optional, Union

from sweetpotato.components import Button, TextInput, View
from sweetpotato.config import settings
from sweetpotato.core import js_utils
from sweetpotato.core.base_components import Composite
from sweetpotato.management import State
from sweetpotato.navigation import create_native_stack_navigator


def login() -> dict[str, Any]:
    """Provides default login plugin screen.

    Returns:
        Dictionary of styles and components to be passed to a View or Layout instance.
    """
    state = State(dict(username="", password="", login="", secure_text_entry=True))
    set_password, password = state.use_state("password")
    set_username, username = state.use_state("username")
    set_login, _ = state.use_state("login")
    view_style: dict[str, Union[str, int]] = {
        "justifyContent": "center",
        "alignItems": "center",
        "width": "100%",
        "flex": 1,
    }
    row_style: dict[str, Union[str, int]] = {
        "flexDirection": "row",
        "marginTop": 4,
        "width": "100%",
        "justifyContent": "center",
    }

    username_row = View(
        style=row_style,
        children=[
            TextInput(
                on_change_text=set_username,
                placeholder=username,
            )
        ],
    )

    password_row = View(
        style=row_style,
        children=[
            TextInput(
                secure_text_entry=state["secure_text_entry"],
                on_change_text=set_password,
                placeholder=password,
            )
        ],
    )
    login_screen = dict(
        style=view_style,
        children=[
            username_row,
            password_row,
            Button(title="SUBMIT", on_press=set_login),
        ],
    )
    return login_screen


authentication_state: dict[str, Union[str, bool]] = {
    "username": "",
    "password": "",
    "secure_text_entry": True,
    "is_authenticated": False,
}


class AuthenticationProvider(Composite):
    """Authentication provider for app.

    Args:
        functions: list of functions passes to authentication component.
        login_screen: function returning login screen component.
        login_screen_name: Name of login screen.
        kwargs: Arbitrary keyword arguments.
    """

    is_context: bool = True

    def __init__(
        self,
        functions: list[str] = None,
        login_screen: Optional[Callable[[], dict[str, Any]]] = None,
        login_screen_name: Optional[str] = "Login",
        state: State = State(authentication_state),
        **kwargs,
    ) -> None:
        if functions is None:
            functions = [
                settings.SET_CREDENTIALS,
                settings.LOGIN_FUNCTION,
                settings.STORE_SESSION,
                settings.STORE_DATA,
            ]
        super().__init__(**kwargs)
        login_screen = login if not login_screen else login_screen
        self._state = state
        stack = create_native_stack_navigator()
        stack.screen(
            functions=functions,
            state=state,
            children=[View(**login_screen())],
            screen_name=login_screen_name,
            extra_imports={
                "@react-native-async-storage/async-storage": "AsyncStorage",
                "expo-secure-store": "* as SecureStore",
            },
        )

        self._children.append(stack)

    @property
    def children(self) -> str:
        """Property returning a string rendition of child components.

        Overrides parent method to return a ternary expression.
        """
        value = js_utils.add_class_state("isAuthenticated")
        return js_utils.ternary_expression(value, self._children[0], self._children[1])

    @children.setter
    def children(self, children: list[Composite]) -> None:
        if len(children) != 2:
            raise ValueError(
                f"Exactly two children must exist within an {self.component_name}"
            )
        self._children = children

    def render(self) -> str:
        """Property returning inner content."""
        return self.children
