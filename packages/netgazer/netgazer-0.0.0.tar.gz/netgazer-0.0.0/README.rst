========
netgazer
========


Netgazer automates the process getting data from network devices


Description
===========

Python Network Automation tool build using NAPALM and CLICK for getting data from network environment.




Note
====

This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.


Sample Device Inventory format:  

[
  {
  "device_type": "ios",
  "device_name": "VAEITSW001a",
  "useRadius": "True",
  "hostname": "192.168.2.1",
  "username": "",
  "password": "",
  "optional_args": {"dest_file_system": "flash:"}
  },
  {
  "device_type": "ios",
  "device_name": "VAEITSW002a",
  "useRadius": "True",
  "hostname": "192.168.2.2",
  "username": "",
  "password": "",
  "optional_args": {"dest_file_system": "flash:"}
  },
  {
  "device_type": "ios",
  "device_name": "VAEITSW003",
  "useRadius": "True",
  "hostname": "192.168.2.3",
  "username": "",
  "password": "",
  "optional_args": {"dest_file_system": "flash:"}
  }
]

get_interfaces_counters - RETURN FORMAT
 {
 'GigabitEthernet2/0/9': {'rx_broadcast_packets': 3605499,
                          'rx_discards': 0,
                          'rx_errors': 0,
                          'rx_multicast_packets': 8,
                          'rx_octets': 39164458043,
                          'rx_unicast_packets': 58218011,
                          'tx_broadcast_packets': -1,
                          'tx_discards': 0,
                          'tx_errors': 0,
                          'tx_multicast_packets': -1,
                          'tx_octets': 111566264942,
                          'tx_unicast_packets': 1208750925},
 'Port-channel1': {'rx_broadcast_packets': 112579624,
                   'rx_discards': 0,
                   'rx_errors': 0,
                   'rx_multicast_packets': 1,
                   'rx_octets': 240968975035,
                   'rx_unicast_packets': 719108482,
                   'tx_broadcast_packets': -1,
                   'tx_discards': 0,
                   'tx_errors': 0,
                   'tx_multicast_packets': -1,
                   'tx_octets': 422137955389,
                   'tx_unicast_packets': 3091858173}
}




get_interfaces_counters - RETURN FORMAT

                       'rx_broadcast_packets': 112579624,
                       'rx_discards': 0,
                       'rx_errors': 0,
                       'rx_multicast_packets': 1,
                       'rx_octets': 240968975035,
                       'rx_unicast_packets': 719108482,
                       'tx_broadcast_packets': -1,
                       'tx_discards': 0,
                       'tx_errors': 0,
                       'tx_multicast_packets': -1,
                       'tx_octets': 422137955389,
                       'tx_unicast_packets': 3091858173}



