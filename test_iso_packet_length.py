import libusb1

max_packet_size = 256
NUM_ISO_PACKETS = 10

transfer_p = libusb1.libusb_alloc_transfer(NUM_ISO_PACKETS)
transfer = transfer_p.contents
transfer.num_iso_packets = NUM_ISO_PACKETS
libusb1.libusb_set_iso_packet_lengths( transfer_p,
                                       max_packet_size )
