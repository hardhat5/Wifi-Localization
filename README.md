## WiFi Analytics

### Project outline

* Even when phones are not connected to WiFi networks, they send out signals called __probe requests__ which look around for known networks.
* The idea is to use these signals along with stationary routers to uniquely __identify__ and __locate__ wireless devices in a vicinity.
* Distance of a wireless device from a router can be estimated using the strength of the probe request signal received by the router
* The devices can be uniquely identified using their MAC addresses.

### Project milestones

1. Learn about WiFi networks
2. Implement packet capture in Python
3. Extracting MAC address and signal strength from captured packets
4. Finding devices compatible with OpenWrt and monitor mode
5. Installing OpenWrt on a device
6. Making the build envionment for OpenWrt
7. Implementing packet capture in C
8. Running the application on the device and troubleshooting
9. Distance measurement using signal strength
10. Trilateration(using distances of a point from known points to estimate location)
11. Combining distance readings from multiple devices
