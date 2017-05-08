from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow

import datetime
import os
import paho.mqtt.client as mqtt
import sys

from window import Ui_window
#os.system("pyuic5 -x window.ui -o window.py")
#os.system("rm window.py")

class MQTTSHELL(QMainWindow):
    trigger = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        
        self.client = mqtt.Client()
        self.ui = Ui_window()
        self.ui.setupUi(self)
        
        self.ui.mac.setText("aa:bb:cc:dd:ee:ff")
        
        self.mac = None
        self.set_widget_status(False)
        self.setWindowTitle("Shell over MQTT")
        self.ui.output.setReadOnly(True)
        self.ui.output.setFont(QFont("Monospace", 10))
        self.ui.output.ensureCursorVisible()
        
        self.trigger.connect(self.handle_trigger)
        self.ui.connect.clicked.connect(self.do_connect)
        self.ui.close.clicked.connect(self.do_quit)
        self.ui.command.returnPressed.connect(self.do_send_cmd)
        
    @pyqtSlot(str)
    def handle_trigger(self, text):
        self.ui.output.appendPlainText(text)
        
    def set_widget_status(self, isenabled):
        self.ui.mac.setEnabled(not isenabled)
        self.ui.output.setEnabled(isenabled)
        self.ui.command.setEnabled(isenabled)
        self.ui.connect.setText("Disconnect" if isenabled else "Connect")
        self.ui.command.setPlaceholderText("Write command and press enter" if isenabled else "Connect to send command")
        
    def do_connect(self):
        if "Disconnect" in self.ui.connect.text():
            self.client.loop_stop()
            self.client.disconnect()
        else:
            self.mac = self.ui.mac.text()
            self.client.username_pw_set("minhaz", "minhaz")
            self.client.connect("localhost", 1883)
            self.client.loop_start()
        
    @pyqtSlot()
    def do_quit(self):
        #self.client.disconnect()
        #self.client.loop_forever()
        # BUG Fix segfault
        QApplication.instance().quit()
        
    def do_send_cmd(self):
        command = self.ui.command.text()
        self.ui.command.clear()
        self.client.publish("shell/" + self.mac + "/execute", command, 2)
        
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.client.subscribe("shell/" + self.mac + "/result", 2)
            self.set_widget_status(True)
            self.ui.command.setFocus()
        
    def on_disconnect(self, client, userdata, rc):
        self.set_widget_status(False)
    
    def on_message(self, client, userdata, msg):
        self.trigger.emit(msg.payload.decode('utf-8'))

    def init_mqtt(self):
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
    
if __name__=="__main__":
    app = QApplication(sys.argv)
    mqttshell = MQTTSHELL()
    mqttshell.show()
    mqttshell.init_mqtt()
    sys.exit(app.exec_())
