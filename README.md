## WiFi Analytics

### Project outline

* Even when phones are not connected to WiFi networks, they send out signals called __probe requests__ which look around for known networks.
* The idea is to use these signals along with stationary routers to uniquely __identify__ and __locate__ wireless devices in a vicinity.
* Distance of a wireless device from a router can be estimated using the strength of the probe request signal received by the router
* The devices can be uniquely identified using their MAC addresses.

### Project milestones

1. Learn about WiFi networks and IEEE 802.11
2. Network monitoring and packet capture using Aircrack-ng and Wireshark
3. Extracting MAC address and signal strength from captured packets
4. OpenWrt and its uses
5. Finding devices that are compatible with OpenWrt and support monitor mode
6. Installing OpenWrt on a device
7. Estimation of distance from signal strength indicators
8. Implementing packet capture and distance measurement using OpenWrt
9. Router placement considerations
10. Trilateration(using distances of a point from known points to estimate location)
11. Combining distance readings from multiple devices
