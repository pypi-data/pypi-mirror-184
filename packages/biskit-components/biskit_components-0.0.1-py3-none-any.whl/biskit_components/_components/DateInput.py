# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DateInput(Component):
    """A DateInput component.
Component description

Keyword arguments:

- dateRange (list of boolean | number | string | dict | lists; required)

- disabled (boolean; optional)

- selected (boolean; required)

- setValue (dict; required)

    `setValue` is a dict with keys:


- type (a value equal to: 'startDate', 'endDate'; required)

- value (list of strings; required):
    DateInput."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'DateInput'
    @_explicitize_args
    def __init__(self, value=Component.REQUIRED, setValue=Component.REQUIRED, selected=Component.REQUIRED, type=Component.REQUIRED, dateRange=Component.REQUIRED, changeDateFunction=Component.REQUIRED, disabled=Component.UNDEFINED, **kwargs):
        self._prop_names = ['dateRange', 'disabled', 'selected', 'setValue', 'type', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['dateRange', 'disabled', 'selected', 'setValue', 'type', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['dateRange', 'selected', 'setValue', 'type', 'value']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DateInput, self).__init__(**args)
