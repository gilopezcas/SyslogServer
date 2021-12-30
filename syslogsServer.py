import time
import threading
import socketserver
import os
from datetime import date
import getSyslogData as gsd

HOST		= '0.0.0.0'
UDP_PORT 	= 514
listening   = False
SyslogFolder = 'C:\\ProgramData\\CI24\\Logs\\Syslog'

class UDPHandler(socketserver.BaseRequestHandler):
	def handle(self):
		data = self.request[0].strip()
		data = str(data)
		IPHost = self.client_address[0]
		scanData = gsd.evaluateData(data)
		#print(scanData[-1]['level'])
		#print(type(scanData[-1]))
		SyslogFolder = 'C:\\ProgramData\\CI24\\Logs\\Syslog'
		if(os.path.exists(SyslogFolder) == False):
			os.makedirs(SyslogFolder)
		os.chdir(SyslogFolder)
		SyslogMSG = IPHost + '\t' + scanData['dateData'][:-1] + '\t' + scanData['host'] + '\t' + scanData['facility'] + '\t' + scanData['SyslogLevel'] + '\t\t' + scanData['data']
		SyslogFile = open('syslog','a')
		SyslogFile.write(SyslogMSG)
		SyslogFile.write('\n')
		logFolder = SyslogFolder + '\\' + scanData['host']
		if(os.path.exists(logFolder) == False):
			os.makedirs(logFolder)
		os.chdir(logFolder)
		logFile = open((str(date.today()) + '.log'),'a')
		HostMSG = scanData['dateData'] + scanData['level'] + scanData['data']
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