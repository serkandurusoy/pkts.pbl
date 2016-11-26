import time
import network
import socket
import machine

moduleID = 'ICAT001'

#Setup network
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
sta_if.active(True)
ap_if.active(True)

#Setup I/O
button1 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
button3 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
button4 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

#FUNCTION -> Start Module
def startUp():
    print('-> [FUNCTION : startUp]')
    #If module is activated as station and not yet connected then connect to network
    if sta_if.active() and not sta_if.isconnected():
        print('Starting Connection ..')
        doConnect()
        pass
    #Start User Mode if module is connected
    if sta_if.active() and sta_if.isconnected():
        print('Getting Module Status ..')
        getModuleStatus()
        print('Starting User Mode ..')
        startUserMode()
        pass
    else:
        print('Network is not ready. User Mode could not be activated.')
        pass

#FUNCTION -> Connect to local wifi network
def doConnect():
    print('-> [FUNCTION : doConnect]')
    tryConnectNo = 0
    if not sta_if.isconnected():
        print('Checking network connection ..')
        #sta_if.connect('I.Cat', '1455268989')
        #sta_if.connect('PEKTAS1', '15263748590')
        #sta_if.connect('iCatphone', '1455268989')
        sta_if.connect('batuzer', 'bthn1042')
        while not sta_if.isconnected():
            tryConnectNo += 1
            time.sleep(2)
            if tryConnectNo == 10:
                print('Tried 10 Times. Cannot setup network connection!')
                break
                pass
            pass
    getModuleStatus()

#FUNCTION -> Start User Mode
def startUserMode():
    button1Count = 0
    button2Count = 0
    button3Count = 0
    button4Count = 0

    print('-> [FUNCTION : startUserMode]')
    print('User Mode Ready..')
    while True:
        buttonStates = str(button1.value()) + str(button2.value()) + str(button3.value()) + str(button4.value())
        if buttonStates is '0111':
            #STOP User Mode
            button1Count += 1
            print('\nB1 Pressed -> ' + buttonStates + ' / Count: ' + str(button1Count) +'\n')
            break
            pass
        if buttonStates is '1011':
            #SEND TCP Message to Server
            button2Count += 1
            print('\nB2 Pressed -> ' + buttonStates + ' / Count: ' + str(button2Count) + '\n')
            talkToServer(moduleID + ' -> Button 2 [' + str(button2Count) + ']')
            pass
        if buttonStates is '1101':
            #SEND TCP Message to Server
            button3Count += 1
            print('\nB3 Pressed -> ' + buttonStates + ' / Count: ' + str(button3Count) + '\n')
            talkToServer(moduleID + ' -> Button 3 [' + str(button3Count) + ']')
            pass
        if buttonStates is '1110':
            #SEND TCP Message to Server
            button4Count += 1
            print('\nB4 Pressed -> ' + buttonStates + ' / Count: ' + str(button4Count) + '\n')
            talkToServer(moduleID + ' -> Button 4 [' + str(button4Count) + ']')
            pass
        pass

#FUNCTION -> Get module status
def getModuleStatus():
    print('-> [FUNCTION : getModuleStatus]')
    #Update module WIFI status as BOOL
    wifiAPStatus = str(ap_if.active())
    wifiSTStatus = str(sta_if.active())
    wifiSTConStatus = str(sta_if.isconnected())

    #Update module WIFI-STATION status as TEXT
    if sta_if.isconnected():
        wifiSTConStatus = 'Online'
    else:
        wifiSTConStatus = 'Offline'

    #Show module status
    print('Module ID : ' + moduleID)
    print('WI-FI Status : [AP] ' + wifiAPStatus + ' | [ST] ' + wifiSTStatus + '/' + wifiSTConStatus)
    print('Network Config :', sta_if.ifconfig())

#FUNCTION -> Connect to Server and send TCP Message
def talkToServer(message):
    print('-> [FUNCTION : talkToServer]')
    address = socket.getaddrinfo('192.168.1.104',9000)[0][-1]
    mySocket = socket.socket()
    mySocket.connect(address)
    mySocket.send(bytes(message, 'utf8'))
    while True:
        data = mySocket.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
            #time.sleep(2)
            mySocket.close()
            print('\nConnection Closed. Waiting ..')
            break
        else:
            break
    pass

#FUNCTION -> Get I2C Devices
def getI2C():
    clockPin = 5
    dataPin = 4
    print('-> [FUNCTION : getI2C]')
    i2c = machine.I2C(machine.Pin(clockPin), machine.Pin(dataPin))
    i2c.scan()
    print('I2C Scan complete!')

#Start Module
startUp()

#Setup I2C
#getI2C()
