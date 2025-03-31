from netmiko import ConnectHandler

# As no ip address and SSH has been setup this has to be manually done, however once it has been configured you can use this script without issue.

R1 = {
    'device_type': 'cisco_ios',
    'host': '10.1.3.1',
    'username': '',
    'password': '',
}

R2 = {
    'device_type': 'cisco_ios',
    'host': '10.1.4.1',
    'username': '',
    'password': '',
}

devices = [R1, R2]

for device in devices:
    connection = ConnectHandler(**device)

    if device == R1:

        display_int_status = connection.send_command('sh int')
        print(display_int_status)

        display_serial_status = connection.send_command('sh int s0/0/0')
        print(display_serial_status)

        display_gigeth_status = connection.send_command('sh int g0/0')
        print(display_gigeth_status)

        display_summary = connection.send_command('sh ip int br')
        print(display_summary)

        serial_interfaces = connection.send_command('sh int | include Serial')
        print(serial_interfaces)

        ethernet_interfaces = connection.send_command('sh int | include Eth')
        print(ethernet_interfaces)

        sh_routing_table = connection.send_command('sh ip route')
        print(sh_routing_table)

        def configure_router():
            try:
                configure_g00 = connection.send_config_set(
                    ['int g0/0', 'ip add 192.168.10.1 255.255.255.0', 'desc LAN connection to S1'])
                configure_g01 = connection.send_config_set(
                    ['int g0/1', 'ip add 192.168.11.1 255.255.255.0', 'desc LAN connection to S2', 'end'])
                connection.send_command(configure_g00, configure_g01)

                connection.send_command('copy run start')
            except Exception as e:
                print(f"Error configuring router: {e}")

        int_ips = connection.send_command('sh ip int br')
        print(int_ips)

    elif device == R2:

        display_int_status = connection.send_command('sh int')
        print(display_int_status)

        display_serial_status = connection.send_command('sh int s0/0/0')
        print(display_serial_status)

        display_gigeth_status = connection.send_command('sh int g0/0')
        print(display_gigeth_status)

        display_summary = connection.send_command('sh ip int br')
        print(display_summary)

        serial_interfaces = connection.send_command('sh int | include Serial')
        print(serial_interfaces)

        ethernet_interfaces = connection.send_command('sh int | include Eth')
        print(ethernet_interfaces)

        sh_routing_table = connection.send_command('sh ip route')
        print(sh_routing_table)

        def configure_router():
            try:
                configure_g00 = connection.send_config_set(
                    ['int g0/0', 'ip add 10.1.1.10 255.255.255.0', 'desc LAN connection to S3'])
                configure_g01 = connection.send_config_set(
                    ['int g0/1', 'ip add 10.1.2.10 255.255.255.0', 'desc LAN connection to S4', 'end'])
                connection.send_command(configure_g00, configure_g01)

                connection.send_command('copy run start')
            except Exception as e:
                print(f"Error configuring router: {e}")
