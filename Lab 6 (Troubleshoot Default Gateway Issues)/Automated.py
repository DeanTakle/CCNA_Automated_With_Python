from netmiko import ConnectHandler

# As no ip address and SSH has been setup this has to be manually done, however once it has been configured you can use this script without issue.

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
    connection = ConnectHandler(**device)

    if device == R1:

        int_ips = connection.send_command('sh ip int br')
        print(int_ips)

        for line in int_ips.splitlines():
            if 'g0/0' in line:
                if 'unassigned' in line:
                    connection.send_config_set(
                        'int g0/0', 'ip address 192.168.10.1 255.255.255.0', 'no shut', 'end')
            elif 'g0/1' in line:
                if 'unassigned' in line:
                    connection.send_config_set(
                        'int g0/1', 'ip address 192.168.11.1 255.255.255.0', 'no shut', 'end')
            else:
                continue

    elif device == S1:
        default_gateway = connection.send_command(
            'sh run | inc ip default-gateway')
        print(default_gateway)

        vlan_ip = connection.send_command('sh ip int br | inc Vlan1')

        if 'ip default-gateway' not in default_gateway:
            connection.send_command('ip default-gateway 192.168.10.1')
        else:
            print("Default gateway already configured.")

        if 'Vlan1' in line:
            if 'unassigned' in line:
                connection.send_config_set(
                    'int Vlan1', 'ip add 192.168.10.2 255.255.255.0', 'no shut', 'end')
        else:
            print("Vlan1 already configured.")

    elif device == S2:
        default_gateway = connection.send_command(
            'sh run | inc ip default-gateway')
        print(default_gateway)

        vlan_ip = connection.send_command('sh ip int br | inc Vlan1')

        if 'ip default-gateway' not in default_gateway:
            connection.send_command('ip default-gateway 192.168.11.1')
        else:
            print("Default gateway already configured.")

        if 'Vlan1' in line:
            if 'unassigned' in line:
                connection.send_config_set(
                    'int Vlan1', 'ip add 192.168.11.2 255.255.255.0', 'no shut', 'end')
        else:
            print("Vlan1 already configured.")
