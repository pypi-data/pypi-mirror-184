# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mg_sql',
 'mg_sql._old.sql_raw',
 'mg_sql._old.sql_raw.async_sql',
 'mg_sql._old.sql_raw.sync_sql',
 'mg_sql._old.sql_raw.test',
 'mg_sql._old.sqllite_orm',
 'mg_sql._old.sqllite_orm.test',
 'mg_sql.sql_async']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.39,<2.0.0']

setup_kwargs = {
    'name': 'mg-sql',
    'version': '0.0.1',
    'description': 'Создание файлов конфигурация',
    'long_description': '# Подготовка\n\nДля работы с БД я создал библиотеку на основе `SqlAlchemy`.\n\nГлавно, что нужно сделать для работы с этой библиотекой, это заранее вызвать конструктор класса `SQL`, который создаст\nподключение к СУБД\n\n```python\nSQL(SqlUrlConnect.СУБД(user=\'\', password=\'\', host=\'\', name_db=\'\'))\n```\n\n- `SqlUrlConnect` - Класс с шаблонами формирования `url` для подключения к СУБД\n\n# Использование\n\n## Использование в асинхронной Функции/Методе\n\n```python\nimport asyncio\nfrom mg_sql.sql_async import SqlUrlConnect\nfrom mg_sql.sql_async.base import SQL\nfrom sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncConnection, AsyncEngine\n\n@SQL.get_session_decor\nasync def ReadDB(_session: AsyncSession):\n    res = await SQL.read_execute_raw_sql(_session, raw_sql=""" SQL ЗАПРОС = :ключ """, params={\'ключ\':Значение})\n\nasyncio.run(ReadDB())\n```\n\n- `raw_sql=\'\'` - SQL запрос\n- `params:dict[str,Any]` - Параметры в шаблонные\n\n## Создание таблиц\n\n```python\nimport asyncio\nfrom mg_sql.sql_async.base import SQL\nfrom mg_sql.sql_async.model_logic import RawSqlModel\n\nclass ИмяТаблицы(RawSqlModel):\n    """Пользователи"""\n    table_name = \'ИмяТаблицы\'\n\n    @classmethod\n    def create_table(cls) -> str:\n        return """\nCREATE TABLE ИмяТаблицы (\n id INTEGER,\n user_id INTEGER,\n);\nCREATE UNIQUE INDEX ix_users_vk_user_id ON users_vk (user_id);\n    """\n\nasyncio.run(SQL.create_models(\n    [ИмяТаблицы]\n))\n```\n\n<!-- ## Использование в FastApi\n\n```python\n@router.api_route("/Путь", methods=["POST"])\nasync def ИмяМаршрутизатора(request: Request, session: AsyncSession = Depends(SQL.get_session)):\n    res = await SQL.read_execute_raw_sql(session, raw_sql=\'\', params={})\n```\n\n- `raw_sql=\'\'` - SQL запрос\n- `params:dict[str,Any]` - Параметры в шаблонные\n -->\n',
    'author': 'Denis Kustov',
    'author_email': 'denis-kustov@rambler.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/denisxab/mg_sql.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
