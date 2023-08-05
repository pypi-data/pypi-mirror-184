# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class LanguageSelect(Component):
    """A LanguageSelect component.
Component description

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional)

- dataValue (string; optional)

- direction (a value equal to: 'top', 'bottom'; optional)

- disabledValue (string; optional)

- key (string; optional)

- multiple (boolean; optional)

- multipleLabel (string; optional)

- options (list of dicts; required)

    `options` is a list of dicts with keys:

    - description (string; optional)

    - key (string; optional)

    - label (string; required)

    - title (string; optional)

    - value (string; required)

- tooltipPosition (a value equal to: 'top', 'topLeft', 'topRight', 'bottom', 'bottomLeft', 'bottomRight', 'left', 'right'; optional)

- value (string | list of strings; optional)

- width (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'LanguageSelect'
    @_explicitize_args
    def __init__(self, options=Component.REQUIRED, onClick=Component.UNDEFINED, multiple=Component.UNDEFINED, multipleLabel=Component.UNDEFINED, value=Component.UNDEFINED, key=Component.UNDEFINED, disabledValue=Component.UNDEFINED, direction=Component.UNDEFINED, width=Component.UNDEFINED, tooltipPosition=Component.UNDEFINED, dataValue=Component.UNDEFINED, className=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'dataValue', 'direction', 'disabledValue', 'key', 'multiple', 'multipleLabel', 'options', 'tooltipPosition', 'value', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'dataValue', 'direction', 'disabledValue', 'key', 'multiple', 'multipleLabel', 'options', 'tooltipPosition', 'value', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['options']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(LanguageSelect, self).__init__(**args)
