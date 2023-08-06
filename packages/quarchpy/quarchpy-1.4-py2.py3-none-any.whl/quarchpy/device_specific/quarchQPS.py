from device import quarchDevice
import os, time, datetime, sys


def timeToQPSStamp( t ):
    return int(round(t * 1000))

# Using standard Unix time,  milliseconds since the epoch (midnight 1 January 1970 UTC)
# Should avoid issues with time zones and summer time correction but the local and host
# clocks should still be synchronised
def qpsNowStr():
    return str( timeToQPSStamp(time.time() ) )                          # datetime supports microseconds



class quarchQPS(quarchDevice):
    def __init__(self, quarchDevice):
        self.quarchDevice = quarchDevice
        self.ConType = quarchDevice.ConType
        self.ConString = quarchDevice.ConString

        self.connectionObj = quarchDevice.connectionObj
        self.IP_address = quarchDevice.connectionObj.qps.host
        self.port_number = quarchDevice.connectionObj.qps.port

    def startStream(self, directory):
        return quarchStream(self.quarchDevice, directory)
    
    

class quarchStream(quarchQPS):
    def __init__(self, quarchQPS, directory):
        self.connectionObj = quarchQPS.connectionObj
        
        self.IP_address = quarchQPS.connectionObj.qps.host
        self.port_number = quarchQPS.connectionObj.qps.port

        self.ConString = quarchQPS.ConString
        self.ConType = quarchQPS.ConType
        
        time.sleep(1)
      
        #check to see if any invalid file entries
        newDirectory = self.failCheck(directory)
        
    def failCheck(self, newDirectory):
        validResponse = False
        while (validResponse == False):
            #send the command to start stream
            response = self.connectionObj.qps.sendCmdVerbose( "$start stream " + str(newDirectory))
            #if the stream fails, loop until user enters valid name
            if "Fail" in response:
                print (response + "Please enter a new file name:")
                #grab directory bar end file / folder
                path = os.path.dirname(newDirectory)
                #get a new file name
                if sys.version_info.major==3:                    
                    newEnd = input()
                else:
                    newEnd = raw_input()
                #append user input to directory
                newDirectory = path.replace("\\\\","\\") + newEnd
            else:
                validResponse = True;
        return newDirectory

        
    def addAnnotation(self, annotationString, annotaionTime = 0):
        if annotaionTime == 0:
            annotaionTime = qpsNowStr()
        else:
            annotaionTime = str(timeToQPSStamp(annotaionTime))

        return self.connectionObj.qps.sendCmdVerbose("$annotate " + str(annotaionTime) + " " + annotationString)


    def createChannel(self, channelName, channelGroup, baseUnits, usePrefix):
        #Conditions to convert false / true inputs to specification input
        if usePrefix == False: 
            usePrefix = "no"
        if usePrefix == True:
            usePrefix = "yes"

        return self.connectionObj.qps.sendCmdVerbose("$create channel " + channelName + " " + channelGroup	+ " " + baseUnits + " " + usePrefix)

             
    def stopStream(self):
        return self.connectionObj.qps.sendCmdVerbose("$stop stream")
            

    #function to add a data point the the stream
    #time value will default to current time if none passed
    def addDataPoint(self, channelName, groupName, driveTemp, dataPointTime = 0):
        if dataPointTime == 0:
            dataPointTime = qpsNowStr()
        else:
            dataPointTime = str(timeToQPSStamp(dataPointTime))
        self.connectionObj.qps.sendCmdVerbose("$log " + channelName + " " + groupName + " " + str(dataPointTime) + " " + str(driveTemp))


    



