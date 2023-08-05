import socket
import time


class TclTvRemote:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def keypress(self, key):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.ip, self.port))
        data = '<?xml version="1.0" encoding="utf-8"?><root><action name="setKey" eventAction="' + key + '" keyCode="' + key + '" /></root>'
        client_socket.send(data.encode())

    def send_key(self, keycode):
        self.keypress(self.keycode, self.ip, self.port);

    def go_to_source(self, source):
        self.keypress("TR_KEY_EXIT")
        time.sleep(1)
        self.keypress("TR_KEY_MUTE")
        time.sleep(1)
        self.keypress("TR_KEY_TV")
        time.sleep(6)
        self.keypress("TR_KEY_SOURCE")
        time.sleep(1)
        i = 0
        while i < int(source):
            self.keypress("TR_KEY_DOWN")
            i += 1
        self.keypress("TR_KEY_OK")
        time.sleep(1)
        self.keypress("TR_KEY_MUTE")
