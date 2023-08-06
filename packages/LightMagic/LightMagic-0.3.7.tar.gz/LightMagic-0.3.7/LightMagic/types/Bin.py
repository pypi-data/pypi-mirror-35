from ._Base import _Base


class Bin(_Base):
    """ Advanced card data type for BIN (Bank Identification Number) """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate(self, obj, value):
        """
            The length of the BIN may be 1 to 10 characters (subranges for different products)
            to start on any number, including 0.
        """
        try:
            if -1 < int(value) < 10 ** 10:
                return int(value)
        except Exception:
            raise ValueError('Value isn\'t BIN')
