import serial.tools.list_ports
port = serial.tools.list_ports.comports();
serialIns = serial.Serial()

portList = []

for oneport in port:
    portList.append(str(oneport))
    print(portList)

data = input("select port: /dev/cu.usbserial-")
url = '/dev/cu.usbserial-' +str(data)

for x in range(0, len(portList)):
    if portList[x].startswith(url):
        print(portList[x])

serialIns.baudrate = 9600
serialIns.port = url
serialIns.open()

while True:
    command = input("Give me a command: ")
    serialIns.write(command.encode("utf-8"))
    if command == "exit":
        exit()
