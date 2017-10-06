#!/bin/sh
cd pcap/
for file in capture_*.pcap
do
	tshark -r "${file}" -Y "icmp.type==0" -T fields -e frame.time_delta > ../txt/"${file}_FrameTimeDelta_cluster.txt"
done
echo "[*] Dumping FrameTimeDelta done"

