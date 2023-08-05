# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MonthlyHistories(Component):
    """A MonthlyHistories component.
MonthlyHistories Components

Keyword arguments:

- locale (string; required)

- monthlyHistories (list of dicts; optional):
    props.

    `monthlyHistories` is a list of dicts with keys:

    - date (string; required)

    - histories (list of dicts; required)

        `histories` is a list of dicts with keys:

        - contents (string; required)

        - date (string; optional)

    - type (list of a value equal to: 'update', 'marketing', 'maintenance's; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'MonthlyHistories'
    @_explicitize_args
    def __init__(self, monthlyHistories=Component.UNDEFINED, renderHistoryItems=Component.REQUIRED, renderHistoryTypeLabel=Component.REQUIRED, locale=Component.REQUIRED, **kwargs):
        self._prop_names = ['locale', 'monthlyHistories']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['locale', 'monthlyHistories']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['locale']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(MonthlyHistories, self).__init__(**args)
