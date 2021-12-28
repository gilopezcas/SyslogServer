import time
import threading
import socketserver
import os
from datetime import date
import getSyslogData as sd

HOST		= '0.0.0.0'
UDP_PORT 	= 514
listening   = False
SyslogFolder = 'C:\\ProgramData\\CI24\\Logs\\Syslog'

class UDPHandler(socketserver.BaseRequestHandler):
	def handle(self):
		data = self.request[0].strip()
		data = str(data)
		IPHost = self.client_address[0]
		scanData = sd.evaluateData(data)
		SyslogFolder = 'C:\\ProgramData\\CI24\\Logs\\Syslog'
		if(os.path.exists(SyslogFolder) == False):
			os.makedirs(SyslogFolder)
		os.chdir(SyslogFolder)
		SyslogMSG = IPHost + '\t' + scanData[5][:-1] + '\t' + scanData[2] + '\t' + scanData[3] + '\t' + scanData[4] + '\t\t' + scanData[1]
		SyslogFile = open('syslog','a')
		SyslogFile.write(SyslogMSG)
		SyslogFile.write('\n')
		logFolder = SyslogFolder + '\\' + scanData[2]
		if(os.path.exists(logFolder) == False):
			os.makedirs(logFolder)
		os.chdir(logFolder)
		logFile = open((str(date.today()) + '.log'),'a')
		HostMSG = scanData[5] + scanData[0] + scanData[1]
		logFile.write(HostMSG)
		logFile.write('\n')

if __name__ == "__main__":
	listening = True
	try:
		udpServer = socketserver.UDPServer((HOST, UDP_PORT), UDPHandler)
		udpThread = threading.Thread(target=udpServer.serve_forever)
		udpThread.daemon = True
		udpThread.start()
		
		while True:
			time.sleep(1)

	except (IOError, SystemExit):
		raise
	except KeyboardInterrupt:
		listening = False
		udpServer.shutdown()
		udpServer.server_close()
		print ("Crtl+C Pressed. Shutting down.")