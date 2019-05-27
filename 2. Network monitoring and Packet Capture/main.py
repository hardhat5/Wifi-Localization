import pyshark 

capture = pyshark.LiveCapture(interface='mon1')
capture.sniff(timeout=10)
capture