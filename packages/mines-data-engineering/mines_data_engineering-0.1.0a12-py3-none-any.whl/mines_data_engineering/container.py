import os
import logging
import threading
import tempfile
from typing import Tuple
try:
    from spython.main import get_client
    from spython.utils import check_install
    USE_DOCKER = False
    client = get_client()
    if not check_install():
        raise ImportError("Singularity not available")
except ImportError:
    from docker import from_env
    USE_DOCKER = True
    client = from_env()

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

# where everything lives
tmpdir = tempfile.TemporaryDirectory(prefix=os.getcwd() + "/tmp")

class Service:
    singularity_container: str
    docker_container: Tuple[str, str]

    @classmethod
    def pull(cls):
        if USE_DOCKER:
            logging.info(f"Pulling contaner: {cls.docker_container}")
            client.images.pull(cls.docker_container[0], tag=cls.docker_container[1])
        else:
            logging.info(f"Pulling contaner: {cls.singularity_container}")
            client.pull(image=cls.singularity_container)

    @classmethod
    def run(cls):
        raise NotImplementedError


class MongoDB(Service):
    singularity_container = "docker://mongo:latest"
    docker_container = ("mongo", "latest")

    @classmethod
    def run(cls):
        cls.pull()
        if USE_DOCKER:
            return client.containers.run(cls.docker_container[0], detach=True, auto_remove=False, name="data-engineering-mongodb")
        else:
            inst = client.instance.instance(image=self.singularity_container, options=[f"-B {tmpdir.name}:/data/db", f"-B {tmpdir.name}:/tmp"])
            def _run_mongo():
                client.execute(image=f"instance://{inst.name}", command=["mongod"])
            t = threading.Thread(target=_run_mongo)
            t.start()
            return inst


class TimescaleDB(Service):
    singularity_container = "docker://timescale/timescaledb:latest-pg14"
    docker_container = ("timescale/timescaledb", "latest-pg14")

    @classmethod
    def run(cls):
        cls.pull()
        if USE_DOCKER:
            return client.containers.run(cls.docker_container[0], detach=True, auto_remove=False, name="data-engineering-timescaledb")
        else:
            os.environ["POSTGRES_PASSWORD"] = "password"
            inst = client.instance.instance(image=cls.singularity_container, options=[f"-B {tmpdir.name}:/var/lib/postgresql/data", f"-B {tmpdir.name}:/var/run/postgresql", f"--env=POSTGRES_PASSWORD"])
            def _run_timescale():
                client.execute(image=f"instance://{inst.name}", command=["/usr/local/bin/docker-entrypoint.sh", "postgres"])
            t = threading.Thread(target=_run_timescale)
            t.start()
            return inst
