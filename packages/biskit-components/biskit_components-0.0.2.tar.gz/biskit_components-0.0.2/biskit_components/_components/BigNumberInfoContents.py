# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class BigNumberInfoContents(Component):
    """A BigNumberInfoContents component.
Component description

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- diffLabel (string; optional)

- diffRate (number; optional)

- diffSuffix (string; optional)

- title (string; optional)

- value (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'BigNumberInfoContents'
    @_explicitize_args
    def __init__(self, title=Component.UNDEFINED, value=Component.UNDEFINED, diffLabel=Component.UNDEFINED, diffRate=Component.UNDEFINED, diffSuffix=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'diffLabel', 'diffRate', 'diffSuffix', 'title', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'diffLabel', 'diffRate', 'diffSuffix', 'title', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(BigNumberInfoContents, self).__init__(**args)
