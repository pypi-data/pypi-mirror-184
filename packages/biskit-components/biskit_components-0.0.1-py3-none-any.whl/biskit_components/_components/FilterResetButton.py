# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FilterResetButton(Component):
    """A FilterResetButton component.
FilterResetButton

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional)

- n_clicks (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'FilterResetButton'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, n_clicks=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'n_clicks']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'n_clicks']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FilterResetButton, self).__init__(**args)
