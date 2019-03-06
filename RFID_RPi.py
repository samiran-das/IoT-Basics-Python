# Gets the data from RFID Tags using a RFID USB Reader 
# Prints the ID of that Tag after decoding and conversion (UTF-8)
# Samiran Das - github.com/samiran-das

import serial
port = serial.Serial('/dev/ttyUSB0', 9600)
id= []
i=0
while True:

	serial_data = port.read()
	data = serial_data.decode('utf-8')
	i=i+1
	if i==12:
		i=0
		ID = ''.join(map(str,id))
		print("ID: {}". format (ID))
		id[:]=[]
		del data
		del ID
	else: 
		id.append(data)

# End of code
