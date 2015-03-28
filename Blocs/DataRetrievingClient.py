# This program allows to get back data from the dht, and use this data to decrypt 


from shutil import copy
from os import remove
import sys



from  II_Cryptography_Block.Code.decrypt import main as blockII
from  III_Shamirs_Block.Code.SecretSharing import reconstruct as blockIII
from  IV_DHT_Block.Code.OWI import main as blockIV

def removeE(path):
   try:
      remove(path)
   except:
      pass


def main(PathtoInputFile, PathToOutputFile,DegradationLevel):
   
   print "Retrieveing Data"
   blockIV("localhost","10000",PathtoInputFile,"./OutputFileBlock4","value")
   blockIII("./OutputFileBlock4","./OutputFileBlock3")
   blockII('./II_Cryptography_Block/Outputs/Encrypted Data/Encrypted Data','./OutputFileBlock3',PathToOutputFile,DegradationLevel)
   print "Data Retrievied"

   removeE('./OutputFileBlock3')
   removeE('./OutputFileBlock4')



if __name__=='__main__':
    sys.exit(main(sys.argv[1],sys.argv[2],sys.argv[3]))
