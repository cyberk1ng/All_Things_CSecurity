'''
This program sniffs tcp logs from the network interface,
With each log having a unique id, and the src, and dst IPs,
and ports.
Cleans the logs and arrange them in a json format. - George
'''


import scapy.all as scapy
import re, json, time, random, os, logging
from datetime import datetime



def snif(inteface):
    scapy.sniff(iface=inteface, store=False,prn=this_pkt) #this is the sniff function that sniffs on my network ether0
    

def make_log_id():
    logs_ID_checker = []
    for i in range(40):
        uniq_id = random.randint(1,30)
        logs_ID_checker.append(uniq_id) #a new random id is appeded to this list variable 
        pre_processed_id =  list(set(logs_ID_checker))
      
    
    return pre_processed_id

def get_ips_ports(packet):

    log_id = make_log_id()
    log_id = list(set(log_id))
    current_date = datetime.now().strftime("%H-%M-%S")

    get_ip = re.compile(r'\d+\.\d+\.\d+\.\d+') #this regex extracts the ip addresses. 
    get_ports =re.compile(r':\w{5}') #this regex get the ports
    #get_protocol = re.compile(r'[TCP]')

    try:
        mo1 = get_ports.findall(str(packet.summary())) #this is the return value of the ips found with regex.   
        psrc, pdst = mo1 #the return value is then assigned to two variables, the source and dest ip address.
        mo2 = get_ip.findall(str(packet.summary()))#samefor this section but for the ports.
        src, dst = mo2
        #proto = get_protocol.findall(str(packet.summary()))
        #each log is appended to the log_list variable in a formated way.
        arranged_dict = {f'Log_ID# {random.choice(log_id)}':'%s %s: %s ----> %s %s' % (current_date, psrc.lstrip(':'), src, dst, pdst.lstrip(':'))}
        
        return arranged_dict 
    
    except ValueError: #if the regexes fail, the except block return nothing, so none packet types are ignore.
       return None
           

def add_log_to_file(logs):
    try:
        #this portion writes the logs to a file; the program navigates to the NetLogs folder and creates a file to write the logs.
        logDirectory = os.chdir('/Users/gcj/Desktop/NetLogs') #the directory is 1changed.
        newFile = 'tcplog008.log' #creating a new file in that changed folder/directory.
        latestLog = open(newFile, 'a') #a file object is created and saved to a variable and set to write mode
        latestLog.write(f'{logs} \n') #the write function is called and the logs are written into it.
        latestLog.close() #the file get sclosed after the writing.
    except FileNotFoundError:
        print(f"Error: File '{logDirectory}' not found.")
    else:
        latestLog = open(newFile, 'a')
        latestLog.read()
        return latestLog
        
    

def this_pkt(packet): #this is the callback function that is called in the sniff function
  
    logging.basicConfig(filename='LoggingPacket.json', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    #logger = logging.getLogger()

    try:

        if packet.haslayer(scapy.TCP): #this checks if the packet has a tcp layer using scapy. 
            ips_ports = get_ips_ports(packet)
            clean_json_logs = json.dumps(f'{ips_ports}')
            logging.info(clean_json_logs)
            time.sleep(1)

            #print_logs = add_log_to_file(clean_json_logs)    
            #return str(print_logs)
    except ValueError:
        return None
    except TypeError:
        return None
    

packet_log = snif('en0')
#print(packet_log, end='\n')



    




 

