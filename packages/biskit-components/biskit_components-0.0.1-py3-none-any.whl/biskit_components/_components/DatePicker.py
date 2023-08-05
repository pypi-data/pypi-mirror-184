# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DatePicker(Component):
    """A DatePicker component.
Component description

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- key (string; optional)

- launchedDate (string; optional)

- name (string; default 'datepicker'):
    DatePicker World, { name }.

- type (a value equal to: 'dateRange', 'year'; default 'dateRange')

- value (dict; default {    startDate: format(endOfYesterday(), 'yyyy-MM-dd'),    endDate: format(endOfYesterday(), 'yyyy-MM-dd'),  })

    `value` is a dict with keys:

    - endDate (string; required)

    - startDate (string; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'DatePicker'
    @_explicitize_args
    def __init__(self, name=Component.UNDEFINED, type=Component.UNDEFINED, key=Component.UNDEFINED, value=Component.UNDEFINED, launchedDate=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'launchedDate', 'name', 'type', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'launchedDate', 'name', 'type', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DatePicker, self).__init__(**args)
