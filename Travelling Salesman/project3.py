import sys, getopt, linecache, math
import numpy as np
# lets parse the input into a adjacency list, each distance caluclation 
# will likely need to be performed at least once, may as well do the calculation upfront
# could simplify this by computing upper or lower triangle since it's mirrored over the diagonal
def parse_input(ifile):
    f = open(ifile, 'r') 
    #get linecount
    for count, _ in enumerate(f):
        pass
    count += 1 #enumerate comes one short
    global linecount 
    linecount = count

    #init adjacency list
    global adj_arr
    adj_arr = [[0] * linecount for i in range(linecount)]
    for i in range(0,linecount):
        line = (linecache.getline(ifile, i+1)).split(" ")
        outer_lat = int(line[1])
        outer_long = int(line[2])
        for j in range(0,linecount):
            if i == j:
                adj_arr[i][j] = 0 #same start / destination 
            else:
                line = (linecache.getline(ifile, j+1)).split( " " )
                inner_lat = int(line[1])
                inner_long = int(line[2])
                adj_arr[i][j] = round(math.hypot(outer_lat - inner_lat, outer_long - inner_long)) #round off per requirements
    print(np.matrix(adj_arr))

def furthest_insertion():
    #start at node 0
    travel_list = []
    travel_list.append(0)
    
    #find furthest node from elements in travel_list 
    def furthest_node():
        max_distance = 0
        idx = 0
        for node in travel_list:
            for ctr in range(0,linecount):
                if adj_arr[node][ctr] > max_distance:
                    print(adj_arr[0][ctr])
                    max_distance = adj_arr[0][ctr]
                    idx = ctr
        travel_list.append(idx)
        print(travel_list)

    furthest_node()

def main(argv):
    opts, args = getopt.getopt(argv,"n:i:")

    for opt, arg in opts:
        if opt == '-i':
                parse_input(arg)
                furthest_insertion()
        else:
            print("Usage: project3.py -i <inputfile>")

main(sys.argv[1:])
