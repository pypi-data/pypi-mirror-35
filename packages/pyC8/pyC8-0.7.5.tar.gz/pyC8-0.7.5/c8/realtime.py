from __future__ import absolute_import, unicode_literals

__all__ = ['Realtime']

from c8.api import APIWrapper
from c8.connection import RealtimeConnection
import c8.constants as constants
import pulsar
import random
import json

from c8.exceptions import (
    StreamConnectionError,
    StreamEventError
)
from c8.executor import DefaultExecutor
from c8.request import Request


class Realtime(APIWrapper):
    """Realtime (C8 Realtime) API wrapper.

    :param tenant_name: HTTP connection.
    :type tenant_name: string
    :param db_name: string
    :type db_name: string
    """

    def __init__(self, stream_host, 
            stream_port=constants.STREAM_PORT, 
            tenant=constants.TENANT_DEFAULT, 
            db=constants.DB_DEFAULT, 
            username=constants.USER_DEFAULT, 
            password='', 
            globalns = False):
        if not stream_host:
            raise ValueError("Realtime: Stream host URL (C8 URL) is null or empty!")

        self.stream_port = stream_port
        self.stream_host = stream_host
        self.tenant = tenant
        self.db = db
        self.user = username
        self.passwd = password
        self.client = pulsar.Client('pulsar://' + self.stream_host + ":" + self.stream_port)
        self.consumer = None
        self.topic = ''

        # We really only do the following bits to keep things consistent with the rest of the code.
        # It's really unnecessary for this, at least right now (26-Jul-2018) while we don't have streams integration.
        connection = RealtimeConnection(
                url=self.client,
                tenant=self.tenant,
                db = self.db,
                username = self.user,
                password = self.passwd,
                http_client = None,
                topic = self.topic
                )
        super(Realtime, self).__init__(connection=connection, executor=DefaultExecutor(connection))
        if self.client:
            print("pyC8 Realtime: Initialized C8Streams connection to "+ self.stream_host + ":" + self.stream_port)


    def printdata(event):
        """Prints the event.

        :param event: real-time update.
        :type event: str | unicode
        """
        print(event)

    def on_change(self, collection, callback=printdata):
        """Execute given input function on receiving a change.

        :param callback: Function to execute on a change
        :type callback: function
        :param collections: Collection name or Collection names regex to listen for
        :type collections: str
        """
        if not collection: 
            raise ValueError('You must specify a collection on which to watch for realtime data!')

        topic = "non-persistent://" + self.tenant + "/" + constants.STREAM_LOCAL_NS_PREFIX + self.db + "/" + collection
        subscription_name = self.tenant + "." + self.db + ".subscription." + str(random.randint(1,1000))
        print("pyC8 Realtime: Subscribing to topic: "+topic)
        print("pyC8 Realtime: Subscription name: "+subscription_name)
        self.topic = topic

        if self.consumer is None:
            self.consumer = self.client.subscribe(topic, subscription_name)

        try:
            print("pyC8 Realtime: Begin monitoring realtime updates for "+topic)
            while True:
                msg = self.consumer.receive()
                data = msg.data().decode('utf-8')
                jdata = json.loads(data)
                #self.consumer.acknowledge(msg)
                callback(jdata)
        finally:
            self.client.close()


