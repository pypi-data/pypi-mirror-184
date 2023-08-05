# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DailyHistories(Component):
    """A DailyHistories component.
DailyHistories Components

Keyword arguments:

- dailyHistories (list of dicts; optional):
    props.

    `dailyHistories` is a list of dicts with keys:

    - contents (string; required)

    - date (string; optional)

    - type (a value equal to: 'update', 'marketing', 'maintenance'; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'DailyHistories'
    @_explicitize_args
    def __init__(self, dailyHistories=Component.UNDEFINED, renderHistoryItems=Component.REQUIRED, renderHistoryTypeLabel=Component.REQUIRED, **kwargs):
        self._prop_names = ['dailyHistories']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['dailyHistories']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DailyHistories, self).__init__(**args)
