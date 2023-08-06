from ._Base import _Base


class Bool(_Base):
    """ Boolean data type """

    def _validate(self, obj, value):
        """
            Проверяем корректность входных данных
        """
        return bool(value)

    def get_db_type(self):
        return 'bool'
