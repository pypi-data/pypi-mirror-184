# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class HistoryContents(Component):
    """A HistoryContents component.
Component description

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- dailyHistories (list of dicts; optional)

    `dailyHistories` is a list of dicts with keys:

    - contents (string; required)

    - date (string; optional)

    - type (a value equal to: 'update', 'marketing', 'maintenance'; required)

- key (string; optional)

- monthlyHistories (list of dicts; optional)

    `monthlyHistories` is a list of dicts with keys:

    - date (string; required)

    - histories (list of dicts; required)

        `histories` is a list of dicts with keys:

        - contents (string; required)

        - date (string; optional)

    - type (list of a value equal to: 'update', 'marketing', 'maintenance's; required)

- reports (list of dicts; optional)

    `reports` is a list of dicts with keys:

    - label (string; required)

    - link (string; required)

- title (string; optional):
    Hello World, { name }."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'HistoryContents'
    @_explicitize_args
    def __init__(self, title=Component.UNDEFINED, monthlyHistories=Component.UNDEFINED, dailyHistories=Component.UNDEFINED, reports=Component.UNDEFINED, key=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'dailyHistories', 'key', 'monthlyHistories', 'reports', 'title']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'dailyHistories', 'key', 'monthlyHistories', 'reports', 'title']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(HistoryContents, self).__init__(**args)
