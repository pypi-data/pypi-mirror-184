# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class InfoIcon(Component):
    """An InfoIcon component.
Component description

Keyword arguments:

- color (string; optional)

- height (number; optional)

- width (number; optional):
    Hello World, { name }."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'InfoIcon'
    @_explicitize_args
    def __init__(self, width=Component.UNDEFINED, height=Component.UNDEFINED, color=Component.UNDEFINED, **kwargs):
        self._prop_names = ['color', 'height', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['color', 'height', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(InfoIcon, self).__init__(**args)
