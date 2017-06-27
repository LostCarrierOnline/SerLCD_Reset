import serial
import sys
import glob

def reset():
    print('\r\nSending')
    print('Please connect your UART tx pin to the rx pin of your SerLCD now')
    print('press ctrl-c to stop')
    while True:
        ser.write('bogus\r'.encode())


def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result





print('Welcome to the SerLCD Reset Tool!\r\n')
print('According to the documentation if you send a CR within the few miliseconds during boot you can reset it.\r\n')
print('Please ensure only power and ground are connected, once you start the proceedure connect your UART TX connection to the RX connector on your serLCD package.\r\n\r\n')

print(serial_ports())

comPort = input('\r\nEnter com port number ONLY: ')

ser = serial.Serial(
    port='COM' + comPort,
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)


input('Press Enter to Start Sending')

while True:
    reset()
