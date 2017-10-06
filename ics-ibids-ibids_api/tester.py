import os

files = os.listdir('pcap')

filtered = [f for f in files if '.pcap' in f]
filtered = [x for x in filtered if not ('capture_111' in x)]

filtered
