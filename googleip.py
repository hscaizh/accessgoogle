#coding:utf8
#author:hscaizh
#create on Nov 2, 2014


import re

def get_ips_from_string(string):
    patt = r'[12]?\d?\d.[12]?\d?\d?.[12]?\d?\d?.[12]?\d?\d?'
    ips = re.findall(patt, string)
    ips = list(set(ips))
    
    if "127.0.0.1" in ips:
        ips.remove("127.0.0.1")
    
    return ips

def get_ips_from_url(filepath):
    pass

def is_ip_available(ip):
    pass

def get_ips_from_file(filepath):
    ifs = open(filepath,"r")
    ifstr = ifs.read()
    ips = get_ips_from_string(ifstr)
    ifs.close()
    return ips

if __name__ == "__main__":
    filepath="googleips.txt"
    googleips = get_ips_from_file(filepath)
    print len(googleips)
    print googleips
        