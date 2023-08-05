# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ChartInfoContents(Component):
    """A ChartInfoContents component.
Component description

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- rows (list of dicts; optional)

    `rows` is a list of dicts with keys:

    - color (string; required)

    - diffLabel (string; optional)

    - diffRate (number; optional)

    - diffSuffix (string; optional)

    - label (string; required)

    - value (number; required)

    - valueRate (number; optional)

    - valueSuffix (string; required)

- title (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'ChartInfoContents'
    @_explicitize_args
    def __init__(self, title=Component.UNDEFINED, rows=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'rows', 'title']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'rows', 'title']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ChartInfoContents, self).__init__(**args)
