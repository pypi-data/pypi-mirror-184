"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
from .... import common
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class StatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___StatusRequest = StatusRequest

@typing_extensions.final
class StatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STATUS_FIELD_NUMBER: builtins.int

    @property
    def status(self) -> common.v1.common_pb2.BoardStatus:
        ...

    def __init__(self, *, status: common.v1.common_pb2.BoardStatus | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['status', b'status']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['status', b'status']) -> None:
        ...
global___StatusResponse = StatusResponse

@typing_extensions.final
class SetGPIORequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    PIN_FIELD_NUMBER: builtins.int
    HIGH_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    pin: builtins.str
    high: builtins.bool

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., pin: builtins.str=..., high: builtins.bool=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'high', b'high', 'name', b'name', 'pin', b'pin']) -> None:
        ...
global___SetGPIORequest = SetGPIORequest

@typing_extensions.final
class SetGPIOResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___SetGPIOResponse = SetGPIOResponse

@typing_extensions.final
class GetGPIORequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    PIN_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    pin: builtins.str

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., pin: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name', 'pin', b'pin']) -> None:
        ...
global___GetGPIORequest = GetGPIORequest

@typing_extensions.final
class GetGPIOResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HIGH_FIELD_NUMBER: builtins.int
    high: builtins.bool

    def __init__(self, *, high: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['high', b'high']) -> None:
        ...
global___GetGPIOResponse = GetGPIOResponse

@typing_extensions.final
class PWMRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    PIN_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    pin: builtins.str

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., pin: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name', 'pin', b'pin']) -> None:
        ...
global___PWMRequest = PWMRequest

@typing_extensions.final
class PWMResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DUTY_CYCLE_PCT_FIELD_NUMBER: builtins.int
    duty_cycle_pct: builtins.float
    '0-1'

    def __init__(self, *, duty_cycle_pct: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['duty_cycle_pct', b'duty_cycle_pct']) -> None:
        ...
global___PWMResponse = PWMResponse

@typing_extensions.final
class SetPWMRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    PIN_FIELD_NUMBER: builtins.int
    DUTY_CYCLE_PCT_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    pin: builtins.str
    duty_cycle_pct: builtins.float
    '0-1'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., pin: builtins.str=..., duty_cycle_pct: builtins.float=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['duty_cycle_pct', b'duty_cycle_pct', 'extra', b'extra', 'name', b'name', 'pin', b'pin']) -> None:
        ...
global___SetPWMRequest = SetPWMRequest

@typing_extensions.final
class SetPWMResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___SetPWMResponse = SetPWMResponse

@typing_extensions.final
class PWMFrequencyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    PIN_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    pin: builtins.str

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., pin: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name', 'pin', b'pin']) -> None:
        ...
global___PWMFrequencyRequest = PWMFrequencyRequest

@typing_extensions.final
class PWMFrequencyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FREQUENCY_HZ_FIELD_NUMBER: builtins.int
    frequency_hz: builtins.int

    def __init__(self, *, frequency_hz: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['frequency_hz', b'frequency_hz']) -> None:
        ...
global___PWMFrequencyResponse = PWMFrequencyResponse

@typing_extensions.final
class SetPWMFrequencyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    PIN_FIELD_NUMBER: builtins.int
    FREQUENCY_HZ_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    pin: builtins.str
    frequency_hz: builtins.int

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., pin: builtins.str=..., frequency_hz: builtins.int=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'frequency_hz', b'frequency_hz', 'name', b'name', 'pin', b'pin']) -> None:
        ...
global___SetPWMFrequencyRequest = SetPWMFrequencyRequest

@typing_extensions.final
class SetPWMFrequencyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___SetPWMFrequencyResponse = SetPWMFrequencyResponse

@typing_extensions.final
class ReadAnalogReaderRequest(google.protobuf.message.Message):
    """Analog Reader"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BOARD_NAME_FIELD_NUMBER: builtins.int
    ANALOG_READER_NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    board_name: builtins.str
    analog_reader_name: builtins.str

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, board_name: builtins.str=..., analog_reader_name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['analog_reader_name', b'analog_reader_name', 'board_name', b'board_name', 'extra', b'extra']) -> None:
        ...
global___ReadAnalogReaderRequest = ReadAnalogReaderRequest

@typing_extensions.final
class ReadAnalogReaderResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.int

    def __init__(self, *, value: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['value', b'value']) -> None:
        ...
global___ReadAnalogReaderResponse = ReadAnalogReaderResponse

@typing_extensions.final
class GetDigitalInterruptValueRequest(google.protobuf.message.Message):
    """Digital Interrupt"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BOARD_NAME_FIELD_NUMBER: builtins.int
    DIGITAL_INTERRUPT_NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    board_name: builtins.str
    digital_interrupt_name: builtins.str

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, board_name: builtins.str=..., digital_interrupt_name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['board_name', b'board_name', 'digital_interrupt_name', b'digital_interrupt_name', 'extra', b'extra']) -> None:
        ...
global___GetDigitalInterruptValueRequest = GetDigitalInterruptValueRequest

@typing_extensions.final
class GetDigitalInterruptValueResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.int

    def __init__(self, *, value: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['value', b'value']) -> None:
        ...
global___GetDigitalInterruptValueResponse = GetDigitalInterruptValueResponse