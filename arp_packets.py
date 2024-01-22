import scapy.all as scapy
import pyinputplus as pyip

#this program uses scapy to get the mac address of a given IP on a network (arp request).
#pyinp is used here to get the ip of the target with input validation. (security first)



def get_mac_address(ip): 
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_requestBroadcast = broadcast/arp_request
    answer_list = scapy.srp(arp_requestBroadcast, verbose=False, timeout=1)[0]
    

    client_list = []
    for element in answer_list:
        client_dict = {'ip':element[1].psrc, 'mac': element[1].hwsrc}

        client_list.append(client_dict)

    return client_list



ip = pyip.inputStr(prompt='Enter the ip of the mac address you want > ', allowRegexes=[r'\d{3}\.\d{3}\.\d{3}\.\d{3}\.?'], blockRegexes=[r'^a-zA-Z\W'])

arp_scanResult = get_mac_address(ip)

print(arp_scanResult[0].get('mac'))


def print_result():
    arp_scanResult = get_mac_address(ip)
    for clients in arp_scanResult:
        for k, v in clients.items():
            print(k.ljust(12), v)



