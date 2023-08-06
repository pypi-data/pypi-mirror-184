"""Default sweetpotato settings.

For the full list of settings and their values, see
https://sweetpotato.readthedocs.io/en/latest/settings.html
"""
from pathlib import Path

from pydantic import BaseSettings, HttpUrl

import sweetpotato.functions.authentication_functions as auth_functions
import sweetpotato.functions.navigation_functions as nav_functions


class Settings(BaseSettings):
    """Provides and allows user to override default configuration."""

    # App configuration
    APP_COMPONENT: str = "App"  #: Name of application component, defaults to `'App'`.
    # UI Kitten settings
    USE_UI_KITTEN: bool = False  #: Indicates whether to use @ui-kitten/components.
    USE_SAFE_AREA: bool = False
    UI_KITTEN_REPLACEMENTS: dict = (
        {}
    )  #: Replaces equivalent react native components with @ui-kitten components.
    # Functions
    FUNCTIONS: dict = {}  #: Default generic functions.
    USER_DEFINED_FUNCTIONS: dict = {}  #: Provided UDFs, if any.
    # User defined components
    USER_DEFINED_COMPONENTS: dict = {}  #: Provided user defined components, if any.
    # API settings
    API_URL: HttpUrl = "http://127.0.0.1:8000"  #: URL for API calls.
    # Authentication settings
    USE_AUTHENTICATION: bool = (
        False  #: Indicates whether to use authentication methods.
    )
    LOGIN_COMPONENT: str = "Login"  #: Name of login component, defaults to `'Login'`.
    LOGIN_FUNCTION: str = auth_functions.LOGIN.replace(
        "API_URL", "http://127.0.0.1:8000"
    )  #: Login function for authentication.
    LOGOUT_FUNCTION: str = auth_functions.LOGOUT.replace(
        "API_URL", "http://127.0.0.1:8000"
    )  #: Logout function for authentication.
    SET_CREDENTIALS = (
        auth_functions.SET_CREDENTIALS
    )  #: Credential setting function for authentication.
    STORE_DATA = (
        auth_functions.STORE_DATA
    )  #: Data storage setting function for authentication.
    RETRIEVE_DATA = (
        auth_functions.RETRIEVE_DATA
    )  #: Data retrieval function for authentication.
    STORE_SESSION = (
        auth_functions.STORE_SESSION
    )  #: Session storage function for authentication.
    RETRIEVE_SESSION: str = (
        auth_functions.RETRIEVE_SESSION
    )  #: Session retrieval function for authentication.
    REMOVE_SESSION: str = (
        auth_functions.REMOVE_SESSION
    )  #: Session removal function for authentication.
    TIMEOUT: str = (
        auth_functions.TIMEOUT
    )  #: Generic timeout function for authentication.
    AUTH_FUNCTIONS: dict = {
        "App": auth_functions.LOGIN.replace("API_URL", "http://127.0.0.1:8000"),
        "LOGIN": auth_functions.SET_CREDENTIALS,
    }  #: Dictionary of authentication functions and corresponding components.
    USE_NAVIGATION: bool = False  #: Indicates whether to use @react-navigation/native.
    NAVIGATION_FUNCTIONS: list = [
        v for k, v in nav_functions.__dict__.items() if not k.startswith("__")
    ]
    # React Native settings
    RESOURCE_FOLDER: str = "frontend"  #: Name of expo project resource folder.
    SOURCE_FOLDER: str = "src"  #: Name of expo project component folder.
    REACT_NATIVE_PATH = f"{Path(__file__).resolve().parent.parent}/frontend"  #: Absolute path to expo project.
