"""
Allowed props for react-navigation components.
"""

NAVIGATION_CONTAINER_PROPS: set[str] = {
    "children",
    "ref",
}  #: Default allowed props for NavigationContainer component.

NATIVE_STACK_NAVIGATOR_PROPS: set[str] = {
    "name"
}  #: Default allowed props for StackNavigator component.

TAB_PROPS: set[str] = {"name"}  #: Default allowed props for TabNavigator component.

BOTTOM_TAB_NAVIGATOR_PROPS: set[str] = {
    "name"
}  #: Additional default allowed props for TabNavigator component.

DRAWER_NAVIGATOR_PROPS: set[
    str
] = set()  #: Default allowed props for DrawerNavigator component.

SCREEN_PROPS: set[str] = {
    "children",
    "functions",
    "state",
    "screen_name",
    "screen_type",
    "prop_functions",
}  #: Default allowed props for Screen component.

BASE_NAVIGATOR_PROPS: set[
    str
] = set()  #: Default allowed props for BaseNavigator component.

ROOT_NAVIGATION_PROPS: set[
    str
] = set()  #: Default allowed props for RootNavigation component.
