# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashboardInformation(Component):
    """A DashboardInformation component.
Component description

Keyword arguments:

- buttonComponent (a list of or a singular dash component, string or number; required)

- description (string; required):
    Children.

- key (string; optional)"""
    _children_props = ['buttonComponent']
    _base_nodes = ['buttonComponent', 'children']
    _namespace = 'biskit_components'
    _type = 'DashboardInformation'
    @_explicitize_args
    def __init__(self, description=Component.REQUIRED, buttonComponent=Component.REQUIRED, key=Component.UNDEFINED, **kwargs):
        self._prop_names = ['buttonComponent', 'description', 'key']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['buttonComponent', 'description', 'key']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['buttonComponent', 'description']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DashboardInformation, self).__init__(**args)
