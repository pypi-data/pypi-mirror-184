# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class SubBanner(Component):
    """A SubBanner component.
nt-disable-next-line @typescript-eslint/no-unused-v

Keyword arguments:

- id (string; optional):
    Hello World.

- iconType (a value equal to: 'biskit', 'help', 'slack'; required)

- label (string; required)

- link (string; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'SubBanner'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, iconType=Component.REQUIRED, label=Component.REQUIRED, link=Component.REQUIRED, **kwargs):
        self._prop_names = ['id', 'iconType', 'label', 'link']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'iconType', 'label', 'link']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['iconType', 'label', 'link']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(SubBanner, self).__init__(**args)
