# -*- coding: utf8 -*-

import sys
import telnetlib
from os import remove


#ARGUMENTS : Host Port PathToFileToRead PathToOutputFile getValue/getKey

# This little script will be the interface with OW, it will create a telnet client on a specific port, and read a file to send the commands.
#  the arguments should be send like this : Host Port PathToFileToRead PathToOutputFile




def sendget(connection,line):
    connection.write(line.encode('ascii'))
    connection.read_until(b"Ready.",0.001)
    return  connection.read_until(b"Ready.",0.2)

def sendput(connection,line):
    connection.write(line.encode('ascii'))
    return  connection.read_until(b"Ready.",0.2)

def get(object, Response, index): #object = "value" or "key"
    ParsedResponse = Response.split("\n") # a response will be : Response\nReady.
    count = 0
    for string in ParsedResponse: # the response should be something like value:smt\n key\n ttl:\n
        if (object in string): # the response might be empty or will not contain the desired attribute
            break
        count +=1
    try:
        Outputs = ParsedResponse[count].split(" ") # the response should be something like : value: something or key: foo something
        return Outputs[index] # The order of the response will always be the same.
    except: 
        # print ParsedResponse
        if(len(ParsedResponse)>1):  #every other case should return a "No Value" except if we want to get the key and the value is empty
            if(ParsedResponse[1].startswith("value:")):
                return "No value"
            else:    
                if(ParsedResponse[1].startswith("key:")):
                    return "No value"
                else:
                    return ParsedResponse[1]
            return "No value"
        else:
            return "No value"

def getValue(file):
    return get("value:",file,1)


def getKey(file):
    return get("key:",file,3)    


def main(Host, Port, PathToInputFile, OutputFile,FunctionToCall):

    telnetConnection = telnetlib.Telnet(Host, Port)

    #There shouldn't be any login/password on the emulator
    if(OutputFile != "...noOut"): # no Out is only for "puts"
        outfile = open("./tempfile",'w')
        # outfile = open(OutputFile,'w')
        with open(PathToInputFile) as CommandsToNode:
            for CommandLine in CommandsToNode:
                telnetResponse = sendget(telnetConnection,CommandLine)
                if(FunctionToCall == "getKey" or FunctionToCall == "getkey" or FunctionToCall == "key"):
                    outfile.write(getKey(telnetResponse)+"\n")
                else:
                    l=getValue(telnetResponse)
                    # print l
                    if(not b"Ready" in l):
                        outfile.write(str(l)+"\n")
                    # outfile.write(getValue(telnetResponse)+"\n")
        outfile.close()
        tempfile = open("./tempfile")
        outfile= open(OutputFile,"w")
        for line in tempfile:
            if(not line=="\n"):
                outfile.write(line)
        outfile.close()
        tempfile.close()
        remove("./tempfile")                    
    else: # when there is an output it's a set
        with open(PathToInputFile) as CommandsToNode:
            for CommandLine in CommandsToNode:
                telnetResponse = sendput(telnetConnection,CommandLine)
    telnetConnection.close()
    

if __name__=='__main__':    
    sys.exit(main(sys.argv[1], sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]))