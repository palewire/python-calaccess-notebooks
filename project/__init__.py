import agate
from django.db import connection

def sql_to_agate(sql):
    """
    Execute a raw sql string and return results as an agate table.
    """
    with connection.cursor() as c:
        c.execute(sql)
        columns = [col.name for col in c.description]

        return agate.Table.from_object(
            [dict(zip(columns, row)) for row in c.fetchall()]
        ).select(columns)
