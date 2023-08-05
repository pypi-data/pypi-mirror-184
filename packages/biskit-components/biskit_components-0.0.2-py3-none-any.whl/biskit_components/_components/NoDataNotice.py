# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class NoDataNotice(Component):
    """A NoDataNotice component.
Component description

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- height (number; optional):
    Children."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'NoDataNotice'
    @_explicitize_args
    def __init__(self, height=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'height']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'height']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(NoDataNotice, self).__init__(**args)
