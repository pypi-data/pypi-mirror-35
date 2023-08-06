""" File with a useful service tools """


def get_additional_parametr(obj, key, parament):
    """ Returns additional parameter value """

    def _dig_class(key, oclass):
        if key in oclass.__dict__:
            return oclass.__dict__[key]
        else:
            for p_class in oclass.__bases__:
                if p_class == object:
                    continue
                elif key in p_class.__dict__:
                    return p_class.__dict__[key]
                else:
                    return _dig_class(key, p_class)
            raise AttributeError('Key %s not found' % key)

    return getattr(_dig_class(key, obj.__class__), parament)
