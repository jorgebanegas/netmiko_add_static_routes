#import paramiko
import time
from netmiko import ConnectHandler

def show_ip_route():
    global cisco
    net_connect = ConnectHandler(**cisco)
    command = "show ip route"
    output = net_connect.send_command(command)
    net_connect.disconnect()
    
    return output

def add_static_route(ip_address,next_hop_address):
    global cisco
    net_connect = ConnectHandler(**cisco)
    command = 'ip route (ip_address) 255.255.255.255 (next_hop)'
    command = command.replace('(ip_address)',ip_address)
    command = command.replace('(next_hop)',next_hop_address)
    output = net_connect.send_config_set(command)
    print(output)
    print("static route added")
    net_connect.disconnect()

def show_static_routes():
    global cisco
    
    net_connect = ConnectHandler(**cisco)
    output = net_connect.send_command("show ip static route")
    net_connect.disconnect()
    
    return output

def show_int_brief():
    global cisco
    net_connect = ConnectHandler(**cisco)
    output = net_connect.send_command("show ip int brief")
    net_connect.disconnect()
    
    return output

host = "x.x.x.x"
username = "username"
password = "password"

ip_address = input("enter ip-address to add: ")
next_hop = input("enter next hop address: ")

cisco = {
        "host":host,
        "username":username,
        "password":password,
        "device_type":"cisco_ios",
        "blocking_timeout":100
        }

print("STATIC ROUTES BEFORE SCRIPT")
print("------------------")
print(show_static_routes())

add_static_route(ip_address,next_hop)


print("STATIC ROUTES AFTER SCRIPT")
print("------------------")
print(show_static_routes())