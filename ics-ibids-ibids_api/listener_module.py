from scapy.all import *
import datetime


COUNT_PACKETS = 10000
TIME_OUT_VAL = 300  # 5 Minutes


def node_traffic_capture(node_ip):
    print "Capturing TCP traffic until 10k...."

    packet_capture = sniff(filter='tcp', timeout=TIME_OUT_VAL)

    # REAL value
    # packet_capture = sniff (filter='tcp and host '+node_ip,timeout=TIME_OUT_VAL)

    no_of_packets_captured = len(packet_capture)

    if no_of_packets_captured > COUNT_PACKETS:
        filename_pcap = 'capture_' + datetime.datetime.now().strftime("%m-%d-%H_%M_%S")
        wrpcap(filename_pcap, packet_capture)
        return filename_pcap

    else:
        return -1

        # else:
        # host_icmp.host_measure(host=node_ip,flag='icmp')
