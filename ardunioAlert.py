#set up serial interface
#
import serial
import smtplib
import time
import smtplib

#Set up emeail stuff
#
SMTPserver = 'smtp'
sender =     'email.com'
destination = 'txt'

# Credentials (if needed)
username = 'email.com'
password = 'pass'

msg = 'Alert something is detected at'

#send type of monitoring
#
ser = serial.Serial('/dev/ttyACM0', 9600)

#types of modes
# W = alert mode, R = reset and T = test mode
ser.write("T")

#open and set up file for writing
#
FILE = open('/tmp/motionFile', 'w')
localtime = time.asctime( time.localtime(time.time()) 

try:
        while 1:
			#set up file to read data and log it
			#
            response = ser.readline()
            FILE.write(response + "_" + localtime);
			
			if(response == "Alert"):
				#handle alert case by sending email
				#
				msg = msg + localtime
				try:
					# The actual mail send
					server = smtplib.SMTP('smtp.com:587')
					server.starttls()
					server.login(username,password)
					server.sendmail(sender, destination, msg)
					server.quit()
				except:
					print "Exception"
				
			
except KeyboardInterrupt:
        ser.close()


#Clean up
#
FILE.close()
ser.close()

