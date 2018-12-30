# coding:utf-8

iplist = []
datafile = open("/Users/liangxuekai/Documents/ip", "r")

for line in datafile.readlines():
    line = line.strip('\n')
    iplist.append(line)
