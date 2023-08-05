# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Breadcrumbs(Component):
    """A Breadcrumbs component.
Component description

Keyword arguments:

- breadcrumbs (list of a list of or a singular dash component, string or numbers; required):
    Children."""
    _children_props = ['breadcrumbs']
    _base_nodes = ['breadcrumbs', 'children']
    _namespace = 'biskit_components'
    _type = 'Breadcrumbs'
    @_explicitize_args
    def __init__(self, breadcrumbs=Component.REQUIRED, **kwargs):
        self._prop_names = ['breadcrumbs']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['breadcrumbs']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['breadcrumbs']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Breadcrumbs, self).__init__(**args)
