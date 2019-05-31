import pyshark
import re

def get_signal_strength(packet):
    layer = packet[1]
    text = str(layer)
    arr = text.splitlines()
    ss = arr[6]
    a = [int(s) for s in re.findall(r'\d+', ss)]
    return a[0]

def get_mac_address(packet):
    layer = packet[2]
    text = str(layer)
    arr = text.splitlines()
    mac = arr[17]
    mac = mac.strip()
    mac = mac.split("address: ",1)[1] 
    return mac

cap = pyshark.LiveCapture(interface='mon0', display_filter='wlan.fc.type_subtype==4')

for packet in cap.sniff_continuously():
    #packet_type = get_packet_type(packet)
    #if(packet_type==match):
    try:
        mac = get_mac_address(packet)
        ss = get_signal_strength(packet)
        print(mac, ss)
    except:
        pass
