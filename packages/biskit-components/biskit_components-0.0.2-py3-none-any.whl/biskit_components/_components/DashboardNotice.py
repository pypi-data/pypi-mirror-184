# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashboardNotice(Component):
    """A DashboardNotice component.
DashboardNotice

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- dashboardKey (string; required):
    Dashboard ID."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'DashboardNotice'
    @_explicitize_args
    def __init__(self, dashboardKey=Component.REQUIRED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'dashboardKey']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'dashboardKey']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['dashboardKey']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DashboardNotice, self).__init__(**args)
