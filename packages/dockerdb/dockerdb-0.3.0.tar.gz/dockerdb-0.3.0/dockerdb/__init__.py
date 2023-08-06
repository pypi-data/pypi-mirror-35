import os
import time
import shutil
import tempfile
import weakref
import atexit
import functools

import docker


__version__ = '0.3.0'
start_time = int(time.time())
counter = 0
client = docker.from_env(version='auto')


def _remove_weakref(service):
    # dereferece weakref
    service = service()
    if service is not None:
        service.remove()


class Service(object):
    """Base class for docker based services"""
    timeout = 30.0
    name = 'service'

    def __init__(self, image, **kwargs):
        global counter

        self.client = client

        kwargs.setdefault('detach', True)
        name = 'tmp_{}_{}_{}'.format(start_time, self.name, counter)
        kwargs.setdefault('name', name)
        counter += 1

        kwargs.setdefault('volumes', {})
        self.share = tempfile.mkdtemp(name)
        kwargs['volumes'][self.share] = {'bind': self.share, 'mode': 'rw'}

        atexit_callback = functools.partial(_remove_weakref, weakref.ref(self))
        atexit.register(atexit_callback)
        self.container = client.containers.run(image, **kwargs)

    def inspect(self):
        """get docker inspect data for container"""
        return self.client.api.inspect_container(self.container.id)

    def ip_address(self):
        return self.inspect()['NetworkSettings']['IPAddress']

    def wait(self, timeout=None):
        if timeout is None:
            timeout = self.timeout

        start = time.time()
        while not self.check_ready() and time.time() - start < timeout:
            time.sleep(0.1)

    def remove(self):
        # this must be safe to call during interpreter shutdown
        # object might already disintegrate
        if hasattr(self, 'container'):
            try:
                self.container.remove(force=True, v=True)
            except docker.errors.NotFound:
                pass

        if os.path.exists(self.share):
            shutil.rmtree(self.share)

    def __del__(self):
        try:
            self.remove()
        except:
            # on interpreter shutdown deleting container will
            # fail as the docker client is already breaking apart.
            # the atexit callback will be called earlier, taking
            # care of this case
            pass


class HTTPServer(Service):
    protocol = 'http'
    port = '80'

    def check_ready(self):
        import requests

        ip = self.ip_address()
        url = '{}://{}:{}'.format(self.protocol, ip, self.port)

        try:
            requests.get(url)
            return True
        except requests.exceptions.ConnectionError:
            return False


class Mongo(Service):
    """Mongo in a docker container

    Starts docker on a it's default port:
    ```
    db_docker = dockerdb.Mongo('4.0.0', wait=True)
    ```

    """
    name = 'mongo'
    mongo_port = 27017

    def __init__(self, tag, wait=False, port=27017, replicaset=None, **kwargs):
        """

        * wait - if true the call blocks until MongoDB is ready to accept clients
        """
        self.port = port

        if replicaset is True:
            replicaset = 'rs0'

        self.replicaset_ready = False
        self.replicaset = replicaset

        if replicaset:
            kwargs['command'] = ['mongod', '--replSet', replicaset]

        ports = {'{}/tcp'.format(self.mongo_port): ('127.0.0.1', self.port)}
        Service.__init__(self, 'mongo:' + tag, ports=ports, **kwargs)
        if wait:
            self.wait()

    def check_ready(self):
        """Check if something responds to ``url``."""
        import pymongo.errors

        client = self.pymongo_client()
        try:
            is_master = client.admin.command('ismaster')
        except pymongo.errors.ConnectionFailure:
            return False

        if self.replicaset and not self.replicaset_ready:
            host = '{}:{}'.format(self.ip_address(), self.port)
            conf = {
                '_id': self.replicaset,
                'members': [{'_id': 0, 'host': host}]
            }
            try:
                client.admin.command('replSetInitiate', conf)
                self.replicaset_ready = True
            except pymongo.errors.OperationFailure:
                # already initlized
                self.replicaset_ready = True
            except pymongo.errors.NetworkTimeout:
                # for some reason this likes to time out
                return False

        if self.replicaset:
            return is_master.get('ismaster', False)
        return True

    def client_args(self):
        host = '{}:{}'.format(self.ip_address(), self.port)
        return {
            'host': [host],
            'socketTimeoutMS': 200,
            'connectTimeoutMS': 200
        }

    def pymongo_client(self):
        import pymongo
        return pymongo.MongoClient(**self.client_args())

    def asyncio_client(self):
        import motor.motor_asyncio
        return motor.motor_asyncio.AsyncIOMotorClient(**self.client_args())

    def factory_reset(self):
        """factory reset the database"""
        client = self.pymongo_client()
        for db in client.database_names():
            if db not in ('admin', 'config', 'local'):
                client.drop_database(db)
