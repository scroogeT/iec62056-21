from iec62056_21.client import Iec6205621Client
from iec62056_21 import messages

client = Iec6205621Client.with_serial_transport(port='/dev/ttyUSB0')


# Standard Readout
client.connect()
print(client.standard_readout())


# Open/Close Latch
client.connect()
client.access_programming_mode()
client.send_password('30003000')
""" Relay States
    0 = switch relay status OFF
    1 = switch relay status ARMED
    2 = switch relay status ON
"""
client.write_single_value(address='S0I', data=2)
client.send_break()
client.disconnect()


# Read Load Profile
client.connect()
client.access_programming_mode()
client.send_password('30003000')
request = messages.CommandMessage.for_single_read('P.01', '02012010000;02012020000')
client.transport.send(request.to_bytes())
response = client.read_response()
client.send_break()
client.disconnect()



