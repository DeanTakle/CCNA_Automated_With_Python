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

devices = [S1, S2]

for device in devices:
    if device == S1:
        # connect to the device
        connection = ConnectHandler(**device)

        # config hostname
        connection.send_command('host Class-A')

        # create vars for passwords
        pass_for_lines = '8ubRU'
        pass_for_secret = 'C9WrE'

        # config passwords for all lines and secret
        connection.send_config_set(
            'line con 0', 'password {}'.format(pass_for_lines), 'login', 'exit')  # .format() is used to format the string with the password stored within the variable pass_for_lines
        connection.send_config_set(
            'lien vty 0 15', 'password {}'.format(pass_for_lines), 'login', 'exit')
        connection.send_command(
            'enable secret {}'.format(pass_for_secret))

        # encrypt all clear text passwords
        connection.send_command('service password-encryption')

        # configure the motd banner
        connection.send_command('banner motd "AUTHORISED USERS ONLY!"')

        # configure IP address for VLAN 1
        connection.send_config_set(
            'int vlan 1', 'ip address 172.16.5.25 255.255.255.0', 'no shut', 'end')

        # save the config to startup
        connection.send_command('copy run start')

    elif device == S2:
        # connect to the device
        connection = ConnectHandler(**device)

        # config hostname
        connection.send_command('host Class-B')

        # create vars for passwords
        pass_for_lines = '8ubRU'
        pass_for_secret = 'C9WrE'

        # config passwords for all lines and secret
        connection.send_config_set(
            'line con 0', 'password {}'.format(pass_for_lines), 'login', 'exit')
        connection.send_config_set(
            'lien vty 0 15', 'password {}'.format(pass_for_lines), 'login', 'exit')
        connection.send_command(
            'enable secret {}'.format(pass_for_secret))

        # encrypt all clear text passwords
        connection.send_command('service password-encryption')

        # configure the motd banner
        connection.send_command('banner motd "AUTHORISED USERS ONLY!"')

        # configure IP address for VLAN 1
        connection.send_config_set(
            'int vlan 1', 'ip address 172.16.5.40 255.255.255.0', 'no shut', 'end')

        # save the config to startup
        connection.send_command('copy run start')
