#!/usr/bin/env python
# encoding: utf-8



fr = open("verified_users.txt", "r")
fw = open("verified_users.csv", "a")

# read file into memory, still < 20MB
lines = fr.readlines()

# can close reading file
fr.close()

for line in lines:
    # for each line iterate through for first two commas
    j = 0
    first_seg = ""
    second_seg = ""
    third_seg = ""
    for i in range(0,len(line)):
        if line[i] == ",":
            first_seg = line[j:i]
            j = i+1
            break

    if j > len(line):
        print("catastrophic error")
        exit()

    for i in range(j,len(line)):
        if line[i] == ",":
            second_seg = line[j:i]
            j = i+1
            break

    fw.write("\"" + first_seg + "\",\"" + second_seg + "\",\"" + line[j:-1] + "\"\n")

fw.close()
