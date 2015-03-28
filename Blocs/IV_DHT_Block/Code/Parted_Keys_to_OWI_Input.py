# -*- coding: utf8 -*-

import sys
import OWI
from Crypto.Hash import SHA256



def PartedKeysToOWI(PathToInputFile, PathToOutputFile, PathToOWIInput):
    OutputFile = open(PathToOutputFile, 'w')
    OWIInputFile = open(PathToOWIInput,'w')
    with open(PathToInputFile) as InputFile:
        for line in InputFile:
            lineHash = SHA256.new()
            lineHash.update(line.encode('ascii'))
            if(lineHash.hexdigest() != "e0c83eba658ec47236190c8d557993b46cf79e5e11be555b1198f5dd3abcb249"):
                OutputFile.write("get "+lineHash.hexdigest()+"\n")
                OWIInputFile.write("put "+lineHash.hexdigest()+" "+line)
            else:
                OutputFile.write("*************"+"\n")
    OWIInputFile.close()
    OutputFile.close()


def main(PathToInputFile, PathToOutputFile,Host,Port):
    PartedKeysToOWI(PathToInputFile, PathToOutputFile, "tempfile.owi")
    print "Block 4 : Parted Keys -> OWI File OK !"
    OWI.main(Host,Port,"tempfile.owi","...noOut","...noGet")
    print "Block 4 : Finished"




if __name__=='__main__':    
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
