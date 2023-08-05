# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Checkbox(Component):
    """A Checkbox component.
Checkbox

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional)

- dataValue (string; optional)

- description (a list of or a singular dash component, string or number; optional)

- disabled (boolean; optional)

- label (string; optional)

- value (boolean; optional)"""
    _children_props = ['description']
    _base_nodes = ['description', 'children']
    _namespace = 'biskit_components'
    _type = 'Checkbox'
    @_explicitize_args
    def __init__(self, value=Component.UNDEFINED, label=Component.UNDEFINED, disabled=Component.UNDEFINED, description=Component.UNDEFINED, dataValue=Component.UNDEFINED, className=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'dataValue', 'description', 'disabled', 'label', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'dataValue', 'description', 'disabled', 'label', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Checkbox, self).__init__(**args)
