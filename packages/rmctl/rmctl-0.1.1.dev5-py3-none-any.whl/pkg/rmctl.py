#!/usr/bin/env python

from __future__ import print_function
import os
import time
from argparse import ArgumentParser
from configparser import ConfigParser

import broadlink


def main():
    args = parse_option()
    select_mode(args)


def parse_option():
    usage = '''
    rmctl.py [options]
    
    1.Manually connect the Broadlink device to Wifi
    2.Make device configure, use -m or --make_device option
      ex:broalink_ctl.py -m -d myroom
    3.Learn IR data, use -l or --learn  option and -c or --command option
      ex:broadlink_cli.py -l -d myroom -c light_on
    4.Send IR data, use -s or --send option and -c or --command option
      ex:broadlink_cli.py -s -d myroom -c light_on
    '''

    parser = ArgumentParser(usage)
    parser.add_argument('-c', '--command', action='store', dest='command_name',
                        help='IR data')
    parser.add_argument('-d', '--device', action='store', help='Broadlink device filename')

    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('-u', '--setup', action='store_true',
                      help='Set up WiFi Broadlink device, but this option is not working', dest='setup')
    mode.add_argument('-s', '--send', action='store_true', help='Send IR data', dest='send')
    mode.add_argument('-l', '--learn', action='store_true', help='Learn IR data', dest='learn')
    mode.add_argument('-m', '--make_device', action='store_true', help='Make Broadlink device file', dest='make_device')

    return parser.parse_args()


def select_mode(args):
    if args.make_device:
        make_device_file(args)
        return
    if args.learn:
        learn_data(args.device, args.command_name)
        return
    if args.setup:
        setup()
        return
    send_data(args.device, args.command_name)


def select_device(ip, mac, port='80', type_='10039'):

    host = (ip, int(port))
    type_ = hex(int(type_))
    type_ = int(type_, 16)
    if not isinstance(mac, bytearray):
        mac = bytearray.fromhex(mac)

    device = broadlink.gendevice(type_, host, mac)
    return device


def format_hex(s):
    formatted = ''
    for c in bytearray(s):
        formatted += format(c, '02x')
    return formatted


def show_device_info(device, device_number):
    if device.auth():
        print('device : {}'.format(device_number))

        print('host   : {}:{}'.format(device.host[0], device.host[1]))
        mac = format_hex(device.mac)
        print('mac    : {}'.format(mac))
        print('type   : {}'.format(device.type))


def ask_overwrite(path):
    if os.path.exists(path):
        while True:
            response = raw_input('File already exists,do you overwrite?(y/n):').lower()
            if response == 'y' or response == 'yes':
                return True
            elif response == 'n' or response == 'no':
                return False
    else:
        return True


def write_device_info(path, ip, mac, port='80', type_='10039'):
    if not ask_overwrite(path):
        quit()
    parser = ConfigParser()
    if os.path.exists(path):
        parser.read(path)

    parser['DEFAULT']['ip'] = ip
    parser['DEFAULT']['mac'] = format_hex(mac)
    parser['DEFAULT']['port'] = port
    parser['DEFAULT']['type'] = type_

    if not parser.has_section('commands'):
        parser['commands'] = {}

    with open(path, 'w') as fp:
        parser.write(fp)


def make_device_file(args):
    print('discover...')

    devices = broadlink.discover(timeout=5)
    if len(devices) == 0:
        print('not found broadlink devices')
        quit()

    for i, device in enumerate(devices):
        show_device_info(device, i)

    device_number = input('Press device number : ')
    if not(0 <= int(device_number) < len(devices)):
        raise IndexError

    device = devices[int(device_number)]
    print(device.devtype)
    write_device_info(args.device, device.host[0], device.mac, str(device.host[1]), str(device.devtype))


def write_device_file(filename, device_ini):
    with open(filename, 'w') as f:
        f.write(device_ini)


def learn_data(device_file, command_name):
    parser = ConfigParser()
    parser.read(device_file)
    ip = parser['DEFAULT']['ip']
    mac = parser['DEFAULT']['mac']
    port = parser['DEFAULT']['port']
    type_ = parser['DEFAULT']['type']

    device = select_device(ip, mac, port, type_)
    device.auth()
    device.enter_learning()

    timeout = 30
    device.timeout = timeout
    device.auth()
    t = 0
    data = None
    print('Learning...')
    while(data is None) and t < timeout:
        data = device.check_data()
        if data:
            data = format_hex(data)
            print(data)
            parser['commands'][command_name] = data
            with open(device_file, 'w') as fp:
                parser.write(fp)

            break
        time.sleep(1)
        t += 1


def send_data(device_file, command_name):
    parser = ConfigParser()
    parser.read(device_file)
    ip = parser['DEFAULT']['ip']
    mac = parser['DEFAULT']['mac']
    port = parser['DEFAULT']['port']
    type_ = parser['DEFAULT']['type']
    data = parser['commands'][command_name]
    device = select_device(ip, mac, port, type_)
    device.auth()
    device.send_data(bytearray.fromhex(data))


def setup():

    """This function is not working"""
    print('Setup option is not working')
    quit()
    print('Long press the reset button until the blue Led is blinking quickly')
    print('Long press again until blinking slowly')
    print('Manually connect this device to the Wifi SSID named BlroadlinkProv')
    print('Press security mode (0 = none, 1 = WEP, 2 = WPA1, 3 = WPA2, 4 = WPA1/2)')
    print('Default:3')

    security = raw_input('Security mode:').lower()

    if security == 'none':
        security = 0
    elif security == 'wep':
        security = 1
    elif security == 'wpa1':
        security = 2
    elif (security == 'wpa2') or (security == ''):
        security = 3
    elif security == 'wpa1/2':
        security = 4
    security = int(security)
    if not(0 <= security <= 4):
        raise IndexError

    ssid = raw_input('SSID of your router :')
    if security != 0:
        password = raw_input('Password:')
    else:
        password = ''
    broadlink.setup(ssid, password, security)


if __name__ == '__main__':
    main()
