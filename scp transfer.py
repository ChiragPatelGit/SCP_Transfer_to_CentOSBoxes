from netmiko import ConnectHandler
from netmiko import file_transfer


def transfer_to_Servers(connection, file_lst, file_sys):

    """
    Transfers files to the server at the directory indicated within the file_sys param
    """
    for i in range(len(file_lst)):
        transfer_output = file_transfer(connection, source_file= file_lst[i], file_system= file_sys, dest_file= file_lst[i], direction='put', overwrite_file=True)
        print(transfer_output)


target_count = ""
while target_count.isdigit() == False:
    target_count = input("How many servers ? ")

target_count = int(target_count)
    

starting_net_address = "10.8.209.20"

target_addrs = [starting_net_address + str(i) for i in range(target_count) ]
server_connections = [] # list of server connections
net_scripts_filenames = ["ifcfg-eno1", "ifcfg-eno2", "ifcfg-enp94s0f0", "ifcfg-enp94s0f1"]
net_scripts_filesys = "/etc/sysconfig/network-scripts"

for i in range(len(target_addrs)):
    """
    creates a list of connection based on the number of servers inputed by user
    """
    CentOSBox = { # each connection's credentials
        "device_type": "linux",
        "host": target_addrs[i],
        "username": "root",
        "password": "password"
    }
    net_connect = ConnectHandler(**CentOSBox)
    print(net_connect.host)
    
    server_connections.append(net_connect)    
    

for i in range(len(server_connections)):

    #traverses all the server connetions to transfer files

    transfer_to_Servers(server_connections[i], net_scripts_filenames,net_scripts_filesys)
    server_connections[i].disconnect()




