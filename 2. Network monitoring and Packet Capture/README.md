## Network monitoring and packet capture

### Useful tools

### 1. Aircrack-ng

* Used for network monitoring
* It is used to put the wireless card into what is called “monitor mode”.  
* Monitor mode is a special mode that allows your computer to listen to every wireless packet.
* [For Linux] In Terminal, type `ifconfig` to get the name of your wireless device(eg. wlan0).
* Execute sudo `airmon-ng start wlan0` [Replace `wlan0` with device name] so that the wireless device is enabled in monitor mode.

### 2. Wireshark

* Wireshark is used to capture packets that are being transferred over the network.
* Since we need to capture only the probe requests, we need to use a filter.
* Use the filter `wlan.fc.type_subtype==4` so that only probe requests are visible by typing it into the search bar kind of thing at the top of the Wireshark window.

### 3. tcpdump

* It is a command line packet analyzer
* Similar to Wireshark, but no GUI
* Useful when you need to only capture and not analyze
* Filter for probe requests - `sudo tcpdump -w traffic.pcap -i wlan0 -e -s 256 type mgt subtype probe-req` (Replace `wlan0` with your interface)

### Tshark
* Tshark is a terminal oriented version of Wireshark
* Wireshark is built on top of Tshark. Basically, TShark with a GUI

### PyShark
* It is a Python wrapper for tshark, allowing Python packet parsing using wireshark dissectors.
* PyShark will be used for automating packet capture and analysis. 

### Program outline

__Defined Functions__

1. `get_signal_strength(packet)`: Takes a packet as an argument and returns the signal strength in dBm
2. `get_mac_address(packet)`: Takes a packet as an argument and returns the MAC address of the signal source

__LiveCapture Object:__  "cap" is the LiveCapture object which will capture all the traffic on `mon0` but will keep only the probe requests due to the `wlan.fc.type_subtype==4` display filter. 

__The sniff_continuously() method:__ As the name implies, it will continuously sniff packets which can be processed as soon as they are captured. 

__Sources__

1. [Capturing probe requests with tcpdump](https://robinhenniges.com/capture-wifi-wlan-802-11-probe-request-with-tcpdump/)
2. [Capturing probe requests with Wireshark](https://www.willhackforsushi.com/papers/80211_Pocket_Reference_Guide.pdf)
