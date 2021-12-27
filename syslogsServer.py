import time
import threading
import socketserver
import os
from datetime import date
import getSyslogData as sd

HOST		= '0.0.0.0'
UDP_PORT 	= 514
listening   = False

class UDPHandler(socketserver.BaseRequestHandler):
	def handle(self):
		data = self.request[0].strip()
		data = str(data)
		scanData = sd.evaluateData(data)
		logPath = 'E:\\Logs\\'
		if(os.path.exists(logPath + scanData[2]) == False):
			os.makedirs(logPath + scanData[2])
		os.chdir(logPath + scanData[2])
		logFile = open((str(date.today()) + '.log'),'a')
		logFile.write(scanData[1])
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