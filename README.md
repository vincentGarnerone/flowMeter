# flowMeter
Record flow meter data

In order to record data from the flow meter with a small time step, we need to use two tools: Hterm to set up the flow meter and our own script to get the data sent by the flow meter and record them in a csv file.

1)	Download Hterm : https://www.der-hammer.info/pages/terminal.html
	This allows serial communication with the flow meter. Advised configuration:
	
	Baud=19200
	
	Port=15 or other
	
	Newline at: CR
	
	Send on enter at : CR
	
	Ascii

2)	When connected, commands can be send to the flowmeter with the interface:
	
	*@=@ : streaming mode
	
	*@=A : pulling mode
		
	A$$R91 : read the time step value
		
	A$$W91=30 : set up the time step value to 30ms. Be careful, going too little can result in a bug, minimum advice would be 20ms.
		
3)	**Open the connection, choose a time step, put back the streaming mode, hit the “Disconnect” button.**

4)	With a Python script named “RecordFlowmeter.py” we can now get the values sent by the flow meter and record them in a csv file. (If prefer, you can work with the code 		CommunicationS358Python.py which work with no graphic interface)

5) 	**Spyder** can be used to run the script. When the script is open, **hit the play** button to run it.

6) 	When running the script, a window opens. Choose the number of iterations and hit **“Start record”**. This will create a csv file named according to the time and record
 	the data.

7)	The most common error happening is :
	SerialException: could not open port 'COM15': PermissionError(13, 'Access is denied.', None, 5)
	That means the serial is still connected, and is not possible to create a new connection.
	Try to close the connection, by for example unplugging the USB.




	

