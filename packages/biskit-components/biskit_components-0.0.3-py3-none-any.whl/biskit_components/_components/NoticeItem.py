# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class NoticeItem(Component):
    """A NoticeItem component.
NoticeItem

Keyword arguments:

- id (string; required)

- content (string; required)

- date (string; required)

- text (string; required)

- title (string; required)

- type (a value equal to: 'failure', 'maintenance', 'notice', 'etc'; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'NoticeItem'
    @_explicitize_args
    def __init__(self, dashboardStorageState=Component.REQUIRED, id=Component.REQUIRED, type=Component.REQUIRED, text=Component.REQUIRED, date=Component.REQUIRED, title=Component.REQUIRED, content=Component.REQUIRED, **kwargs):
        self._prop_names = ['id', 'content', 'date', 'text', 'title', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'content', 'date', 'text', 'title', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id', 'content', 'date', 'text', 'title', 'type']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(NoticeItem, self).__init__(**args)
