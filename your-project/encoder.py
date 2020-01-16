import base64
from datetime import datetime


class Encoder:

    def encode_str(self, msg, encriptor):
        encoded_bytes = base64.b64encode(msg.encode("utf-8"))
        encoded_str = str(int.from_bytes(encoded_bytes, byteorder = 'big'), "utf-8")
        separator = len(encoded_str) / 2
        encoded_parts = [encoded_str[:separator], encoded_str[separator:]]
        return [int(i) * encriptor for i in encoded_parts]
    
    def decode_str(self, msg, encriptor):
        # TODO: ERROR --> split msg string in 2 instead of casting to int
        """msg_bytes = bytes(int(msg / encriptor))
        encodedStr = str(msg_bytes, "utf-8")
        decodedBytes = base64.b64decode(encodedStr)
        return str(decodedBytes, "utf-8")
        """
        encoded_int = sum([i / 2 for i in msg])
        encoded_bytes = bytes(encoded_int)

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
        print('encriptor: ', self.encriptors[-1])
        self.messages.append(self.encoder.encode_str(msg, self.encriptors[-1]))
        self.add_new_encriptor()

    def read_message(self, pos):
        return self.encoder.decode_str(self.messages[pos], self.encriptors[0])


mgr = MessageManager()
msg = 'hola gramola'
mgr.add_message(msg)
print(mgr.messages[0])

print(mgr.read_message(0))















