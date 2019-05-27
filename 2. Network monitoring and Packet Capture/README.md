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

__Note__
The probe request sends the MAC address of the source as well as the target device. But, Apple iPhones send out randomized MAC addresses and thus unique identification of iPhones is not possible. Most Android devices however, do not have MAC address randomization enabled.

__Sources__

1. [Capturing probe requests with tcpdump](https://robinhenniges.com/capture-wifi-wlan-802-11-probe-request-with-tcpdump/)
2. [Capturing probe requests with Wireshark](https://www.willhackforsushi.com/papers/80211_Pocket_Reference_Guide.pdf)
