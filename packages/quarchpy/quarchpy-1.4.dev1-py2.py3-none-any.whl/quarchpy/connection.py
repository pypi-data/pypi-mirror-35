import os, sys
import inspect
import time 
from connection_specific.connection_QIS import QisInterface

def startLocalQis(QisPath=None):
   
    if QisPath == None:
        QisPath = os.path.join(os.path.abspath(__file__), "..", "connection_specific", "QIS", "qis.jar")

    else:
        QisPath = QisPath.replace("\r", "\\r")
        QisPath = os.path.normpath(QisPath)

    current_direc = os.getcwd()
    
    os.chdir(QisPath + "\\..")

    startQISchar = "start /b java -Djava.awt.headless=true -jar " + QisPath + " > pipe"

    os.system(startQISchar)

    time.sleep(2)

    os.chdir(current_direc)

    myQis = QisInterface(host='127.0.0.1', port=9722)
    myQis.sendAndReceiveCmd(cmd = "$scan")
    
    time.sleep(3)
    
    myQis.sendAndReceiveCmd(cmd = "$list")
    del myQis
    
    try:
        startLocalQis.func_code = (lambda:None).func_code
    except:
        startLocalQis.__code__ = (lambda:None).__code__ 

def closeQIS(host='127.0.0.1', port=9722):
    myQis = QisInterface(host, port)
    myQis.sendAndReceiveCmd(cmd = "$shutdown")
    del myQis

class QISConnection:
    
    def __init__(self, ConString, host, port):
        
        from connection_QIS import QisInterface
        self.qis = QisInterface(host, port) 	# Create an instance of QisInterface. Before this is ran QIS needs to have been started
        
class PYConnection:
    
    def __init__(self, ConString):
        # Finds the separator.
        Pos = ConString.find (':')
        if Pos is -1:
            raise ValueError ('Please check your module name!')
        # Get the connection type and target.
        self.ConnTypeStr = ConString[0:Pos]
        self.ConnTarget = ConString[(Pos+1):]
        
        if self.ConnTypeStr.lower() == 'rest':
            from connection_ReST import ReSTConn
            self.connection = ReSTConn(self.ConnTarget)
            
        elif self.ConnTypeStr.lower() == 'usb':
            from connection_USB import USBConn
            self.connection = USBConn(self.ConnTarget)
        
        elif self.ConnTypeStr.lower() == 'serial':
            from connection_Serial import SerialConn
            self.connection = SerialConn(self.ConnTarget)
        
        elif self.ConnTypeStr.lower() == 'telnet':
            from connection_Telnet import TelnetConn
            self.connection = TelnetConn(self.ConnTarget)
        
        else:
            return "Please check your connection string."
