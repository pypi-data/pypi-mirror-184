# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Link(Component):
    """A Link component.
Link description

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional)

- href (string; required):
    Link.

- key (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'Link'
    @_explicitize_args
    def __init__(self, children=None, href=Component.REQUIRED, className=Component.UNDEFINED, key=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'href', 'key']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'href', 'key']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['href']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Link, self).__init__(children=children, **args)
