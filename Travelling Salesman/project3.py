import sys, getopt, linecache, math
import numpy as np
# lets parse the input into a adjacency list, each distance caluclation 
    # will likely need to be performed at least once, may as well do the calculation upfront
def parse_input(ifile):
    f = open(ifile, 'r') 
    #get linecount
    for linecount, _ in enumerate(f):
        pass
    linecount += 1 #enumerate comes one short
    print(linecount)
    #init adjacency list
    adj_arr = [[0] * linecount for i in range(linecount)]
    for i in range(0,linecount):
        line = (linecache.getline(ifile, i+1)).split(" ")
        outer_lat = int(line[1])
        outer_long = int(line[2])
        print(line[0])
        for j in range(0,linecount):
            if i == j:
                adj_arr[i][j] = 0 #same start / destination 
            else:
                line = (linecache.getline(ifile, j+1)).split( " " )
                inner_lat = int(line[1])
                inner_long = int(line[2])
                adj_arr[i][j] = round(math.hypot(outer_lat - inner_lat, outer_long - inner_long)) #round off per requirements
    print(np.matrix(adj_arr))
    #print(adj_arr[74][75])


def main(argv):
    opts, args = getopt.getopt(argv,"n:i:")

    for opt, arg in opts:
        if opt == '-i':
                parse_input(arg)
        else:
            print("Usage: project3.py -i <inputfile>")

main(sys.argv[1:])
