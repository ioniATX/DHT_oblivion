from shutil import copy
from os import remove
import sys


from  I_Data_Degradation_Block.Code.Degradation import main as blockI
from  II_Cryptography_Block.Code.encrypt import main as blockII
from  III_Shamirs_Block.Code.SecretSharing import main as blockIII
from  IV_DHT_Block.Code.Parted_Keys_to_OWI_Input import main as blockIV

def removeE(path):
   try:
      remove(path)
   except:
      pass

def checkentryInt(var):
    try:
        return int(var)
    except:
        print "Incorrect entry, please retype it."
        var = raw_input()
        var = checkentryInt(var)
        return var

def checkentryFloat(var):
    try:
        return float(var)
    except:
        print "Incorrect entry, please retype it."
        var = raw_input()
        var = checkentryFloat(var)
        return var

def checkentryDuration(var):
    try:
        int(var[0])
        int(var[1])
        int(var[2])
        return var
    except:
        print "Incorrect entry, please retype it. Syntax Hours/Minutes/Seconds"
        var = raw_input()
        var = var.split("/")
        var = checkentryDuration(var)
        return var



def main(n,churn,std):
   n= int(n)
   churn=int(churn)
   std=int(std)
   print "Hello"
   print "Please enter your current latitude:"
   latitude = raw_input()
   latitude = checkentryFloat(latitude)
   print "Please enter your current longitude:"
   longitude = raw_input()
   longitude = checkentryFloat(longitude)
   print "How many degradation levels do you want ?"
   degradationLevels = raw_input()
   degradationLevels = checkentryInt(degradationLevels)

  ################################################################
  # BLOCK 1
  ################################################################

   blockIinput = open('./I_Data_Degradation_Block/Inputs/Data to Degrade/Data', 'w')
   blockIinput.write(str(latitude)+" ; "+str(longitude))
   blockIinput.close()
   blockI('./I_Data_Degradation_Block/Inputs/Data to Degrade/Data','./I_Data_Degradation_Block/Outputs/Degraded Data/Degraded Data',degradationLevels)
   copy('./I_Data_Degradation_Block/Outputs/Degraded Data/Degraded Data' , './II_Cryptography_Block/Inputs/Degraded Data')


  ################################################################
  # BLOCK 2
  ################################################################

   blockII('./II_Cryptography_Block/Inputs/Degraded Data/Degraded Data','./II_Cryptography_Block/Outputs/Encrypted Data/Encrypted Data','./II_Cryptography_Block/Outputs/Encryption Keys/Keys','./II_Cryptography_Block/Outputs/Encryption Keys/Record')
   copy('./II_Cryptography_Block/Outputs/Encryption Keys/Keys' , './III_Shamirs_Block/Inputs/Encryption Keys')



  ################################################################
  # BLOCK 3
  ################################################################

   dataduration = []
   for a in range(0,degradationLevels):
      i = a+1
      print "How long do you want the data of privacy level "+str(i)+" to be available ? (1 is the most private level, the syntax is hours/minutes/seconds)"
      currentduration = raw_input()
      currentduration = currentduration.split("/")
      currentduration = checkentryDuration(currentduration)
      dataduration.append(currentduration)
   


   blockIII('./III_Shamirs_Block/Inputs/Encryption Keys/Keys', './III_Shamirs_Block/Outputs/Parted Keys/KeyParts',churn,dataduration,n,std,'./PointRecord')  
   copy('./III_Shamirs_Block/Outputs/Parted Keys/KeyParts' , './IV_DHT_Block/Inputs/Parted Keys')
   copy('./II_Cryptography_Block/Outputs/Encryption Keys/Record' , '.')
   
  ################################################################
  # BLOCK 4
  ################################################################

   blockIV('./IV_DHT_Block/Inputs/Parted Keys/KeyParts',"./LocalizationsInstruction","127.0.0.1","10000")
   
   FinalOutputFile = open("./FinalOutput","w")
   with open("./Record") as RecordFile:
     PointFile = open("./PointRecord") 
     for line in RecordFile: 
       if(not "*************" in line):
          dataHash = line.split(";")[0]
          i=0
          for i in range(0,n):
             pointline = PointFile.readline()
             pointline = pointline.split("   ")
             FinalOutputFile.write(dataHash +" ; "+ pointline[1])            
   PointFile.close()         
   FinalOutputFile.close()
                  
  ################################################################
  # Cleaning up
  ################################################################

  
   removeE('./I_Data_Degradation_Block/Inputs/Data to Degrade/Data')
   removeE('./I_Data_Degradation_Block/Outputs/Degraded Data/Degraded Data')
   removeE('./II_Cryptography_Block/Outputs/Encryption Keys/Keys')
   removeE('./II_Cryptography_Block/Outputs/Encryption Keys/Record')
   removeE('./II_Cryptography_Block/Inputs/Degraded Data/Degraded Data')
   removeE('./III_Shamirs_Block/Inputs/Encryption Keys/Keys')
   removeE('./III_Shamirs_Block/Outputs/Parted Keys/KeyParts')
   removeE('./IV_DHT_Block/Inputs/Parted Keys')
   removeE('./Record')
   removeE('./PointRecord')
   removeE('./tempfile.owi')
  
if __name__ == "__main__":
      sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))