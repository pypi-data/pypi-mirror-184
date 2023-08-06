"""js_utils provides a collection of utilities for rendering javascript objects.

The camelize and decamelize utilities are copied from https://github.com/nficano/humps/blob/master/humps/main.py.

Todos:
    * Cleanup + add docstrings, typing
"""
import inspect
import json
import re
from collections.abc import Mapping
from functools import singledispatch
from typing import Any, NoReturn, Optional, Type, Union

from sweetpotato.config import settings
from sweetpotato.core.interfaces import BaseComposite, BaseRootComponent


def add_curls(val: str) -> str:
    """Adds those sweet, sweet curly brackets.

    Typical usage is for adding attributes within JS elements,
    ex: <Component val={"my_value"}/>.

    Args:
        val: Value to be surrounded by curly brackets.

    Examples:
        `print(add_curls("...eva"))`
        `{...eva}`

    Returns:
        String with value inside brackets.
    """
    return f"{'{'}{val}{'}'}"


def add_state(val: Optional[str] = "") -> str:
    """Adds state to value.

    Used alone, this is normally for adding the state value to
    data attributes within a functional component.

    Args:
        val: State value.

    Examples:
        `print(add_state("data"))`
        `state.data`

    Returns:
        Value with a `state` string added to the start.
    """
    return f"state{f'.{val}' if val else val}"


def add_props(val: Optional[str] = "") -> str:
    """Adds props to value.

    Used alone, this is normally for adding the props value to
    data attributes within a functional component.

    Args:
        val: Props value.

    Examples:
        `print(add_props("data"))`
        `props.data`

    Returns:
        Value with a `props` string added to the start."""
    return f"props{f'.{val}' if val else val}"


def add_this(val: Optional[str] = "") -> str:
    """Adds this to value/function.

    Used alone, this is normally for adding the `this` value to
    data attributes/methods within a class component.

    Args:
        val: Value or function.

    Examples:
        `print(add_this(add_state()))`
        `this.state`

    Returns:
        Value with a `this` string added to the start."""
    return f"this.{val}"


def add_class_props(val: str) -> str:
    """Adds this.props.

    Used alone, this is normally for adding the `this.props` value to
    data attributes/methods within a class component.

    Args:
        val: Value or function.

    Examples:
        `print(add_class_props(val))`
        `this.props.{val}`

    Returns:
        Value with a `this.props` string added to the start."""
    return add_this(add_props(val))


def add_class_state(val: Optional[str] = "") -> str:
    """Adds this.state.

    Used alone, this is normally for adding the `this.state` value to
    data attributes/methods within a class component.

    Args:
        val: Value or function.

    Examples:
        `print(add_class_state(val))`
        `this.state.{val}`

    Returns:
        Value with a `this.state` string added to the start."""
    return add_this(add_state(val))


def const(const_name: str, value: str) -> str:
    """Renders a javascript const.

    Args:
        const_name: Name of const.
        value: Value of const.

    Examples:
        name = "Tab"\n
        value = "{}"\n`
        print(const(name, value))\n`
        const Tab = {};'

    Returns:
        Const defined with value.
    """
    return f"const {const_name} = {value}"


def ternary_expression(
    condition: str,
    truthy: Union[int, str, bool, Type[None]],
    falsy: Union[int, str, bool, Type[None]],
) -> str:
    """Renders a ternary expression from passed vals.

    Args:
        condition: Variable being evaluated.
        truthy: Expression to be executed if the value is true.
        falsy: Expression to be executed if the value is not true.

    Returns:
        Ternary expression from passed vals
    """

    @singledispatch
    def ternary_value(t_value: Any) -> NoReturn:
        """Generic function for rendering truthy and falsy values.

        See Also:
            https://peps.python.org/pep-0443/

        Args:
            t_value: Any string, integer, boolean, null value or Composite type component.

        Returns:
            Composite type component.
        """
        raise ValueError(f"Type of {type(t_value)} is not allowed.")

    @ternary_value.register(BaseComposite)
    def _(t_value: BaseComposite) -> str:
        return t_value.render()

    @ternary_value.register(int)
    @ternary_value.register(str)
    @ternary_value.register(bool)
    def _(t_value: Union[int, str, bool, Type[None]]) -> str:
        return json.dumps(t_value)

    truthy = ternary_value(truthy)
    falsy = ternary_value(falsy)
    return add_curls(f"{condition} ? {truthy} : {falsy}")


def react_function() -> str:
    """Returns a snakecase rendition of outer function name.

    Returns:
        Snakecase rendition of a function name.
    """
    action, hook = inspect.stack()[1][3].split("_")
    return f"React.{action}{hook.title()}()"


def inline_variable(name: str, props: Optional[Any] = None) -> str:
    """

    Args:
        name:
        props:

    Returns:

    """
    props = add_curls(props) if props else "()"
    return f"{props} => {name}"


def inline_function(
    name: str, props: Optional[Any] = None, value: Optional[Any] = ""
) -> str:
    """

    Args:
        name:
        props:
        value:

    Returns:

    """
    props = add_curls(props) if props else ""
    return f"({props}) => {name}({value})"


def arrow_function(
    name: str, props: Optional[Any] = None, value: Optional[Any] = ""
) -> str:
    """

    Args:
        name:
        props:
        value:

    Returns:

    """
    return f"{name} = {inline_function(name, props, value)}"


def const_arrow_function(
    name: str, props: Optional[Any] = None, value: Optional[Any] = ""
) -> str:
    """

    Args:
        name:
        props:
        value:

    Returns:

    """
    return const(name, inline_function(name, props, value))


def _class_constructor(state: str) -> str:
    """

    Args:
        state:

    Returns:

    """
    class_state = add_class_state()
    internal = f"super(props);{class_state} = {state}"
    return f"constructor(props){add_curls(internal)}"


def _function_constructor(component: BaseRootComponent) -> str:
    """

    Args:
        component:

    Returns:

    """
    return f"{component.state}\n"


def _return(components: Optional[str]) -> str:
    return f"return ({components})"


def _render_return(components: str) -> str:
    """

    Args:
        components:

    Returns:

    """
    return f"render(){add_curls(_return(components))}"


def class_declaration(name: str, react_type: str) -> str:
    """

    Args:
        name:
        react_type:
    """
    default = ""
    if not name.title():
        name = name.title()
    if name == settings.APP_COMPONENT:
        default = "default"

    return f"export {default} class {name} extends React.{react_type.title()}"


def function_declaration(
    component: BaseRootComponent,
) -> str:
    """

    Args:
        component:
    """
    default = ""
    name = component.import_name
    props = "{props}" if component.attrs else ""
    if not name.title():
        name = name.title()
    if name == settings.APP_COMPONENT:
        default = "default"

    return f"export {default} function {name}({props})"


def component_header(component: BaseRootComponent) -> str:
    """

    Args:
        component:

    Returns:

    """
    return f"{component.imports}\n{component.variables}\n"


def function_header(component: BaseRootComponent) -> str:
    """

    Args:
        component:

    Returns:

    """
    return f"{component.imports}\n{component.variables}\n"


def component_body(component: BaseRootComponent) -> str:
    """

    Args:
        component:

    Returns:

    """
    children = _render_return(component.children)
    constructor = _class_constructor(component.state)
    return f"{constructor}{component.functions}{children}"


def function_body(component: BaseRootComponent) -> str:
    """

    Args:
        component:

    Returns:

    """
    children = _return(component.children)
    return f"{component.functions}{children}"


def class_component(component: BaseRootComponent) -> str:
    """

    Args:
        component:

    Returns:

    """
    header = component_header(component)
    class_header = class_declaration(component.import_name, "component")
    body = add_curls(component_body(component))
    return f"{header}{class_header}{body}"


def functional_component(component: BaseRootComponent) -> str:
    """

    Args:
        component:

    Returns:

    """
    header = function_header(component)
    function_head = function_declaration(component)
    body = add_curls(function_body(component))
    return f"{header}{function_head}{body}"


def context_component(component: BaseRootComponent) -> str:
    """

    Args:
        component:

    Returns:

    """
    return f"{component.imports}\n{component.functions}"


def react_component(component: BaseRootComponent) -> str:
    """

    Args:
        component:

    Returns:

    """
    if component.is_context:
        return context_component(component)
    if component.is_functional:
        return functional_component(component)

    return class_component(component)


ACRONYM_RE = re.compile(r"([A-Z]+)$|([A-Z]+)(?=[A-Z\d])")
PASCAL_RE = re.compile(r"([^\-_\s]+)")
SPLIT_RE = re.compile(r"([\-_\s]*[A-Z]+?[^A-Z\-_\s]*[\-_\s]*)")
UNDERSCORE_RE = re.compile(r"(?<=[^\-_\s])[\-_\s]+[^\-_\s]")


def camelize(str_or_iter: Union[list, dict, str]) -> Union[list, dict, str]:
    """Convert a string, dict, or list of dicts to camel case.

    Args:
        str_or_iter: A string or iterable

    Returns:
        Camel case string, dictionary, or list of dictionaries.
    """
    if isinstance(str_or_iter, (list, Mapping)):
        return _process_keys(str_or_iter, camelize)

    s = str(str_or_iter if str_or_iter else "")
    if s.isupper() or s.isnumeric():
        return str_or_iter

    if len(s) != 0 and not s[:2].isupper():
        s = s[0].lower() + s[1:]

    return UNDERSCORE_RE.sub(lambda m: m.group(0)[-1].upper(), s)


def decamelize(str_or_iter: Union[list, dict, str]) -> Union[list, dict, str]:
    """Convert a string, dict, or list of dicts to snake case.

    Args:
        str_or_iter: A string or iterable

    Returns:
        Snake cased string, dictionary, or list of dictionaries.
    """
    if isinstance(str_or_iter, (list, Mapping)):
        return _process_keys(str_or_iter, decamelize)

    s = str(str_or_iter if str_or_iter else "")
    if s.isupper() or s.isnumeric():
        return str_or_iter
    fixed_abbr = ACRONYM_RE.sub(lambda m: m.group(0).title(), s)
    return "_".join(s for s in SPLIT_RE.split(fixed_abbr) if s).lower()


def _process_keys(str_or_iter, fn):
    if isinstance(str_or_iter, list):
        return [_process_keys(k, fn) for k in str_or_iter]
    if isinstance(str_or_iter, Mapping):
        return {fn(k): _process_keys(v, fn) for k, v in str_or_iter.items()}
    return str_or_iter
