from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'host': '10.1.3.1',
    'username': '',
    'password': '',
}

S1 = {
    'device_type': 'cisco_ios',
    'host': '10.1.3.2',
    'username': '',
    'password': '',
}

S2 = {
    'device_type': 'cisco_ios',
    'host': '10.1.3.3',
    'username': '',
    'password': '',
}

devices = [R1, S1, S2]
for device in devices:
    if device == S1:
        # connect to the device
        connection = ConnectHandler(**device)
        connection.send_command('host S1')
        connection.send_command('no ip domain-lookup')

        connection.send_config_set(
            'int vlan 1', 'ip add 192.168.1.2 255.255.255.0', 'no shut', 'exit')

        int_mac_address = connection.send_command('sh int vlan 1').splitlines
        for line in int_mac_address:
            if 'address is' in line:
                # splitting the line to get the MAC address, -1 is used to get the last element of the list
                mac_address = line.split(' ')[-1]
                print(f"MAC address of S1: {mac_address}")
                break

        sh_arp = connection.send_command('sh arp')
        print(sh_arp)

        sh_mac = connection.send_command('sh mac address-table')
        print(sh_mac)
