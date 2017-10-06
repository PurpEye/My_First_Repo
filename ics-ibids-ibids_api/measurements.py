import os


def perform_filter(file_to_filter, flag_val):
    if flag_val == 'tcp':
        os.system(
            "su -c 'tshark -r pcap/%s -T fields -e frame.time_delta > txt/%s_FrameTimeDelta.txt' -s /bin/sh rn" % (
                file_to_filter, file_to_filter))  # pcap to txt file

    if flag_val == 'icmp':
        os.system(
            "tshark -r pcap/%s -Y icmp.type==0 -T fields -e frame.time_delta > txt/%s_FrameTimeDelta.txt" % (
                file_to_filter, file_to_filter))  # pcap to txt file
