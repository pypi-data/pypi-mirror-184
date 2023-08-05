# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashboardHeader(Component):
    """A DashboardHeader component.
Component description

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- breadcrumbs (list of a list of or a singular dash component, string or numbers; required):
    Children.

- buttonComponent (a list of or a singular dash component, string or number; optional)

- description (string; optional)

- key (string; optional)

- title (a list of or a singular dash component, string or number; required)"""
    _children_props = ['breadcrumbs', 'title', 'buttonComponent']
    _base_nodes = ['breadcrumbs', 'title', 'buttonComponent', 'children']
    _namespace = 'biskit_components'
    _type = 'DashboardHeader'
    @_explicitize_args
    def __init__(self, breadcrumbs=Component.REQUIRED, title=Component.REQUIRED, description=Component.UNDEFINED, buttonComponent=Component.UNDEFINED, key=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'breadcrumbs', 'buttonComponent', 'description', 'key', 'title']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'breadcrumbs', 'buttonComponent', 'description', 'key', 'title']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['breadcrumbs', 'title']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DashboardHeader, self).__init__(**args)
