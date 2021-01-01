from google.cloud.datastore.entity import Entity as Entity
from google.cloud.datastore.key import Key as Key
from google.cloud.datastore_v1.proto import datastore_pb2 as datastore_pb2, entity_pb2 as entity_pb2
from google.protobuf import struct_pb2 as struct_pb2
from google.type import latlng_pb2 as latlng_pb2
from typing import Any

def entity_from_protobuf(pb: Any): ...
def entity_to_protobuf(entity: Any): ...
def get_read_options(eventual: Any, transaction_id: Any): ...
def key_from_protobuf(pb: Any): ...

class GeoPoint:
    latitude: Any = ...
    longitude: Any = ...
    def __init__(self, latitude: Any, longitude: Any) -> None: ...
    def to_protobuf(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...