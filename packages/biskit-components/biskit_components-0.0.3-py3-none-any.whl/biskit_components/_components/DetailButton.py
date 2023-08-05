# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DetailButton(Component):
    """A DetailButton component.
Detail Button

Keyword arguments:

- dataValue (string; optional)

- href (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'DetailButton'
    @_explicitize_args
    def __init__(self, href=Component.UNDEFINED, dataValue=Component.UNDEFINED, **kwargs):
        self._prop_names = ['dataValue', 'href']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['dataValue', 'href']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DetailButton, self).__init__(**args)
