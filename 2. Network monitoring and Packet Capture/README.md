## Network monitoring and packet capture

__Network monitoring__
* Aircrack-ng is used to put the wireless card into what is called “monitor mode”. 
* Monitor mode is a special mode that allows your computer to listen to every wireless packet.
* [For Linux] In Terminal, type `ifconfig` to get the name of your wireless device(eg. wlan0).
* Execute sudo `airmon-ng start wlan0` [Replace `wlan0` with device name] so that the wireless device is enabled in monitor mode.

__Packet sniffing__
* Wireshark is used to capture packets that are being transferred over the network.
* Since we need to capture only the probe requests, we need to use a filter.
* Use the filter `wlan.fc.type_subtype==4` so that only probe requests are visible by typing it into the search bar kind of thing at the top of the Wireshark window. 
