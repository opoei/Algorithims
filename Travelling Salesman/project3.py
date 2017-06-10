import sys, getopt, linecache, math
#import numpy as np

# lets parse the input into a adjacency list, each distance caluclation 
# will likely need to be performed at least once, may as well do the calculation upfront
# could simplify this by computing upper or lower triangle since it's mirrored over the diagonal
def parse_input(ifile):
    f = open(ifile, 'r') 
    #get linecount
    for count,_ in enumerate(f):
        pass
    count += 1 # our inputs count starting at zero. Some functions index at zero, some at one. 
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
    #print(np.array(adj_arr))
    f.close()

def calc_tour_len(ifile, tour_list):
    distance = 0
    f = open(ifile, 'r')
    for i,j in zip(tour_list, tour_list[1:]):
        line = (linecache.getline(ifile, i+1)).split(" ")
        line2 = (linecache.getline(ifile, j+1)).split( " " )
        distance += round(math.hypot(int(line2[1]) - int(line[1]) , int(line2[2]) - int(line[2]))) #round off per requirements
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

def nearest_insertion():
    #start at node 0
    travel_list = [0]
    
    # return closest node from elements in travel_list, that is currently not in travel_list 
    # WARNING: If called after all nodes have been visited, it will return -1 !
    # Two modifications need to be made to make this furthest insertion. max_distance = 0  and adj_arr[node][ctr] > max_distance
    # Based on the example cases, it was found that nearest_insertion performed much better
    def nearest_node():
        min_distance = sys.maxsize
        near_node = -1 
        for node in travel_list:
            for ctr in range(linecount):
                if ctr in travel_list:
                    pass 
                elif adj_arr[node][ctr] < min_distance:
                    min_distance = adj_arr[node][ctr]
                    near_node = ctr
        return near_node 


    #find the closest edge for a given node, insert the node. 
    def closest_edge(node):
        ins_pt = 0
        curr_min = sys.maxsize
        #print(travel_list)
        #print("end of list:",travel_list[-1])
        
        # go pairwise through the travel list (traverse all edges) , 
        # take the minimum distance needed to accomodate for the newly inserted node
        for i,j in zip(travel_list, travel_list[1:]):
            if adj_arr[node][i] + adj_arr[node][j] - adj_arr[i][j] < curr_min:
                curr_min = adj_arr[node][i] + adj_arr[node][j] - adj_arr[i][j]
                ins_pt = travel_list.index(j) #update insertion point
        #check the connection from the tail to the front
        if adj_arr[node][travel_list[-1]] + adj_arr[node][travel_list[0]] - adj_arr[-1][0] < curr_min:
            curr_min = adj_arr[node][travel_list[-1]] + adj_arr[node][travel_list[0]] - adj_arr[-1][0]
            ins_pt = travel_list[0]
        #insert new node 
        travel_list.insert(ins_pt, node)

    #start 
    n = nearest_node()
    travel_list.append(n)

    #loop until all nodes visited
    while True:
        if len(travel_list) == linecount:
           break 
        n = nearest_node()
        if n == -1:
            continue
        closest_edge(n)

    return travel_list

def nearest_neighbor():
    #start at node 0 
    travel_list = [0]
    
    #find the nearest neighbor for a given node
    #returns node that is closest
    def find_nearest_neighbor(node):
        curr_min = sys.maxsize 
        for i in range(linecount):
            if i in travel_list:
               pass 
            elif adj_arr[node][i] < curr_min:
                curr_min = adj_arr[node][i]
                idx = i
        return idx

    while True:
        if len(travel_list) == linecount:
            break
        n = find_nearest_neighbor(travel_list[-1])
        travel_list.append(n)

    return travel_list

def main(argv):
    opts, args = getopt.getopt(argv,"n:i:")

    for opt, arg in opts:
        if opt == '-i':
                parse_input(arg)
                travel_list = nearest_insertion()
                distance = calc_tour_len(arg, travel_list)
                write_tour(distance,travel_list, arg + '.tour') #temporarily naming it .out since .tour conflicts with solutions
        else:
            print("Usage: project3.py -i <inputfile>")

main(sys.argv[1:])
