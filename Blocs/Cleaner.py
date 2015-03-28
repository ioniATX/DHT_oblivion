from os import remove
import sys



def removeE(path):
   try:
      remove(path)
   except:
      pass

def main():

   removeE('./I_Data_Degradation_Block/Inputs/Data to Degrade/Data')
   removeE('./I_Data_Degradation_Block/Outputs/Degraded Data/Degraded Data')
   removeE('./II_Cryptography_Block/Outputs/Encryption Keys/Keys')
   removeE('./II_Cryptography_Block/Outputs/Encryption Keys/Record')
   removeE('./II_Cryptography_Block/Outputs/Encrypted Data/Encrypted Data')
   removeE('./II_Cryptography_Block/Inputs/Degraded Data/Degraded Data')
   removeE('./III_Shamirs_Block/Inputs/Encryption Keys/Keys')
   removeE('./III_Shamirs_Block/Outputs/Parted Keys/KeyParts')
   removeE('./IV_DHT_Block/Inputs/Parted Keys/KeyParts')
   removeE('./Record')
   removeE('./PointRecord')
   removeE('./OutputFileBlock3')
   removeE('./OutputFileBlock4')
   removeE('./LocalizationsInstruction')
   removeE('./FinalOutput')
   removeE('./tempfile.owi')

if __name__=='__main__':
    sys.exit(main())
