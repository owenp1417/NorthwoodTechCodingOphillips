# Import the modules
import subprocess
import ipaddress
import nmap
responding = []
# Prompt the user to input a network address
# For classroom testing, use 172.19.0.16/28
net_addr = input('Please enter a network address in CIDR format (EXAMPLE: 192.168.10.0/29): ')
print()
# Create the network
ip_net = ipaddress.ip_network(net_addr)

# Get all hosts on that network
all_hosts = list(ip_net.hosts())

# Configure subprocess to hide the console window
info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE


# For each IP address in the subnet, 
# run the ping command with subprocess.popen interface
with open('livehosts.txt','w') as file:
    for i in range(len(all_hosts)):
        output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_hosts[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
        
        if "Destination host unreachable" in output.decode('utf-8'):
            #pass
            print(str(all_hosts[i]), "is Offline")
        elif "Request timed out" in output.decode('utf-8'):
            #pass
            print(str(all_hosts[i]), "is Offline")
        else:
            print(str(all_hosts[i]), " is responding")
            responding.append(all_hosts[i])
            file.write(str(all_hosts[i]) + '\n')



# Identify the ports that are being scanned on any open IP addresses
ports = [22,80,135]

# Opens the livehosts text file in read-only mode to view the active IPs
with open('livehosts.txt','r') as fileR:
    for line in fileR:
        target = line.strip()
# Scanning the ports to view their state
        print(f'\nPort info for {target}:')
        for p in ports:
            myscan = nmap.PortScanner()
            myscanner = myscan.scan(target,str(p))
            state = myscanner['scan'][target]['tcp'][p]['state']
            print(f'Port {p} is {state}')

