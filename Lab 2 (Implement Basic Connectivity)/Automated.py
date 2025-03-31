from netmiko import ConnectHandler

# As no ip address and SSH has been setup this has to be manually done, however once it has been configured you can use this script without issue.

S1 = {
    'device_type': 'cisco_ios',
    'host': '10.1.3.1',
    'username': '',
    'password': '',
}

S2 = {
    'device_type': 'cisco_ios',
    'host': '10.1.3.2',
    'username': '',
    'password': '',
}

devices = [S1, S2]

for device in devices:
    connection = ConnectHandler(**device)

    if device == S1:

        connection.send_command('host S1')
        connection.send_config_set(
            'line con 0', 'password cisco', 'login', 'exit')
        connection.send_command('enable secret class')
        connection.send_command(
            'banner motd # Authorized access only. Violators will be prosecuted to the full extent of the law. #')

        connection.send_config_set(
            'int vlan1', 'ip add 192.168.1.253 255.255.255.0', 'no shut')

        check_config = connection.send_command('do show run')
        print(check_config)

        connection.send_command('do copy run start')

        connection.disconnect()

    elif device == S2:

        connection.send_command('host S2')
        connection.send_config_set(
            'line con 0', 'password cisco', 'login', 'exit')
        connection.send_command('enable secret class')
        connection.send_command(
            'banner motd # Authorized access only. Violators will be prosecuted to the full extent of the law. #')

        connection.send_config_set(
            'int vlan1', 'ip add 192.168.1.254', 'no shut')

        check_config = connection.send_command('do show run')
        print(check_config)

        connection.send_command('do copy run start')

        connection.disconnect()

    else:
        print('No device found')

print('Configuration completed')
