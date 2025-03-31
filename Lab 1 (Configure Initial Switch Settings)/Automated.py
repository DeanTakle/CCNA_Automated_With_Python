from netmiko import ConnectHandler

# As no ip address and SSH has been setup this has to be manually done, however once it has been configured you can use this script without issue.

S1 = {
    'device_type': 'cisco_ios',
    'host': '10.0.1.2',
    'username': '',
    'password': '',
}

S2 = {
    'device_type': 'cisco_ios',
    'host': '10.0.1.3',
    'username': '',
    'password': '',
}

devices = [S1, S2]

for device in devices:
    if device == S1:
        connection = ConnectHandler(**device)
        connection.send_command('host S1')
        connection.send_config_set(
            'line con 0', 'password letmein', 'login', 'exit')
        connection.send_config_set(
            'enable password c1$c0', 'enable secret itsasecret')
        connection.send_command('banner motd "AUTHORISED USERS ONLY!"')
        connection.send_command('service password-encryption')

        check_config = connection.send_command('show run')
        print(check_config)

        connection.send_command('copy run start')

        connection.disconnect()

    elif device == S2:
        connection = ConnectHandler(**device)

        connection.send_command('host S2')
        connection.send_config_set(
            'line con 0', 'password letmein', 'login', 'exit')
        connection.send_config_set(
            'enable password c1$c0', 'enable secret itsasecret')
        connection.send_command('banner motd "AUTHORISED USERS ONLY!"')
        connection.send_command('service password-encryption')

        check_config = connection.send_command('show run')
        print(check_config)

        connection.send_command('copy run start')

        connection.disconnect()

    else:
        print('No device found')

print('Configuration completed')
