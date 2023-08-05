# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Fragment(Component):
    """A Fragment component.
Component description

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'Fragment'
    @_explicitize_args
    def __init__(self, children=None, **kwargs):
        self._prop_names = ['children']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Fragment, self).__init__(children=children, **args)
