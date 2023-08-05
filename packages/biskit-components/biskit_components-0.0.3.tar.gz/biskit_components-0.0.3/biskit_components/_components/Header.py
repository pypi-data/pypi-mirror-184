# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Header(Component):
    """A Header component.
Component description

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- selectComponents (a list of or a singular dash component, string or number; required):
    Hello World, { name }."""
    _children_props = ['selectComponents']
    _base_nodes = ['selectComponents', 'children']
    _namespace = 'biskit_components'
    _type = 'Header'
    @_explicitize_args
    def __init__(self, selectComponents=Component.REQUIRED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'selectComponents']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'selectComponents']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['selectComponents']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Header, self).__init__(**args)
