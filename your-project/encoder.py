import base64
from datetime import datetime


class Encoder:

    def split_string_in_parts(self, msg):
        spl = []
        for i in range(0, len(msg), 2):
            splitted_part = msg[i:i + 2]
            print('splitted part', splitted_part)
            splitted_bytes = bytes(splitted_part, 'utf-8')
            print('splitted bytes', splitted_bytes)
            int_val = int.from_bytes(splitted_bytes, byteorder = 'big')
            spl.append(int_val)
        print('splitted -->',spl)
        return spl

    def encode_str(self, msg, encriptor):
        encoded_bytes = base64.b64encode(msg.encode('utf-8'))
        print('encoded bytes', encoded_bytes)
        encoded_str = str(encoded_bytes, 'utf-8')
        print('encoded str', encoded_str)
        encoded_parts = self.split_string_in_parts(encoded_str)
        return [int(i) * encriptor for i in encoded_parts]
    
    def decode_str(self, msg, encriptor):
        encoded_list = []
        for i in msg:
            #print('value i: ', i, ' value encriptor', encriptor, ' result', (i/encriptor))
            base_int = int(i / encriptor)
            #print('base_int',base_int)
            base_bytes = bytes(base_int)
            #print('base_bytes', base_bytes)
            base_str = str(base_bytes,'utf-8')
            encoded_list.append(base_str)

        print(encoded_list)
        encoded_str = ''.join(encoded_list)
        print('encoded_str', encoded_str)
        encoded_bytes = bytes(encoded_str, 'utf-8')
        decoded_bytes = base64.b64decode(encoded_bytes)
        return str(decoded_bytes, 'utf-8')



        """
        encoded_list = [str(int(i / encriptor)) for i in msg]
        encoded_bytes = bytes(int(''.join(encoded_list)))
        print('decoding bytes', encoded_bytes)
        encoded_str = str(encoded_bytes, 'utf-8')
        print('decoding string', encoded_str)
        decoded_bytes = base64.b64decode(encoded_bytes)
        return str(decoded_bytes, 'utf-8')"""

class MessageManager:
    messages = []
    encriptors = []
    encoder = Encoder()

    def get_second(self):
        curr_time = datetime.now()
        return int(curr_time.strftime('%S'))

    def __init__(self):
        self.encriptors = [self.get_second()]

    def add_new_encriptor(self):
        self.encriptors.append(self.get_second())

    def add_message(self, msg):
        print('adding message: ', msg)
        print('encriptor: ', self.encriptors[0])
        self.messages.append(self.encoder.encode_str(msg, self.encriptors[0]))
        self.add_new_encriptor()

    def read_message(self, pos):
        return self.encoder.decode_str(self.messages[pos], self.encriptors[0])


mgr = MessageManager()
msg = 'hola gramola'
mgr.add_message(msg)
print(mgr.messages[0])

print(mgr.read_message(0))















