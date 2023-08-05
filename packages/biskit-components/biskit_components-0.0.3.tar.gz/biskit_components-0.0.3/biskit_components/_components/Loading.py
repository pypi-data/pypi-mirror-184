# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Loading(Component):
    """A Loading component.
Layout Component

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- key (string; optional)

- loading (boolean; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

- size (a value equal to: 'medium', 'small'; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'Loading'
    @_explicitize_args
    def __init__(self, children=None, loading=Component.UNDEFINED, loading_state=Component.UNDEFINED, size=Component.UNDEFINED, key=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'key', 'loading', 'loading_state', 'size']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'key', 'loading', 'loading_state', 'size']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Loading, self).__init__(children=children, **args)
