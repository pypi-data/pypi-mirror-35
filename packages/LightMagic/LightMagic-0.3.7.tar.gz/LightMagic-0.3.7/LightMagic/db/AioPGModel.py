from ._Model import _Model


class AioPGModel(_Model):
    """ Базовая модель """

    async def create(self):
        """ Создает объект в БД """
        query, data = self._create()

        async with self.db.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(query, data)
                if len(self._get_primary_keys()) > 0:
                    result = await cursor.fetchone()
                    result = self._generate_dict_values(cursor, [result])[0]
                    for key in self._get_primary_keys():
                        setattr(self, key, self.get_additional_parametr(key, 'db_deserialize')(result[key]))

                self._is_created = True

    async def get_list(self, *args, **kwargs):
        """ Возвращает список записей """
        query, data = self._get_list(*args, **kwargs)
        async with self.db.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(query, data)
                return self._generate_dict_values(cursor, await cursor.fetchall())

    async def load(self, *args, **kwargs):
        """ Загружает информацию о моделе """
        query, data, fields = self._load(*args, **kwargs)

        async with self.db.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(query, data)
                result = await cursor.fetchone()
                if result is None:
                    raise LookupError

                result = self._generate_dict_values(cursor, [result])[0]

                if result is None:
                    raise LookupError('Object not found')
                else:
                    self.print_debug('-' * 10, 'Загрузка данных в модель', '-' * 10)
                    for key in fields:
                        try:
                            setattr(self, key, self.get_additional_parametr(key, 'db_deserialize')(result[key]))

                        # Игнорируем ошибку присваивания пустого поля (None)
                        except ValueError as e:
                            self.print_debug('Ошибка', e)

                    self.print_debug('-' * 10, 'Конец загрузки данных в модель', '-' * 10)

                    self._is_created = True
                    return True

    async def remove(self):
        """ Удаляем объект"""
        query, data = self._remove()
        async with self.db.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(query, data)
                self._is_created = False

    async def update(self, fields=None):
        """ Обновляем объект.
        :param fields: Список полей, которые будут обновлены. Если пустой, обновляем все поля.
        """
        query, data = self._update(fields)
        async with self.db.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(query, data)

    async def upsert(self):
        """
            Метод обновляет объект, если он существут и создает объект, если он не существуте (не были вызваны)
            методы load/create. Состояние в БД не отслеживается
        """
        if self._is_created:
            await self.update()
        else:
            await self.create()
            self._is_created = True

    def _generate_dict_values(self, cursor, values):
        names = [x.name for x in cursor.description]
        return [dict(zip(names, x)) for x in values]
