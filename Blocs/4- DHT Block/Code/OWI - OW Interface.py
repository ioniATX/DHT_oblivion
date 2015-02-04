# -*- coding: utf8 -*-

import sys
import telnetlib

# This little script will be the interface with OW, it will create a telnet client on a specific port, and read a file to send the commands.
#  the arguments should be send like this : Host Port PathToFileToRead PathToOutputFile


# Part to watch if the number of arguments is correct, use len(sys.argv)

def sendCommand(connection,file):
    connection.write(file.readline().encode('ascii'))
    connection.read_until(b"Ready.")
    return  connection.read_until(b"Ready.",5)


def get(object, Response, index): #object = "value" or "key"
    ParsedResponse = Response.split("\n")
    count = 0
    for string in ParsedResponse:
        if (object in string):
            break
        count +=1
    try:
        Outputs = ParsedResponse[count].split(" ")
        print Outputs
        return Outputs[index]
    except: 
        return ParsedResponse[1]

def getValue(file):
    return get("value:",file,1)


def getKey(file):
    return get("key:",file,3)    


scriptArguments = sys.argv

    
#  ************************************************************************************************************

HOST = scriptArguments[1]
Port = scriptArguments[2]

telnetConnection = telnetlib.Telnet(HOST, Port)

#There shouldn't be any login/password on the emulator

CommandsToNode = open(scriptArguments[3])

telnetResponse = sendCommand(telnetConnection,CommandsToNode)


if(scriptArguments[4] == "...noOut"):
    print "Ok"
else:
    outfile = open(scriptArguments[4],'w')
    outfile.write(getKey(telnetResponse))