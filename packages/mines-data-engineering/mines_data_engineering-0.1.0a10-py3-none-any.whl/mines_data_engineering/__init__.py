import time
from mines_data_engineering.container import MongoDB, TimescaleDB, tmpdir

_mongo_instance = None
_pg_instance = None

def start_mongo():
    """
    Starts MongoDB and returns the connection string
    """
    global _mongo_instance
    _mongo_instance = MongoDB.run()
    time.sleep(2)
    return "mongodb://" + f"{tmpdir.name}/mongodb-27017.sock".replace('/', '%2F')


def start_postgres():
    """
    Starts MongoDB and returns the connection string
    """
    global _pg_instance
    _pg_instance = TimescaleDB.run()
    time.sleep(2)
    return f"user=postgres password=password host={tmpdir.name}/.s.PGSQL.5432"
