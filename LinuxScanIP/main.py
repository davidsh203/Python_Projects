import os

from colorama import Fore, Style


def get_inet_line():
    """
    return inet line
    search inet word and check if it doesn't belongs loopback interface
    """
    base_info = os.popen('ifconfig').readlines()
    for i, value in enumerate(base_info):
        if "inet" in value and "inet6" not in value:
            if not base_info[i - 1].startswith('lo'):
                return value
    return False


def get_inet_address():
    # return inet address between 'inet' and 'netmask' words

    inet_line = get_inet_line()
    if inet_line:
        inet_index = inet_line.find('inet')
        netmask_index = inet_line.find('netmask')
        start_index = inet_index + 5
        end_index = netmask_index - 2
        inet_address = inet_line[start_index:end_index]
        return inet_address
    return 'not found'


def get_netmask_address():
    # return netmask address between 'netmask' and 'broadcast' words
    inet_line = get_inet_line()
    if inet_line:
        netmask_index = inet_line.find('netmask')
        start_index = netmask_index + 8
        end_index = inet_line.find('broadcast') - 2
        netmask_address = inet_line[start_index:end_index]
        return netmask_address
    return 'not found'


def ping_address(ip):
    # ping address and return 'True' if it used
    command = "ping {0} -c 1".format(ip)
    res = os.popen(command).readlines()
    if "ttl" in res[1]:
        return True
    return False


def short_inet(inet, numToShort):
    """
    cut the irrelevant octets to build new 'inet' address
    numToShort - how many octets to remove from original 'inet' address
    """
    ip1 = None
    inet_copy = inet
    for t in range(numToShort):
        last_point = inet_copy.rfind('.')
        ip1 = inet_copy[:last_point]
        inet_copy = ip1
    return ip1


# main program

print(Fore.GREEN + "START PROGRAM")

ips_used = []
netmask_address = get_netmask_address()
print(Fore.RED + "check netmask address..", Style.RESET_ALL, netmask_address)

inet = get_inet_address()
print(Fore.RED + "check inet address..", Style.RESET_ALL, inet)

if netmask_address == "255.255.255.0":
    for i in range(1, 255):
        ip = short_inet(inet, 1)
        ip = ip + '.{}'.format(i)
        if ping_address(ip):
            print(ip)
            ips_used.append(ip)
        else:
            print('checking the next ip, written here if it used')

elif netmask_address == "255.255.0.0":
    for i in range(1, 255):
        for j in range(1, 255):
            ip = short_inet(inet, 2)
            ip = ip + '.{}.{}'.format(i, j)
            if ping_address(ip):
                print(ip)
                ips_used.append(ip)
            else:
                print('checking the next ip, written here if it used')

elif netmask_address == "255.0.0.0":
    for i in range(1, 255):
        for j in range(1, 255):
            for x in range(1, 255):
                ip = short_inet(inet, 3)
                ip = ip + '.{}.{}.{}'.format(i, j, x)
                if ping_address(ip):
                    print(ip)
                    ips_used.append(ip)
                else:
                    print('checking the next ip, written here if it used')

fs = open('log_scan_ip.txt', 'w')
fs.write("ip addresses that used in the last scan: \n")
for i in ips_used:
    fs.write(i + '\n')
fs.close()

print(Fore.GREEN + "END PROGRAM")
