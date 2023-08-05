# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CheckIcon(Component):
    """A CheckIcon component.
Component description

Keyword arguments:

- checked (boolean; required):
    Hello World, { name }."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'CheckIcon'
    @_explicitize_args
    def __init__(self, checked=Component.REQUIRED, **kwargs):
        self._prop_names = ['checked']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['checked']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['checked']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(CheckIcon, self).__init__(**args)
