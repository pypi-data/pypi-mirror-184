# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TableRow(Component):
    """A TableRow component.
TableRow

Keyword arguments:

- color (string; required)

- diffLabel (string; optional)

- diffRate (number; optional)

- diffSuffix (string; optional)

- label (string; required)

- value (number; required)

- valueRate (number; optional)

- valueSuffix (string; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'TableRow'
    @_explicitize_args
    def __init__(self, color=Component.REQUIRED, label=Component.REQUIRED, value=Component.REQUIRED, valueRate=Component.UNDEFINED, valueSuffix=Component.REQUIRED, diffRate=Component.UNDEFINED, diffLabel=Component.UNDEFINED, diffSuffix=Component.UNDEFINED, **kwargs):
        self._prop_names = ['color', 'diffLabel', 'diffRate', 'diffSuffix', 'label', 'value', 'valueRate', 'valueSuffix']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['color', 'diffLabel', 'diffRate', 'diffSuffix', 'label', 'value', 'valueRate', 'valueSuffix']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['color', 'label', 'value', 'valueSuffix']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(TableRow, self).__init__(**args)
