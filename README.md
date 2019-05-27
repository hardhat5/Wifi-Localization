## WiFi Analytics

### Project outline
* Even when phones are not connected to WiFi networks, they send out probe requests to look for known networks.
* The idea is to use these request signals and MAC addresses of devices to uniquely localize wireless devices in a location.

### Project milestones
1. WiFi networks and IEEE 802.11
2. Network monitoring and packet capture using Aircrack-ng and Wireshark
3. Extracting MAC address and signal strength from captured packets
4. Estimation of distance from signal strength indicators
5. OpenWrt and its uses
6. Finding devices that are compatible with OpenWrt and support monitor mode
7. Installing OpenWrt on a router
8. Implementing packet capture and distance measurement using OpenWrt
9. Router placement considerations
10. Trilateration(using distances of a point from known points to estimate location)
11. Combining distance readings from multiple devices
