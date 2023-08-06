import datetime

from ._Base import _Base


class TimeDelta(_Base):
    """
        Работает с интервалом времени
    """

    def _validate(self, obj, value):
        """
            Проверяем корректность входных данных
        """
        if isinstance(value, datetime.timedelta):
            return value

        else:
            raise ValueError('Unknown format: type: %s  | value: %s' % (type(value), str(value)))

    def get_db_type(self):
        if self.db_type:
            return self.db_type
        return 'interval'
