# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Board(Component):
    """A Board component.
Board Components

Keyword arguments:

- id (string; optional):
    props.

- items (list of dicts; required)

    `items` is a list of dicts with keys:

    - content (string; optional)

    - date (string; optional)

    - id (string; optional):
        props.

    - isPinned (boolean; optional)

    - link (string; optional)

    - onClick (dict; optional)

        `onClick` is a dict with keys:


    - title (string; optional)

    - type (a value equal to: 'failure', 'maintenance', 'notice', 'etc'; optional)

- title (string; required)

- titleLink (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'Board'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, title=Component.REQUIRED, titleLink=Component.UNDEFINED, items=Component.REQUIRED, **kwargs):
        self._prop_names = ['id', 'items', 'title', 'titleLink']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'items', 'title', 'titleLink']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['items', 'title']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Board, self).__init__(**args)
