import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout = 0.5
)

ser.isOpen()
#codes = [b'#:GR#',b'#:GD#',b'Sr01:00:00#',b'Sd+00*00:00#',b'MS#',b'Q#']
codes = [b'RC#',b'Mn#',b'Qn#']
for code in codes:
	ser.write(code)
	time.sleep(0.2)
	a = ser.read(12)
	print(a)
	if not code == codes[-1]:
		t = input('next?\n')
	if t == 'n':
		ser.close()
		exit()
	
	
ser.close()

'''
# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout = 0.5)
print('Enter your commands below.\r\nInsert "exit" to leave the application.')

input_=1
while 1 :
    # get keyboard input
    input_ = input(">> ")
    if input_ == 'exit':q
        ser.close()
        exit()
    else:
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        #ser.write((input_ + '\n').encode())
        ser.write(input_.encode())
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out = str(ser.read(10),errors = 'ignore')
            
        if out != '':
            print(">>" + out)
'''
