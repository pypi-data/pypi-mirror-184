"""Abstractions of React Native core components.

See the `React Native docs <https://reactnative.dev/docs/components-and-apis>`_ for more.

Todo:
    * Add examples to all classes.
"""
from __future__ import annotations

from typing import Final, Literal, Optional, Type, Union

from pydantic import HttpUrl
from pydantic.color import Color

from sweetpotato.core.base_components import Component, Composite
from sweetpotato.core.base_management import Function
from sweetpotato.core.interfaces import BaseFunction, BaseType
from sweetpotato.props.components_props import (
    ACTIVITY_INDICATOR_PROPS,
    BUTTON_PROPS,
    FLAT_LIST_PROPS,
    IMAGE_PROPS,
    SAFE_AREA_PROVIDER_PROPS,
    SCROLL_VIEW_PROPS,
    TEXT_INPUT_PROPS,
    TEXT_PROPS,
    TOUCHABLE_OPACITY_PROPS,
    VIEW_PROPS,
)


class ActivityIndicator(Component):
    """React Native ActivityIndicator component.

    See https://reactnative.dev/docs/activityindicator.
    """

    allowed_attributes: Final[
        set[str]
    ] = ACTIVITY_INDICATOR_PROPS  #: Set of allowed attributes for component.

    def __init__(
        self,
        animating: Optional[bool] = None,
        color: Optional[Color] = None,
        hides_when_stopped: Optional[bool] = None,
        size: Optional[int] = None,
        *args: Union[BaseType, str, None],
        **kwargs: Union[BaseType, Function, str, bool, int, Type[None]],
    ):
        super().__init__(
            animating=animating,
            color=color,
            hides_when_stopped=hides_when_stopped,
            size=size,
            *args,
            **kwargs,
        )


class Text(Component):
    """React Native Text component.

    See https://reactnative.dev/docs/text.

    Args:
        text: Inner content for Text component inplace of children.
        kwargs: Arbitrary allowed attributes for component.

    Example:
        text = Text(text="foo")
    """

    allowed_attributes: Final[
        set[str]
    ] = TEXT_PROPS  #: Set of allowed attributes for component.

    def __init__(
        self,
        text: Optional[str] = None,
        accessible: Optional[bool] = None,
        accessibility_hint: Optional[str] = None,
        accessibility_language: Optional[str] = None,
        accessibility_label: Optional[str] = None,
        accessibility_role: Optional[str] = None,
        accessibility_state: Optional[str] = None,
        accessibility_actions: Optional[str] = None,
        on_accessibility_action: Optional[Union[BaseFunction, str]] = None,
        adjusts_font_size_to_fit: Optional[bool] = None,
        allow_font_scaling: Optional[bool] = None,
        android_hyphenation_frequency: Optional[
            Literal["none", "normal", "full"]
        ] = None,
        data_detector_type: Optional[
            Literal["phoneNumber", "link", "email", "none", "all"]
        ] = None,
        disabled: Optional[bool] = None,
        ellipsize_mode: Optional[Literal["head", "middle", "tail", "clip"]] = None,
        max_font_size_multiplier: Optional[int] = None,
        minimum_font_scale: Optional[int] = None,
        number_of_lines: Optional[int] = None,
        on_layout: Optional[str] = None,
        on_long_press: Optional[str] = None,
        on_move_should_set_responder: Optional[str] = None,
        on_press: Optional[str] = None,
        on_responder_grant: Optional[str] = None,
        on_responder_move: Optional[str] = None,
        on_responder_release: Optional[str] = None,
        on_responder_terminate: Optional[str] = None,
        on_responder_termination_request: Optional[str] = None,
        on_start_should_set_responder_capture: Optional[str] = None,
        on_text_layout: Optional[str] = None,
        press_retention_offset: Optional[str] = None,
        selectable: Optional[bool] = None,
        selection_color: Optional[Color] = None,
        style: Optional[dict[str, Union[int, str]]] = None,
        suppress_highlighting: Optional[bool] = None,
        text_break_strategy: Optional[str] = None,
        *args: Optional[Union[BaseType, str]],
        **kwargs: dict[str, str],
    ) -> None:
        super().__init__(
            children=text,
            accessibility_hint=accessibility_hint,
            accessibility_language=accessibility_language,
            accessibility_label=accessibility_label,
            accessibility_role=accessibility_role,
            accessibility_state=accessibility_state,
            accessibility_actions=accessibility_actions,
            on_accessibility_action=on_accessibility_action,
            accessible=accessible,
            adjusts_font_size_to_fit=adjusts_font_size_to_fit,
            allow_font_scaling=allow_font_scaling,
            android_hyphenation_frequency=android_hyphenation_frequency,
            data_detector_type=data_detector_type,
            disabled=disabled,
            ellipsize_mode=ellipsize_mode,
            max_font_size_multiplier=max_font_size_multiplier,
            minimum_font_scale=minimum_font_scale,
            number_of_lines=number_of_lines,
            on_layout=on_layout,
            on_long_press=on_long_press,
            on_move_should_set_responder=on_move_should_set_responder,
            on_press=on_press,
            on_responder_grant=on_responder_grant,
            on_responder_move=on_responder_move,
            on_responder_release=on_responder_release,
            on_responder_terminate=on_responder_terminate,
            on_responder_termination_request=on_responder_termination_request,
            on_start_should_set_responder_capture=on_start_should_set_responder_capture,
            on_text_layout=on_text_layout,
            press_retention_offset=press_retention_offset,
            selectable=selectable,
            selection_color=selection_color,
            style=style,
            suppress_highlighting=suppress_highlighting,
            text_break_strategy=text_break_strategy,
            *args,
            **kwargs,
        )


class TextInput(Component):
    """React Native TextInput component.

    See https://reactnative.dev/docs/textinput.
    """

    allowed_attributes: Final[
        set[str]
    ] = TEXT_INPUT_PROPS  #: Set of allowed props for component.

    def __init__(
        self,
        on_key_pre_ime: Optional[str] = None,
        allow_font_scaling: Optional[bool] = None,
        auto_capitalize: Optional[bool] = None,
        auto_complete: Optional[bool] = None,
        auto_correct: Optional[bool] = None,
        auto_focus: Optional[bool] = None,
        blur_on_submit: Optional[bool] = None,
        caret_hidden: Optional[bool] = None,
        clear_button_mode: Optional[bool] = None,
        clear_text_on_focus: Optional[bool] = None,
        context_menu_hidden: Optional[bool] = None,
        data_detector_types: Optional[str] = None,
        default_value: Optional[str] = None,
        cursor_color: Optional[Color] = None,
        disable_fullscreen_ui: Optional[bool] = None,
        editable: Optional[bool] = None,
        enables_return_key_automatically: Optional[bool] = None,
        important_for_autofill: Optional[bool] = None,
        inline_image_left: Optional[Image] = None,
        inline_image_padding: Optional[int] = None,
        input_accessory_view_id: Optional[str] = None,
        keyboard_appearance: Optional[str] = None,
        keyboard_type: Optional[str] = None,
        max_font_size_multiplier: Optional[int] = None,
        max_length: Optional[int] = None,
        multiline: Optional[str] = None,
        number_of_lines: Optional[int] = None,
        on_blur: Optional[str] = None,
        on_change: Optional[str] = None,
        on_change_text: Optional[Union[str, Function]] = None,
        on_content_size_change: Optional[str] = None,
        on_end_editing: Optional[str] = None,
        on_press_in: Optional[str] = None,
        on_press_out: Optional[str] = None,
        on_focus: Optional[str] = None,
        on_key_press: Optional[str] = None,
        on_layout: Optional[str] = None,
        on_scroll: Optional[str] = None,
        on_selection_change: Optional[str] = None,
        on_submit_editing: Optional[str] = None,
        placeholder: Optional[str] = None,
        placeholder_text_color: Optional[Color] = None,
        return_key_label: Optional[str] = None,
        return_key_type: Optional[str] = None,
        reject_responder_termination: Optional[str] = None,
        scroll_enabled: Optional[bool] = None,
        secure_text_entry: Optional[bool] = None,
        selection: Optional[str] = None,
        selection_color: Optional[Color] = None,
        select_text_on_focus: Optional[bool] = None,
        show_soft_input_on_focus: Optional[bool] = None,
        spell_check: Optional[str] = None,
        text_align: Optional[str] = None,
        text_content_type: Optional[str] = None,
        password_rules: Optional[str] = None,
        style: Optional[str] = None,
        text_break_strategy: Optional[str] = None,
        underline_color_android: Optional[Color] = None,
        value: Optional[Union[str, int]] = None,
        *args: Optional[Union[BaseType, str]],
        **kwargs: dict[str, str],
    ):
        super().__init__(
            on_key_pre_ime=on_key_pre_ime,
            allow_font_scaling=allow_font_scaling,
            auto_capitalize=auto_capitalize,
            auto_complete=auto_complete,
            auto_correct=auto_correct,
            auto_focus=auto_focus,
            blur_on_submit=blur_on_submit,
            caret_hidden=caret_hidden,
            clear_button_mode=clear_button_mode,
            clear_text_on_focus=clear_text_on_focus,
            context_menu_hidden=context_menu_hidden,
            data_detector_types=data_detector_types,
            default_value=default_value,
            cursor_color=cursor_color,
            disable_fullscreen_ui=disable_fullscreen_ui,
            editable=editable,
            enables_return_key_automatically=enables_return_key_automatically,
            important_for_autofill=important_for_autofill,
            inline_image_left=inline_image_left,
            inline_image_padding=inline_image_padding,
            input_accessory_view_id=input_accessory_view_id,
            keyboard_appearance=keyboard_appearance,
            keyboard_type=keyboard_type,
            max_font_size_multiplier=max_font_size_multiplier,
            max_length=max_length,
            multiline=multiline,
            number_of_lines=number_of_lines,
            on_blur=on_blur,
            on_change=on_change,
            on_change_text=on_change_text,
            on_content_size_change=on_content_size_change,
            on_end_editing=on_end_editing,
            on_press_in=on_press_in,
            on_press_out=on_press_out,
            on_focus=on_focus,
            on_key_press=on_key_press,
            on_layout=on_layout,
            on_scroll=on_scroll,
            on_selection_change=on_selection_change,
            on_submit_editing=on_submit_editing,
            placeholder=placeholder,
            placeholder_text_color=placeholder_text_color,
            return_key_label=return_key_label,
            return_key_type=return_key_type,
            reject_responder_termination=reject_responder_termination,
            scroll_enabled=scroll_enabled,
            secure_text_entry=secure_text_entry,
            selection=selection,
            selection_color=selection_color,
            select_text_on_focus=select_text_on_focus,
            show_soft_input_on_focus=show_soft_input_on_focus,
            spell_check=spell_check,
            text_align=text_align,
            text_content_type=text_content_type,
            password_rules=password_rules,
            style=style,
            text_break_strategy=text_break_strategy,
            underline_color_android=underline_color_android,
            value=value,
            *args,
            **kwargs,
        )


class Button(Composite):
    """React Native Button component.

    See https://reactnative.dev/docs/button.

    Example:
        button = Button(title="foo")
    """

    allowed_attributes: Final[
        set[str]
    ] = BUTTON_PROPS  #: Set of allowed props for component.

    def __init__(
        self,
        title: str,
        on_press: Union[BaseFunction, str],
        accessibility_label: Optional[str] = None,
        accessibility_language: Optional[str] = None,
        accessibility_actions: Optional[list] = None,
        on_accessibility_action: Optional[Union[BaseFunction, str]] = None,
        color: Optional[Color] = None,
        has_tv_preferred_focus: Optional[bool] = None,
        next_focus_down: Optional[int] = None,
        next_focus_forward: Optional[int] = None,
        next_focus_left: Optional[int] = None,
        next_focus_right: Optional[int] = None,
        next_focus_up: Optional[int] = None,
        touch_sound_disabled: Optional[bool] = None,
        disabled: Optional[bool] = None,
        *args: Optional[Union[BaseType, str]],
        **kwargs: dict[str, str],
    ):
        super().__init__(
            title=title,
            on_press=on_press,
            accessibility_label=accessibility_label,
            accessibility_language=accessibility_language,
            accessibility_actions=accessibility_actions,
            on_accessibility_action=on_accessibility_action,
            color=color,
            has_tv_preferred_focus=has_tv_preferred_focus,
            next_focus_down=next_focus_down,
            next_focus_forward=next_focus_forward,
            next_focus_left=next_focus_left,
            next_focus_right=next_focus_right,
            next_focus_up=next_focus_up,
            touch_sound_disabled=touch_sound_disabled,
            disabled=disabled,
            *args,
            **kwargs,
        )


class Image(Component):
    """React Native Image component.

    See https://reactnative.dev/docs/image.

    Example:
        image = Image(source={"uri": image_source})
    """

    allowed_attributes: Final[
        set[str]
    ] = IMAGE_PROPS  #: Set of allowed allowed_attributes for component.

    def __init__(
        self,
        source: Optional[dict[Literal["uri"], Union[HttpUrl, str]]],
        accessible: Optional[bool] = None,
        accessibility_label: Optional[str] = None,
        blur_radius: Optional[int] = None,
        cap_insets: Optional[int] = None,
        default_source: Optional[str] = None,
        fade_duration: Optional[int] = None,
        loading_indicator_source: Optional[str] = None,
        on_error: Optional[str] = None,
        on_layout: Optional[str] = None,
        on_load: Optional[str] = None,
        on_load_end: Optional[str] = None,
        on_load_start: Optional[str] = None,
        on_partial_load: Optional[str] = None,
        on_progress: Optional[str] = None,
        progressive_rendering_enabled: Optional[bool] = None,
        resize_method: Optional[Literal["auto", "resize", "scale"]] = None,
        resize_mode: Optional[
            Literal["cover", "contain", "stretch", "repeat", "center"]
        ] = None,
        *args: Optional[Union[BaseType, str]],
        **kwargs: Optional[Union[BaseType, Function, str]],
    ) -> None:
        super().__init__(
            source=source,
            accessible=accessible,
            accessibility_label=accessibility_label,
            blur_radius=blur_radius,
            cap_insets=cap_insets,
            default_source=default_source,
            fade_duration=fade_duration,
            loading_indicator_source=loading_indicator_source,
            on_error=on_error,
            on_layout=on_layout,
            on_load=on_load,
            on_load_end=on_load_end,
            on_load_start=on_load_start,
            on_partial_load=on_partial_load,
            on_progress=on_progress,
            progressive_rendering_enabled=progressive_rendering_enabled,
            resize_method=resize_method,
            resize_mode=resize_mode,
            *args,
            **kwargs,
        )


class FlatList(Component):
    """React Native FlatList component.

    See https://reactnative.dev/docs/flatlist.
    """

    allowed_attributes: Final[
        set[str]
    ] = FLAT_LIST_PROPS  #: Set of allowed props for component.


class SafeAreaProvider(Composite):
    """React Native react-native-safe-area-context SafeAreaProvider component.

    See https://docs.expo.dev/versions/latest/sdk/safe-area-context/.
    """

    package: str = "react-native-safe-area-context"  #: Default package for component.
    allowed_attributes: set[
        str
    ] = "react-native-safe-area-context"  #: Default package for component.
    allowed_attributes: Final[
        set[str]
    ] = SAFE_AREA_PROVIDER_PROPS  #: Set of allowed props for component.


class ScrollView(Component):
    """React Native ScrollView component.

    See https://reactnative.dev/docs/scrollview.
    """

    allowed_attributes: set[
        str
    ] = SCROLL_VIEW_PROPS  #: Set of allowed props for component.


class StyleSheet:
    """React Native StyleSheet component.

    See https://reactnative.dev/docs/stylesheet.

    Args:
        styles: Dictionary of dicts consisting of styles.

    Example:
        styles = StyleSheet.create({
            "container": {"flex": 1, "justifyContent": "center", "alignItems": "center"}
        })

    Todo:
        * Implement compose and flatten methods.
    """

    def __init__(self, styles: dict[str, dict[str, Union[str, int]]]) -> None:
        self.styles = styles

    @classmethod
    def create(cls, styles: dict[str, dict[str, Union[str, int]]]) -> StyleSheet:
        """Method for creating stylesheet for use with components.

        Args:
            styles: Dictionary of dicts consisting of styles.
        """
        return cls(styles)

    def compose(self) -> None:
        """Not implemented."""
        raise NotImplementedError

    def flatten(self) -> None:
        """Not implemented."""
        raise NotImplementedError

    def __getattr__(self, item: str) -> dict[str, Union[str, int]]:
        return self.styles[item]


class TouchableOpacity(Composite):
    """React Native TouchableOpacity component.

    See https://reactnative.dev/docs/touchableopacity.
    """

    allowed_attributes: Final[
        set[str]
    ] = TOUCHABLE_OPACITY_PROPS  #: Set of allowed props for component.


class View(Composite):
    """React Native View component.

    See https://reactnative.dev/docs/view.
    """

    allowed_attributes: Final[
        set[str]
    ] = VIEW_PROPS  #: Set of allowed props for component.
