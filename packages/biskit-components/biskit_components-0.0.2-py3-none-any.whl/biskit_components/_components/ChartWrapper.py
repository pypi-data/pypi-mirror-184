# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ChartWrapper(Component):
    """A ChartWrapper component.
Component description

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- chart (a list of or a singular dash component, string or number; optional):
    Children.

- key (string; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

- showData (boolean; optional)"""
    _children_props = ['chart']
    _base_nodes = ['chart', 'children']
    _namespace = 'biskit_components'
    _type = 'ChartWrapper'
    @_explicitize_args
    def __init__(self, chart=Component.UNDEFINED, showData=Component.UNDEFINED, key=Component.UNDEFINED, loading_state=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'chart', 'key', 'loading_state', 'showData']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'chart', 'key', 'loading_state', 'showData']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ChartWrapper, self).__init__(**args)
