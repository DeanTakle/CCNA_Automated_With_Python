from netmiko import ConnectHandler

# As no ip address and SSH has been setup this has to be manually done, however once it has been configured you can use this script without issue.

R1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.253',
    'username': '',
    'password': '',
}


def RouterConfig():

    running_config = Connection.send_command('sh run')
    print(running_config)

    nvram_config = Connection.send_command('sh start')
    print(nvram_config)

    Connection = ConnectHandler(**R1)
    Connection.send_command('host R1')
    Connection.send_command(
        'banner motd # Unauthorized access is strictly prohibited. ')

    def passwords():
        Connection.send_command('enable password cisco')
        Connection.send_command('enable secret itsasecret')
        Connection.send_config_set(
            'line con 0', 'password cisco', 'login', 'exit')
    Connection.send_command(passwords())

    Connection.send_command('service password-encryption')

    Connection.send_command('copy run start')
    Connection.send_command('copy start flash')

    Connection.disconnect()
