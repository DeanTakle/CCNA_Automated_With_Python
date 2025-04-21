In the repo I will be going through a vast amount of labs manually and then will be automating them using Python and later on using Ansible.

There will be some labs that cannot be done via the means of automation, as to automate you will need to have and IP address and SSH (Port 22) setup before being able to connect to a device remotley. You can connect to a device via Telnet (Port 23), however SSH is the industry standard due to it being secure by encrypti g data in transit unlike Telnet that has zero encryption.

Everything added to this repository will be added via Git.

I will be using a vast amount of labs stemming from my Uni Course, Niel Anderson and Jeremy's IT Lab

Tech Stack:

CI/CD:
Git

Langauage:
Python:

Python Libraries:
Netmiko

What is Netmiko
Netmiko is a Python Library that makes it easier to automate network configuration, its simplifies error handling, command sending as well as the overall connectivity to network devices.

Why use Netmiko?

Connection Establishment: ConnectHandler class allows for connection to a network device, netmiko works by establishing an SSH session with the device using provided connection parameters.

Command Execution: Netmikos send_command(), send_commands() and send_config_set() makes it easier for commands to be defined and executed using this library, whilst also capturing the output and storing it in a variable if defined.

Output Parsing: Various methods and utilities are included in Netmiko to help in parsing the output of the commands. Inlcudes features such as prompt detection, output cleaning and structured data extraction.

Error Handling: Netmiko handles common SSH and CLI-related errors. These errors include connection timeouts, authentication failures and unexpected prompts.

Vendor Abstraction: Netmiko provides a vendor-agnostic interface, allowing you to use the same script no matter what the vendor is all that needs to happen is change the ios section.
