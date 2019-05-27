## Some stuff about WiFi networks

### Important definitions

__IEEE 802.11:__ A set of LAN protocols. Specifies the set of media access control(MAC) and physical layer (PHY) protocols for implementing wireless local area network (WLAN) WiFi computer communication in various frequencies, including but not limited to 2.4, 5, and 60 GHz frequency bands.

__Network interface controller(NIC):__ A computer hardware component that connects a computer to a computer network.

__Media Access Control(MAC) Address:__ A unique identifier assigned to a network interface controller(NIC). It is used as a network address for most IEEE 802 network technologies, including Ethernet, WiFi and Bluetooth. 

__Data Packet:__ A unit of data made into a single package that travels along a given network path. Data packets are used in Internet Protocol (IP) transmissions for data that navigates the Web, and in other kinds of networks.

__Is a device’s MAC address unique?__
Yes. Vendors are given a range of MAC Addresses that can be assigned to their products by the IEEE (Institute of Electrical and Electronics Engineers). Basically, a device can be uniquely identified by its MAC address.

__How would you detect a device whose WiFi is on but is not connected to your network?__

* Whenever a phone’s WiFi is turned on, but not connected to a network, it openly broadcasts the SSIDs (network names) of all previously-associated networks in an attempt to connect to one of them.  
* These small packets, called probe requests, are publicly viewable by anyone in the area running trivially simple sniffing software. 
* Probe requests include a unique device fingerprint called a MAC address that can be used to specifically identify each device. 

### Sources

* (http://www.rfwireless-world.com/Terminology/WLAN-probe-request-and-response-frame.html)
* (https://medium.com/@brannondorsey/wi-fi-is-broken-3f6054210fa5)
