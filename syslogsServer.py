#Syslog Server 1.0.3
#UDP SyslogServer

import time
import threading
import socketserver
import os
from datetime import date
import getSyslogData as gsd
import fileManagement as fm

serverHOST = '0.0.0.0'
portUDP = 514
SyslogFolder = 'C:\\ProgramData\\CI24\\Logs\\Syslog'

class UDPHandler(socketserver.BaseRequestHandler):
	def handle(self):
		data = self.request[0].strip()
		data = str(data)
		IPHost = self.client_address[0]
		scanData = gsd.evaluateData(data)
		SyslogFolder = 'C:\\ProgramData\\CI24\\Logs\\Syslog'
		SyslogMSG = IPHost + '\t' + scanData['dateData'][:-1] + '\t' + scanData['host'] + '\t' + scanData['facility'] + '\t' + scanData['SyslogLevel'] + '\t\t' + scanData['data']
		fm.management(SyslogFolder, 'syslog', 30, SyslogMSG)
		logFolder = SyslogFolder + '\\' + scanData['host']
		HostMSG = scanData['dateData'] + scanData['level'] + scanData['data']
		fm.management(logFolder, (str(date.today()) + '.log'), 30, HostMSG)

if __name__ == "__main__":
	try:
		udpServer = socketserver.UDPServer((serverHOST, portUDP), UDPHandler)
		udpThread = threading.Thread(target=udpServer.serve_forever)
		udpThread.daemon = True
		udpThread.start()
		
		while True:
			time.sleep(1)

	except (IOError, SystemExit):
		raise
	except KeyboardInterrupt:
		udpServer.shutdown()
		udpServer.server_close()
		print ("Crtl+C Pressed. Shutting down.")