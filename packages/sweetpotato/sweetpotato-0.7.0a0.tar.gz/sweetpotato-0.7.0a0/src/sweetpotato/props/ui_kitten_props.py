"""
Allowed allowed_attributes for ui-kitten components.
"""
ICON_REGISTRY_PROPS: set[str] = {
    "icons"
}  #: Default allowed allowed_attributes for IconRegistry component.

APPLICATION_PROVIDER_PROPS: set[str] = {
    "theme",
    "children",
}  #: Default allowed allowed_attributes for ApplicationProvider component.

LAYOUT_PROPS: set[str] = {
    "children",
    "style",
}  #: Default allowed allowed_attributes for Layout component.

TEXT_PROPS: set[str] = {
    "text"
}  #: Default allowed allowed_attributes for Text component.

BUTTON_PROPS: set[str] = {
    "title",
    "onPress",
}  #: Default allowed allowed_attributes for Button component.

INPUT_PROPS: set[str] = {
    "placeholder",
    "value",
    "onChangeText",
    "secureTextEntry",
}  #: Default allowed allowed_attributes for Input component.
