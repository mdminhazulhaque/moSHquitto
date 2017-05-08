# moSHquitto

moSHquitto is a Shell that works over MQTT protocol. This tool might come handy when there is no direct SSH connection with the remote device.

MQTT is very reliable, has very low overhead and automatically connects when the internet connection is available.

## Setup

* The client script requires `lua` and `lua-mosquitto` module.
* The console application is written using `pyqt5` and `paho-mqtt`.

Put `client/mqttshell.lua` in remote machine and make sure that it runs always. Say the mac address of the device is `aa:bb:cc:dd:ee:ff`, so remote machine will listen for data on topic `shell/aa:bb:cc:dd:ee:ff/execute`.

Anything published to this topic will be executed, for example `ls -l /` is a valid command.

**DO NOT ENTER COMMANDS LIKE `nano /etc/issue`**. This will make the remote application crash. To recover from such situation, do reboot the machine.

To get results from remote machine, subscribe to `shell/aa:bb:cc:dd:ee:ff/result`. Upon the execution of valid command, stdout buffer will be posted to this topic.

For easier console-like feelings, run `console/app.py` and put a mac address of the desired remote machine. Note that remote machine must run the instance of `mqttshell.lua` and should have valid mac address.

## Security?

I know it's not safe. May be you can use TLS Authentication for the clients. This project is a simple proof-of-concept one. Use it with your own risk.

## BUGS

* Cannot use commands that requires writing channel because it is not possible to write to process.
* Found one? Post in the Issues.
