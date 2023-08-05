import logging

import redis

from fastiot.core.serialization import serialize_to_bin, serialize_from_bin
from fastiot.env.env import env_redis
from fastiot.msg import RedisMsg


class RedisClient:
    client = None

async def connectRedis():
    client = redis.Redis(
        host=env_redis.host,
        port=env_redis.port)
    return client

async def getRedisClient():
    if RedisClient.client is None:
        RedisClient.client = await connectRedis()
    return RedisClient.client


class RedisHelper:
    """
    Saves files in the redis Database and sends the ID of the files  as  :class:`fastiot.msg.redis.RedisMsg`.

    You can send files by using :meth:`send_data` you must specify the data to send and the subject under which the data
    should be published. The max number of Datasets you can store at once is specified by :var: `maxDataSets` .
    If you add a Dataset above the given limit the first Dataset stored is deleted. When you have problems that an ID
    is overwritten before you accessed the data you can change the :var:`idBuffer` to have more Ids before an ID is
    reused.

    You can access the stored data with :meth:`get_data`. The Id of the Data has to be provided. and the returned data
    will be deserialized with :meth:`fastiot.core.serialization.serialize_from_bin`.
    """

    def __init__(self, broker_connection):
        self.broker_connection = broker_connection
        self.usedIds = []
        self.maxDataSets = 100
        """The max number of Datasets you can store at once"""
        self.idCounter = 0
        self.idBuffer = 2
        """:var:`maxDataSets` * :var:`idBuffer` is the total number of Ids, that are used before an Id is overwritten """

    async def _create_id(self) -> int:
        if self.idCounter >= (self.maxDataSets * self.idBuffer):
            self.idCounter = 0
        while self.idCounter in self.usedIds:
            self.idCounter = self.idCounter + 1
        self.usedIds.append(self.idCounter)
        return self.idCounter

    async def send_data(self, data, subject):
        id = await self._create_id()
        client = await getRedisClient()
        data = serialize_to_bin(data.__class__, data)
        await self.delete()
        client.set(name=id, value=data)
        await self.broker_connection.publish(
            subject=subject,
            msg=RedisMsg(id=id))
        logging.info("Saved data at %d from  %s", id, subject.name)

    async def get_data(self, address: str):
        client = await getRedisClient()
        return serialize_from_bin("".__class__, client.get(address))

    async def delete(self):
        client = await getRedisClient()
        while len(self.usedIds) > self.maxDataSets:
            delete = self.usedIds[0]
            client.delete(delete)
            self.usedIds.remove(delete)
            logging.debug("Removed Data with Id %d", delete)

    async def deleteall(self):
        client = await getRedisClient()
        while len(self.usedIds) > 0:
            delete = self.usedIds[0]
            client.delete(delete)
            self.usedIds.remove(delete)
            logging.debug("Removed Data with Id %d", delete)
