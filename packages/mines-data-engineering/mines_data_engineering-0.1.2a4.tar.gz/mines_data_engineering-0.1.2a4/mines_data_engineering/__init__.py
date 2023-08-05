import logging
import time
from mines_data_engineering.container import MongoDB, TimescaleDB, dbdir

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

_mongo_instance = None
_pg_instance = None

def start_mongo():
    """
    Starts MongoDB and returns the connection string
    """
    logging.info("Starting MongoDB")
    global _mongo_instance
    _mongo_instance = MongoDB.run()
    logging.info("Sleeping for 2 seconds to let MongoDB start")
    time.sleep(2)
    return "mongodb://" + f"{dbdir.name}/mongodb-27017.sock".replace('/', '%2F')


def start_postgres():
    """
    Starts Postgres w/ TimescaleDB extension and returns the connection string
    """
    logging.info("Starting Postgres")
    global _pg_instance
    _pg_instance = TimescaleDB.run()
    logging.info("Sleeping for 20 seconds to let Postgres start")
    time.sleep(20)
    return f"user=postgres password=password host={dbdir.name}"
