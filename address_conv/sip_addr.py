#!/usr/bin/env python

import sys

# addresses where we want to end up
dest = [(0x13400, 0x13401), (0x12400,0x133FF), (0x2400,0x123ff) ]

# addresses where we are at
src = [(0x2400, 0x2401), (0x12408, 0x13407), (0x2408, 0x12407)]


def create_offset(list0, list1):
   offset = []
   for x in range(len(list0)):
         offset.append(list0[x][0] - list1[x][0])
   return  offset



def within_range(num, tup):
    if num >= tup[0] and num <= tup[1]:
        return True
    else:
        return False

def get_offset(num0, num1):
    # if the number we want is bigger
    if num0 > num1:
        return num0 - num1
    else:
        return num1 - num0


offset_list = create_offset(dest,src)

while(1):
    stdin_data = sys.stdin.readline()
    address = int(stdin_data, 16)

    for idx in range(len(src)):
        if within_range(address, src[idx]):
            #print "Within range of " + hex(src[idx][0])
            #print "We will add " + hex(offset_list[idx])
            print hex(address + offset_list[idx])
