# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Reports(Component):
    """A Reports component.
Reports Components

Keyword arguments:

- hasHistories (boolean; optional)

- reports (list of dicts; required):
    props.

    `reports` is a list of dicts with keys:

    - label (string; required)

    - link (string; required)

- type (a value equal to: 'monthly', 'daily'; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'Reports'
    @_explicitize_args
    def __init__(self, reports=Component.REQUIRED, type=Component.UNDEFINED, hasHistories=Component.UNDEFINED, **kwargs):
        self._prop_names = ['hasHistories', 'reports', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['hasHistories', 'reports', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['reports']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Reports, self).__init__(**args)
