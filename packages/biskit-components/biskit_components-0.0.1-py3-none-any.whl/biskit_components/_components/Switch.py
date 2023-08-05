# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Switch(Component):
    """A Switch component.
Component description

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional)

- dataValue (string; optional)

- value (boolean; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'Switch'
    @_explicitize_args
    def __init__(self, children=None, value=Component.UNDEFINED, className=Component.UNDEFINED, dataValue=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'dataValue', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'dataValue', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Switch, self).__init__(children=children, **args)
