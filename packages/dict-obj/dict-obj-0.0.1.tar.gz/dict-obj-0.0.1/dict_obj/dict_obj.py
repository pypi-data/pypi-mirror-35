def _ret(element):
    if isinstance(element, dict):
        return obj(element)
    if isinstance(element, list):
        return list(map(_ret, element))
    return element


class obj(object):
    def __init__(self, dictionary):
        self._dict = dictionary

    def __getattr__(self, name):
        if not name in self._dict:
            return getattr(self._dict, name)
        return _ret(self._dict[name])

    def __setattr__(self, name, value):
        if name == '_dict':
            super().__setattr__(name, value)
        else:
            self._dict[name] = value

    def __getitem__(self, name):
        return self.__getattr__(name)

    def __setitem__(self, name, value):
        self._dict[name] = value
