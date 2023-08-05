# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class BoardItem(Component):
    """A BoardItem component.
BoardItem Components

Keyword arguments:

- id (string; optional):
    props.

- content (string; optional)

- date (string; optional)

- isPinned (boolean; optional)

- link (string; optional)

- onClick (dict; optional)

    `onClick` is a dict with keys:


- title (string; optional)

- type (a value equal to: 'failure', 'maintenance', 'notice', 'etc'; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'BoardItem'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, title=Component.UNDEFINED, content=Component.UNDEFINED, isPinned=Component.UNDEFINED, onClick=Component.UNDEFINED, type=Component.UNDEFINED, date=Component.UNDEFINED, link=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'content', 'date', 'isPinned', 'link', 'onClick', 'title', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'content', 'date', 'isPinned', 'link', 'onClick', 'title', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(BoardItem, self).__init__(**args)
