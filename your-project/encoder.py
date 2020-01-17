import base64
from datetime import datetime
from pathlib import Path
import os

class Encoder:

    def split_string_in_parts(self, msg):
        spl = []
        for i in range(0, len(msg), 2):
            splitted_part = msg[i:i + 2]
            spl.append(splitted_part)
        return spl

    def encode_str(self, msg, encriptor):
        encoded_bytes = base64.b64encode(msg.encode('utf-8'))
        encoded_str = str(encoded_bytes, 'utf-8')
        encoded_parts = self.split_string_in_parts(encoded_str)
        encoded_parts = encoded_parts[::-1]
        return encoded_parts
    
    def decode_str(self, msg, encriptor):
        msg = msg[::-1]
        encoded_str = ''.join(msg)
        encoded_bytes = bytes(encoded_str, 'utf-8')
        decoded_bytes = base64.b64decode(encoded_bytes)
        return str(decoded_bytes, 'utf-8')

class MessageManager:
    messages = []
    encriptors = []
    encoder = Encoder()
    f = ''
    f_path = ''
    f_lines = 0

    def __init__(self):
        path = input('Please introduce a path to recover old messages: ')
        self.f_path = path + 'decenc'
        data_folder = Path(path + 'decenc')
        if (data_folder.exists()):
            self.f = open(self.f_path, 'r+')
            for line in self.f.readlines():
                spl = []
                for i in range(0, len(line), 2):
                    splitted_part = line[i:i + 2]
                    spl.append(splitted_part)
                self.messages.append(spl)
                self.f_lines += 1
            print('Found previous encripted messages.')
        else:
            self.f = open(path + 'decenc', 'w+')
        self.encriptors = [self.get_second()]

    def get_second(self):
        curr_time = datetime.now()
        return int(curr_time.strftime('%S'))

    def add_new_encriptor(self):
        self.encriptors.append(self.get_second())

    def add_message(self):
        msg = input('Please, introduce the message: ')
        encrypted_msg = ''.join(self.encoder.encode_str(msg, self.encriptors[0]))
        self.messages.append(encrypted_msg)
        self.f.write(encrypted_msg + '\r\n')
        self.add_new_encriptor()
        self.f_lines

    def read_message(self, pos):
        if(len(self.messages) >= (pos)):
            return self.encoder.decode_str(self.messages[pos - 1], self.encriptors[0])
        else:
            return f'out of range, remember there are {len(self.messages)} messages'
    
    def remove_line(self, pos):
        pos -= 1
        self.f.seek(0)
        lines = self.f.readlines()
        self.f = open(self.f_path, 'w+')
        for line in lines:
            if (line != ''.join(self.messages[pos])):
                self.f.write(line)
        self.f.truncate()
        del self.messages[pos]
        self.f_lines -= 1


def exec_menu(mgr):
    print('Please, chose an action:')
    print('1. save a new encrypted message')
    if (mgr.f_lines > 0):
        print('2. delete an existing message')
        print('3. recover a message')
        print('4. ask the unicorn')
    opt = input('\r\n   option selected : ')
    if (opt == '1'):
        mgr.add_message()
    elif (opt == '2'):
        pos = ''
        while not pos.isdigit():
            pos = input('Introduce the position of the requested message: ')
        mgr.remove_line(int(pos))
        print(f'line {pos} removed')
    elif (opt == '3'):
        pos = ''
        while not pos.isdigit():
            pos = input('Introduce the position of the requested message: ')
        print('\r\n---------------------------------------------')
        print(mgr.read_message(int(pos)))
        print('---------------------------------------------')
        input()
    elif (opt == '4'):
        mgr.f.close()
        return False

    return True
    

mgr = MessageManager()
opt = True
print('Welcome to the super duper message encriptor!')
while opt:
    opt = exec_menu(mgr)




