#!/usr/bin/env python
import socket
import sys


# ------------------------------------------------------------------------------
def char_print_block(block):
    for x in block:
        if ord(x) < 32 or ord(x) > 127:
            sys.stdout.write('.')
        else:
            sys.stdout.write(x)


# ------------------------------------------------------------------------------
def hex_print_block(block, offset):
    sys.stdout.write("%04X: " % (offset))
    for x in block:
        sys.stdout.write("%02X " % (ord(x)))

    pad = 16 - len(block)
    if pad > 0:
        block += pad * ' '

    sys.stdout.write("%s    [" % ('   ' * pad))
    char_print_block(block)
    sys.stdout.write("]\n")


# ------------------------------------------------------------------------------
def hex_print(data):
    print 76 * "-"

    offset = 0

    while offset < len(data):
        block = data[offset:offset+16]
        hex_print_block(block, offset)
        offset += 16

    sys.stdout.flush()


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: %s <ip> <port>" % (sys.argv[0])
        sys.exit(1)

    ip = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ip, port))

    print "Listening to %s:%i" % (ip, port)

    while True:
        try:
            data = s.recv(16384)
            hex_print(data)
        except KeyboardInterrupt:
            break

    print "\nDone!"
