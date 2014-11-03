#coding:utf8
#author:hscaizh
#create on Nov 2, 2014


import re
import socket
import time
import sys
import urllib2

def get_ips_from_string(string):
    patt = r'[12]?\d?\d.[12]?\d?\d?.[12]?\d?\d?.[12]?\d?\d?'
    ips = re.findall(patt, string)
    ips = list(set(ips))
    
    if "127.0.0.1" in ips:
        ips.remove("127.0.0.1")
    
    return ips

def socket_connect_time(ip_address, port):
    #print "testing ip :" + str(ip_address)
    connect_time = 0
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket()
        start_time = time.time()
        s.connect((ip_address,port))
        end_time = time.time()
        connect_time = end_time - start_time
    except:
        connect_time = -1
    finally:
        s.close()
        
    if connect_time > 0:
        #print "found one! " + str(ip_address)
        pass
    return connect_time

def get_ips_from_file(filepath):    
    try:
        ifs = open(filepath,"r")
        ifstr = ifs.read()
        ips = get_ips_from_string(ifstr)
        ifs.close()
    except:
        ips = []
    finally:
        try:
            ifs.close()
        except:
            pass
    return ips

def get_ips_from_url(filepath):
    ips = []
    try:
        ifstr = urllib2.urlopen(filepath, timeout=5).read()+""
        ips = get_ips_from_string(ifstr)
    except:
        pass
    return ips


def is_ip_avaliable(ip):
    flag = False
    try:  
        f = urllib2.urlopen(r"http://"+ip, timeout=5).read()+""
        if f.find("google") > 0:
            flag = True  
    except:
        pass  
    return flag

def get_best_ip(ips,N=10,port=443):
    iplist = []
    best_ip = None
    
    for ip in ips:
        if len(iplist) >= 2*N:
            break
        con_time = socket_connect_time(ip, port)
        if con_time > 0:
            iplist.append((con_time,ip))
    
    #test another time
    ips = [x[1] for x in iplist]
    iplist = []
    for ip in ips:
        if len(iplist) >= N:
            break
        con_time = socket_connect_time(ip, port)
        if con_time > 0:
            iplist.append((con_time,ip))
            
    iplist.sort(key=lambda x:x[1])
    
    ips = [x[1] for x in iplist]
    
    for x in iplist:
        if is_ip_avaliable(x[1]):
            return x[1]
    return None

def _generate_hosts_str(template_str,ip):
    regex = r'[12]?\d?\d.[12]?\d?\d?.[12]?\d?\d?.[12]?\d?\d?'
    result, number = re.subn(regex, ip, template_str)  # @UnusedVariable
    return result

def get_template_str(template_path):    
    try:
        ifs = open(template_path,'r')
        template_str = ifs.read()
    except:
        template_str = ""
    finally:
        try:
            ifs.close()
        except:
            pass
    return template_str

def generate_hosts_file(hoststr,filename="hosts"):
    ofs = open(filename,"w")
    try:
        ofs.write(hoststr)
    finally:
        ofs.close()

def is_url(path):
    if path.startswith("http") or path.startswith("ftp"):
        return True
    return False


if __name__ == "__main__":
    ippath = "googleips.txt"
    if len(sys.argv) > 1:
        ippath = sys.argv[1]
    
    print "ip path:" + ippath
    
    if is_url(ippath):
        ips = get_ips_from_url(ippath)
    else:
        ips = get_ips_from_file(ippath)
        
    best_ip = get_best_ip(ips)
    
    if best_ip != None:
        print "find best ip : " + best_ip
        template_str = get_template_str("hosts")
        hosts_str = _generate_hosts_str(template_str, best_ip)
        generate_hosts_file(hosts_str)
        print "generate hosts complete"
    else:
        print "no ip avaliable, please try again!"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        