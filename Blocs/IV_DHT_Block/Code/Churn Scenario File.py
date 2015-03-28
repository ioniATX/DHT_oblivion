# -*- coding: utf8 -*-
import random
import sys


#ARGUMENTS  Churn(hours) Churn(minutes) Churn(secondes) StandardDevi NumberofNodes OutFile


# This little script will be able to create little parts of senarios for Overlay Weaver, those parts will emulate the churn
# The nodes emu0 and emu1 will be used to interact with the DHT via telnet, but we always give the total number of Nodes to this script
# All nodes that are turned off, will be restarted after 5 seconds.


def main(churnmean, StandardDevi, numberofnodes, outfilename):
    outfile = open(outfilename,'w')

    # this loop will start at 2 (emu0 and emu1 will be used for direct interactions, and shouldn't be turned off)
    for nodenumber in range(2,numberofnodes):
        nodeChurn = int(random.gauss(churnmean, StandardDevi))
        while(nodeChurn < 0):
            nodeChurn = int(random.gauss(churnmean, StandardDevi))
        outfile.write("schedule "+str(nodeChurn)+" control "+str(nodenumber)+" halt \n")
        outfile.write("arg -m emu0 \n")
        outfile.write("schedule "+str(nodeChurn+5000)+" invoke "+str(nodenumber)+ "\n")
    print "File Done"
    outfile.close()



if __name__=='__main__':    
    sys.exit(main(int((3600*int(sys.argv[1])+60*int(sys.argv[2])+int(sys.argv[3]))*(10**3)), int(sys.argv[4]),int(sys.argv[5]),str(sys.argv[6])))