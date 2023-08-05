# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Label(Component):
    """A Label component.
Label component

Keyword arguments:

- type (a value equal to: 'maintenance', 'failure', 'notice', 'etc'; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'Label'
    @_explicitize_args
    def __init__(self, type=Component.REQUIRED, **kwargs):
        self._prop_names = ['type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['type']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Label, self).__init__(**args)
