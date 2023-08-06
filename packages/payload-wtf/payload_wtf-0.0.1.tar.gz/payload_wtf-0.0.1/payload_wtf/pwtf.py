import json


class PayloadBase(object):
    def __init__(self):
        self._data_payload = {}

    def set_state(self, *args, **kwargs):
        pass


class Links:
    KEY_LINKS = 'links'
    KEY_PREV = 'prev'
    KEY_NEXT = 'next'
    SET_LINKS = '_set_links'

    def _build_links(self):
        return {
            Links.KEY_LINKS: {
                Links.KEY_NEXT: '',
                Links.KEY_PREV: ''
            }
        }


class Metas:
    KEY_META = 'meta'
    SET_META = '__set_meta'

    def _build_meta(self):
        return {Metas.KEY_META: {}}


class Resultset:
    SET_RESULT = 'set_result'
    KEY_RESULT = 'results'

    def _build_result(self):
        return {Resultset.KEY_RESULT: {}}


class PayloadWTF(PayloadBase, Links, Metas, Resultset):

    def __init__(self):
        super(PayloadWTF, self).__init__()
        self._build()

    def _build(self):
        self._data_payload.update(self._build_result())
        self._data_payload.update(self._build_meta())
        self._data_payload.update(self._build_links())

    def set_state(self, *args, **kwargs):
        if kwargs.get('setter') == self.SET_RESULT:
            self._set_result(*args, **kwargs)
        if kwargs.get('setter') == self.SET_LINKS:
            self._set_links(*args, **kwargs)
        if kwargs.get('setter') == self.SET_META:
            self._set_meta(*args, **kwargs)

    def _set_result(self, *args, **kwargs):
        self._data_payload[self.KEY_RESULT] = kwargs.get('data')

    def _set_links(self, *args, **kwargs):
        self._data_payload[self.KEY_LINKS] = {
            self.KEY_NEXT: kwargs.get('next', ''),
            self.KEY_PREV: kwargs.get('prev', '')
        }

    def _set_meta(self, *args, **kwargs):
        self._data_payload[self.KEY_META] = kwargs.get('data')

    def todata(self):
        return self._data_payload

    def tojson(self):
        return json.dumps(self._data_payload)

    def reset(self):
        self._build()

