import math
import sys
 
#####################

# This block will degrade the input data and write the degraded data in a file.


####################



def degrade(data, level):
	return str(math.floor(float(data)*10**(2*level))/10**(2*level))

def main(PathToInputFile,PathToOutputFile,degradationLevels):

    inputFile = open(PathToInputFile, 'r')
    outputFile = open(PathToOutputFile, 'a')
    for line in inputFile:
        data = line.split(' ; ')

        for i in range(degradationLevels-1, -1, -1):
            outputFile.write( degrade(data[0],i) + " ; " + degrade(data[-1],i) + "\n")
        
        outputFile.write("---\n")

    outputFile.close()
    inputFile.close()	


if __name__ == "__main__":
    sys.exit(main(sys.argv[1],sys.argv[2],sys.argv[3]))


     