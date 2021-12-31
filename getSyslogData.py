#Scan the syslog data received, getting level, facility, host and mensaje,
#converting to string and print in console with colors to diference de level
#Version 1.0.1

from colorama import init, Fore
init(autoreset=True)
def evaluateData(data):
    data = data[2:-1]
    endLevelData = data.find('>')+1
    levelData = data[0:endLevelData]
    colorLevel = Fore.RESET
    data = data[endLevelData:]
    host = 'Host'
    scanSyslogData = {
        #User
        '<15>':{'level': '[DEBUG]', 'facility': 'User', 'SyslogLevel': 'debug', 'colorLevel': Fore.CYAN},
        '<14>':{'level': '[INFO]', 'facility': 'User', 'SyslogLevel': 'info', 'colorLevel': Fore.GREEN},
        '<12>':{'level': '[WARNIG]', 'facility': 'User', 'SyslogLevel': 'warning', 'colorLevel': Fore.YELLOW},
        '<11>':{'level': '[ERROR]', 'facility': 'User', 'SyslogLevel': 'err', 'colorLevel': Fore.RED},
        '<10>':{'level': '[CRITICAL]', 'facility': 'User', 'SyslogLevel': 'crit', 'colorLevel': Fore.MAGENTA},
        #System
        '<31>':{'level': '[DEBUG]', 'facility': 'System', 'SyslogLevel': 'debug', 'colorLevel': Fore.CYAN},
        '<30>':{'level': '[INFO]', 'facility': 'System', 'SyslogLevel': 'info', 'colorLevel': Fore.GREEN},
        '<28>':{'level': '[WARNIG]', 'facility': 'System', 'SyslogLevel': 'warning', 'colorLevel': Fore.YELLOW},
        '<27>':{'level': '[ERROR]', 'facility': 'System', 'SyslogLevel': 'err', 'colorLevel': Fore.RED},
        '<26>':{'level': '[CRITICAL]', 'facility': 'System', 'SyslogLevel': 'crit', 'colorLevel': Fore.MAGENTA},
        #Audit
        '<111>':{'level': '[DEBUG]', 'facility': 'Audit', 'SyslogLevel': 'debug', 'colorLevel': Fore.CYAN},
        '<110>':{'level': '[INFO]', 'facility': 'Audit', 'SyslogLevel': 'info', 'colorLevel': Fore.GREEN},
        '<108>':{'level': '[WARNIG]', 'facility': 'Audit', 'SyslogLevel': 'warning', 'colorLevel': Fore.YELLOW},
        '<107>':{'level': '[ERROR]', 'facility': 'Audit', 'SyslogLevel': 'err', 'colorLevel': Fore.RED},
        '<106>':{'level': '[CRITICAL]', 'facility': 'Audit', 'SyslogLevel': 'crit', 'colorLevel': Fore.MAGENTA},
        #Alert
        '<119>':{'level': '[DEBUG]', 'facility': 'Alert', 'SyslogLevel': 'debug', 'colorLevel': Fore.CYAN},
        '<118>':{'level': '[INFO]', 'facility': 'Alert', 'SyslogLevel': 'info', 'colorLevel': Fore.GREEN},
        '<116>':{'level': '[WARNIG]', 'facility': 'Alert', 'SyslogLevel': 'warning', 'colorLevel': Fore.YELLOW},
        '<115>':{'level': '[ERROR]', 'facility': 'Alert', 'SyslogLevel': 'err', 'colorLevel': Fore.RED},
        '<114>':{'level': '[CRITICAL]', 'facility': 'Alert', 'SyslogLevel': 'crit', 'colorLevel': Fore.MAGENTA},
        #Local0
        '<135>':{'level': '[DEBUG]', 'facility': 'Local0', 'SyslogLevel': 'debug', 'colorLevel': Fore.CYAN},
        '<134>':{'level': '[INFO]', 'facility': 'Local0', 'SyslogLevel': 'info', 'colorLevel': Fore.GREEN},
        '<132>':{'level': '[WARNIG]', 'facility': 'Local0', 'SyslogLevel': 'warning', 'colorLevel': Fore.YELLOW},
        '<131>':{'level': '[ERROR]', 'facility': 'Local0', 'SyslogLevel': 'err', 'colorLevel': Fore.RED},
        '<130>':{'level': '[CRITICAL]', 'facility': 'Local0', 'SyslogLevel': 'crit', 'colorLevel': Fore.MAGENTA},
        #Local1
        '<143>':{'level': '[DEBUG]', 'facility': 'Local1', 'SyslogLevel': 'debug', 'colorLevel': Fore.CYAN},
        '<142>':{'level': '[INFO]', 'facility': 'Local1', 'SyslogLevel': 'info', 'colorLevel': Fore.GREEN},
        '<140>':{'level': '[WARNIG]', 'facility': 'Local1', 'SyslogLevel': 'warning', 'colorLevel': Fore.YELLOW},
        '<139>':{'level': '[ERROR]', 'facility': 'Local1', 'SyslogLevel': 'err', 'colorLevel': Fore.RED},
        '<138>':{'level': '[CRITICAL]', 'facility': 'Local1', 'SyslogLevel': 'crit', 'colorLevel': Fore.MAGENTA},
        #Local2
        '<151>':{'level': '[DEBUG]', 'facility': 'Local2', 'SyslogLevel': 'debug', 'colorLevel': Fore.CYAN},
        '<150>':{'level': '[INFO]', 'facility': 'Local2', 'SyslogLevel': 'info', 'colorLevel': Fore.GREEN},
        '<148>':{'level': '[WARNIG]', 'facility': 'Local2', 'SyslogLevel': 'warning', 'colorLevel': Fore.YELLOW},
        '<147>':{'level': '[ERROR]', 'facility': 'Local2', 'SyslogLevel': 'err', 'colorLevel': Fore.RED},
        '<146>':{'level': '[CRITICAL]', 'facility': 'Local2', 'SyslogLevel': 'crit', 'colorLevel': Fore.MAGENTA},
        #Local3
        '<159>':{'level': '[DEBUG]', 'facility': 'Local3', 'SyslogLevel': 'debug', 'colorLevel': Fore.CYAN},
        '<158>':{'level': '[INFO]', 'facility': 'Local3', 'SyslogLevel': 'info', 'colorLevel': Fore.GREEN},
        '<156>':{'level': '[WARNIG]', 'facility': 'Local3', 'SyslogLevel': 'warning', 'colorLevel': Fore.YELLOW},
        '<155>':{'level': '[ERROR]', 'facility': 'Local3', 'SyslogLevel': 'err', 'colorLevel': Fore.RED},
        '<154>':{'level': '[CRITICAL]', 'facility': 'Local3', 'SyslogLevel': 'crit', 'colorLevel': Fore.MAGENTA},
        #Local4
        '<167>':{'level': '[DEBUG]', 'facility': 'Local4', 'SyslogLevel': 'debug', 'colorLevel': Fore.CYAN},
        '<166>':{'level': '[INFO]', 'facility': 'Local4', 'SyslogLevel': 'info', 'colorLevel': Fore.GREEN},
        '<164>':{'level': '[WARNIG]', 'facility': 'Local4', 'SyslogLevel': 'warning', 'colorLevel': Fore.YELLOW},
        '<163>':{'level': '[ERROR]', 'facility': 'Local4', 'SyslogLevel': 'err', 'colorLevel': Fore.RED},
        '<162>':{'level': '[CRITICAL]', 'facility': 'Local4', 'SyslogLevel': 'crit', 'colorLevel': Fore.MAGENTA},
        #Local5
        '<175>':{'level': '[DEBUG]', 'facility': 'Local5', 'SyslogLevel': 'debug', 'colorLevel': Fore.CYAN},
        '<174>':{'level': '[INFO]', 'facility': 'Local5', 'SyslogLevel': 'info', 'colorLevel': Fore.GREEN},
        '<172>':{'level': '[WARNIG]', 'facility': 'Local5', 'SyslogLevel': 'warning', 'colorLevel': Fore.YELLOW},
        '<171>':{'level': '[ERROR]', 'facility': 'Local5', 'SyslogLevel': 'err', 'colorLevel': Fore.RED},
        '<170>':{'level': '[CRITICAL]', 'facility': 'Local5', 'SyslogLevel': 'crit', 'colorLevel': Fore.MAGENTA},
        #Local6
        '<183>':{'level': '[DEBUG]', 'facility': 'Local6', 'SyslogLevel': 'debug', 'colorLevel': Fore.CYAN},
        '<182>':{'level': '[INFO]', 'facility': 'Local6', 'SyslogLevel': 'info', 'colorLevel': Fore.GREEN},
        '<180>':{'level': '[WARNIG]', 'facility': 'Local6', 'SyslogLevel': 'warning', 'colorLevel': Fore.YELLOW},
        '<179>':{'level': '[ERROR]', 'facility': 'Local6', 'SyslogLevel': 'err', 'colorLevel': Fore.RED},
        '<178>':{'level': '[CRITICAL]', 'facility': 'ULocal6ser', 'SyslogLevel': 'crit', 'colorLevel': Fore.MAGENTA},
        #Local7
        '<191>':{'level': '[DEBUG]', 'facility': 'Local7', 'SyslogLevel': 'debug', 'colorLevel': Fore.CYAN},
        '<190>':{'level': '[INFO]', 'facility': 'Local7', 'SyslogLevel': 'info', 'colorLevel': Fore.GREEN},
        '<188>':{'level': '[WARNIG]', 'facility': 'Local7', 'SyslogLevel': 'warning', 'colorLevel': Fore.YELLOW},
        '<187>':{'level': '[ERROR]', 'facility': 'Local7', 'SyslogLevel': 'err', 'colorLevel': Fore.RED},
        '<186>':{'level': '[CRITICAL]', 'facility': 'Local7', 'SyslogLevel': 'crit', 'colorLevel': Fore.MAGENTA},
    }
    try:
        getDataScan = scanSyslogData[levelData]
    except KeyError:
        getDataScan = {'level': 'Nivel no encontrado', 'facility': 'System', 'SyslogLevel': 'warning', 'colorLevel': Fore.RESET}
    dateData = data[:16]
    data = data[16:]
    endHost = data.find(' ')
    host = data[:endHost]
    data = data[endHost:]
    level = getDataScan['level']
    facility = getDataScan['facility']
    colorLevel = getDataScan['colorLevel']
    print(colorLevel + dateData + level + Fore.RESET + data)
    mensage = dateData + level + data
    SyslogLevel = getDataScan['SyslogLevel']
    sysData = {'dateData':dateData,'level':level,'host':host,'data':data,'facility':facility,'SyslogLevel':SyslogLevel}
    return sysData