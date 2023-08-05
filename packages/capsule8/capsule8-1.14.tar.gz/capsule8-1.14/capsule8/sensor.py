from itertools import islice

import asyncio
import aiogrpc

import grpc
from grpc import FutureTimeoutError
from google.protobuf.json_format import MessageToDict

import capsule8.api.v0.subscription_pb2 as sub
import capsule8.api.v0.telemetry_service_pb2 as telem
import capsule8.api.v0.telemetry_service_pb2_grpc as telem_grpc

import capsule8.exceptions as cap8e


class SensorClient(object):
    def __init__(self, sensor="unix:/var/run/capsule8/sensor.sock", certs=None):
        self.sensor = sensor
        self.certs = grpc.ssl_channel_credentials(
            open(certs).read()) if certs else None
        self.subscription = {}

    @property
    def subscription(self):
        return self._subscription

    @subscription.setter
    def subscription(self, value):
        """Convert dict to Subscription grpc message. Raise error if invalid

        Args:
            value (dict): subscription as dictionary
        """
        try:
            self._subscription = sub.Subscription(**value)
        except ValueError as e:
            raise cap8e.InvalidSubscriptionError(
                "Malformed subscription supplied: %s" % e)

    def subscribe(self, subscription):
        self.subscription = subscription

    def create_channel(self, asynchronous=False, loop=None):
        """Create async/non async grpc channel 
        Args:
            asynchronous (bool): flag to define whether to return async channel

        Returns:
            grpc.Channel: grpc channel to use with grpc stubs
        """
        if self.certs:
            if asynchronous:
                channel = aiogrpc.secure_channel(
                    self.sensor, self.certs, loop=loop)
            else:
                channel = grpc.secure_channel(
                    self.sensor, self.certs)
        else:
            if asynchronous:
                channel = aiogrpc.insecure_channel(
                    self.sensor, loop=loop)
            else:
                channel = grpc.insecure_channel(self.sensor)

        return channel

    def test_connection(self, timeout=2):
        """test connection to capsule8 sensor
        Args:
            timeout (int): amount of time to test connection before raising error
        """

        channel = self.create_channel(asynchronous=False)

        try:
            grpc.channel_ready_future(channel).result(timeout)
        except FutureTimeoutError:
            raise cap8e.SensorConnectionError(
                "Could not connect to sensor at %s. Is it running?" % self.sensor)

    def get_telemetry_service(self, channel):
        return telem_grpc.TelemetryServiceStub(channel)

    def telemetry(self, max_num_events=None, timeout=None, connection_timeout=2, asynchronous=False, loop=None, ignore_status=True):
        self.test_connection(connection_timeout)

        channel = self.create_channel(asynchronous=asynchronous, loop=loop)
        service = self.get_telemetry_service(channel)
        telemetry_stub_iterator = service.GetEvents(
            telem.GetEventsRequest(subscription=self.subscription), timeout=timeout)

        return TelemetryIterator(telemetry_stub_iterator, max_num_events, ignore_status=ignore_status, loop=loop)


class TelemetryIterator(object):

    def __init__(self, stub, max_num_events, ignore_status=True, loop=None):
        self.stub = stub
        self.max_num_events = max_num_events
        self.ignore_status = ignore_status
        self.loop = loop
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.max_num_events:
            if self.counter >= self.max_num_events:
                raise StopIteration

        try:
            self.counter += 1
            value = MessageToDict(next(self.stub))
            return value
        except grpc._channel._Rendezvous:
            raise TimeoutError("gRPC timeout exceeded")

    def __aiter__(self):
        asyncio.set_event_loop(self.loop)
        return self

    async def __anext__(self):
        if self.counter >= self.max_num_events:
            raise StopAsyncIteration

        try:
            self.counter += 1

            if self.loop:
                value = MessageToDict(await self.stub.__anext__())
            else:
                value = MessageToDict(self.stub._next())

        except StopIteration:
            raise StopAsyncIteration
        except grpc._channel._Rendezvous:
            raise TimeoutError("gRPC timeout exceeded")

        return value
