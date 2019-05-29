## Extracting MAC address and signal strength from packets

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
