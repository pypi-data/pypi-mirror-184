# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class InfoButton(Component):
    """An InfoButton component.
Component description

Keyword arguments:

- color (string; optional)

- description (a list of or a singular dash component, string or number; required):
    InfoButton World, { name }.

- disabled (boolean; optional)

- key (string; optional)

- position (a value equal to: 'top', 'topLeft', 'topRight', 'bottom', 'bottomLeft', 'bottomRight', 'left', 'right'; optional)

- title (a list of or a singular dash component, string or number; optional)

- type (a value equal to: 'alert', 'info'; optional)"""
    _children_props = ['description', 'title']
    _base_nodes = ['description', 'title', 'children']
    _namespace = 'biskit_components'
    _type = 'InfoButton'
    @_explicitize_args
    def __init__(self, description=Component.REQUIRED, color=Component.UNDEFINED, title=Component.UNDEFINED, type=Component.UNDEFINED, key=Component.UNDEFINED, position=Component.UNDEFINED, disabled=Component.UNDEFINED, **kwargs):
        self._prop_names = ['color', 'description', 'disabled', 'key', 'position', 'title', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['color', 'description', 'disabled', 'key', 'position', 'title', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['description']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(InfoButton, self).__init__(**args)
