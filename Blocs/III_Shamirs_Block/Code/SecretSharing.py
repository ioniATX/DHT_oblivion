# -*- coding: utf8 -*-
import sys
from Crypto.Hash import SHA256
from secret_sharing_modif import secret_sharing
from secret_sharing_c_modif import secret_sharing_c
import math


####################

# This block will either construct the secret using the secret_sharing library, or it will reconstruct the secret.
# if we try to reconstruct a secret without giving any input parts, an exception will occur.
# else no exception occur even if number of used parts < number of mandatory parts.
# the reconstructed key will just be useless.

####################

def SecretSharing(PathToInputFile, PathToOutputFile,Churn,dataduration, n,StandardDev,PathToPointRecord):
    OutputFile = open(PathToOutputFile, 'w')
    PointRecordFile = open(PathToPointRecord, 'w')
    c = int(Churn)
    std = int(StandardDev)
    klist = [] #k depends of the data, that's why we have a k list

    for duration in dataduration:
        t = int(duration[0])*3600+int(duration[1])*60+int(duration[2])
        if(duration <= c):
            if (int(int(n)*0.5*(1+math.sqrt(1-math.exp(-(((c-t)/(std*math.sqrt(2)))**2)))))>1):
                klist.append(   int(math.ceil(       int(n)*0.5*(1+math.sqrt(1-math.exp(-(((c-t)/(std*math.sqrt(2)))**2)))) + 1  )   ))
            else: # if k<=1, by default, the list will consider k =2 
                klist.append(2)
        else:
            if (int(int(n)*0.5*(1-math.sqrt(1-math.exp(-(((t-c)/std)**2)))))>1):
                klist.append(int(math.ceil(int(n)*0.5*(1-math.sqrt(1-math.exp(-(((t-c)/std)**2)))))  ))
            else: # if k<=1, by default, the list will consider k =2 
                klist.append(2)


    with open(PathToInputFile) as InputFile:
        OutString = ""
        kindex = 0
        k = klist[kindex]
        for line in InputFile: 
            if("---" in line): # for each seperator, we should use the next k in the list, the except is for the last one
                try:
                    kindex = kindex +1
                    k = klist[kindex]
                except:
                    k = k
            else:
                sharecreator = secret_sharing(line,n,k)
                for i in range(0,n): # we put n parts of the secret in the file, k parts are mandatory to reconstruct the secret
                    lineHash = SHA256.new() # we need the hashes to make a table key/keyparts
                    lineHash.update(line)
                    pointHash= SHA256.new() # those are the key parts
                    share = sharecreator.share_random()
                    outstring = str(share[1][0])+";"+str(share[1][1])+"\n"
                    OutputFile.write(outstring)
                    pointHash.update(outstring.encode('ascii'))
                    PointRecordFile.write(lineHash.hexdigest()+"   "+pointHash.hexdigest()+"\n")
                OutputFile.write("*************"+"\n")
    OutputFile.close()


def main(PathToInputFile, PathToOutputFile,Churn,dataduration, n,StandardDev,PathToPointRecord):
    SecretSharing(PathToInputFile, PathToOutputFile, Churn,dataduration,n,StandardDev, PathToPointRecord)
    print "Block 3 : Encryption Keys -> Parted Keys OK !"
    print "Block 3 : Finished"


def reconstruct(PathToInputFile,PathToOutputFile):
    s = secret_sharing_c()
    with open(PathToInputFile) as InputFile:
        for line in InputFile:
            if(not "No value" in line):
                line = line.split(";")
                share = (0,(int(line[0]),long(line[1]))) #We have to respect the syntax of the shamir's secret library
                s.add_share(share)
    with open(PathToOutputFile,'w') as OutputFile:    
        OutputFile.write(s.reconstruct())       

if __name__=='__main__':
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5],sys.argv[6],sys.argv[7]))
