#Creation a specific number of files to save de syslog data
#Version 1.0.0

import os
from os import remove

def management(folderPath, filePath, fileLimit, data):
    if(os.path.exists(folderPath) == False):
        os.mkdir(folderPath)
    os.chdir(folderPath)

    if(os.path.exists(filePath)):
        sizeFile = os.path.getsize(filePath)
        sizeFile = (sizeFile // 1024) // 1024
        if(sizeFile == 5):
            for i in range(fileLimit, 0, -1):
                newFile = filePath + str(i)
                if(os.path.exists(newFile)):
                    if(newFile == filePath + str(fileLimit)):
                        remove(newFile)
                    else:
                        os.rename(newFile, (filePath + str(i + 1)))
            os.rename(filePath, filePath + '1')

    writeFile = open(filePath, 'a')
    writeFile.write(data)
    writeFile.write('\n')