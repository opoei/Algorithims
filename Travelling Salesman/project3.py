import sys, getopt, linecache, math
import numpy as np
# lets parse the input into a adjacency list, each distance caluclation 
# will likely need to be performed at least once, may as well do the calculation upfront
# could simplify this by computing upper or lower triangle since it's mirrored over the diagonal
def parse_input(ifile):
    f = open(ifile, 'r') 
    #get linecount
    for count,_ in enumerate(f):
        pass
    count += 1 #count comes one short
    global linecount 
    linecount = count

    #init adjacency list
    global adj_arr
    adj_arr = [[0] * linecount for i in range(linecount)]

    #compute distances into adjacency list
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
    f.close()
#    np.print(adj_arr)

def farthest_insertion():
    #start at node 0
    travel_list = []
    travel_list.append(0)
    
    #return farthest node from elements in travel_list 
    def farthest_node():
        max_distance = 0
        idx = 0
        for node in travel_list:
            for ctr in range(0,linecount):
                if ctr in travel_list:
                    pass
                elif adj_arr[node][ctr] > max_distance:
                    max_distance = adj_arr[0][ctr]
                    idx = ctr
        return idx


    #find the closest edge for a given node
    # im trying to minimize the distance to accomodate for the newly inserted node
    def closest_edge(node):
        n1_idx = -1 
        n2_idx = -1
        curr_min = sys.maxsize
        #print(travel_list)
        #print("end of list:",travel_list[-1])
        

        for elem in travel_list:
#            print("current:", elem)
            if elem == linecount-1:
               if adj_arr[node][elem] + adj_arr[node][0] < curr_min:
                    curr_min = adj_arr[node][elem] + adj_arr[node][0] 
                    n1_idx = elem
                    n2_idx = elem+1
            elif adj_arr[node][elem] + adj_arr[node][elem+1] < curr_min:
                curr_min = adj_arr[node][elem] + adj_arr[node][elem+1] 
                n1_idx = elem
                n2_idx = elem+1
        #"delete edge" between n1 and n2, insert node
        travel_list.insert(n2_idx, node)

    #start with a triangle    
    n = farthest_node()
    travel_list.append(n)
    n = farthest_node()
    travel_list.append(n)

    while(len(travel_list) < linecount):
        n = farthest_node()
        closest_edge(n)
    return travel_list

def calc_tour_len(ifile, tour_list):
    distance = 0
    f = open(ifile, 'r')
    for i,j in zip(tour_list, tour_list[1:]):
        line = (linecache.getline(ifile, i+1)).split(" ")
        line2 = (linecache.getline(ifile, j+1)).split( " " )
        distance += round(math.hypot(int(line2[1]) - int(line[1]) , int(line2[2]) - int(line[2]))) #round off per requirements
        print(distance)
    #calcuate cost returning from last node to first
    line = (linecache.getline(ifile, tour_list[-1]+1)).split(" ")
    line2 = (linecache.getline(ifile, tour_list[0]+1)).split( " " )
    distance += round(math.hypot(int(line2[1]) - int(line[1]) , int(line2[2]) - int(line[2]))) #round off per requirements
    f.close()
    return(distance)

        
def write_tour(distance, travel_list, ofile):
    with open(ofile, 'w') as f:
        f.write(str(distance) + '\n')
        for elem in travel_list:
            f.write(str(elem) + '\n')

def main(argv):
    opts, args = getopt.getopt(argv,"n:i:")

    for opt, arg in opts:
        if opt == '-i':
                parse_input(arg)
                travel_list = farthest_insertion()
                print(travel_list)
                distance = calc_tour_len(arg, travel_list)
                write_tour(distance,travel_list, arg +'.out') #temporarily naming it .out since .tour conflicts with solutions
        else:
            print("Usage: project3.py -i <inputfile>")

main(sys.argv[1:])
