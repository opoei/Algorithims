import getopt, sys
#problem 1 and 2
def brute_force(input_arr, better_bool):
    max_sum = 0
    for i in range(0,len(input_arr)): #increase index through the entire input array
        current_sum=0 #reset current_sum between sub arrays
        for j in range(i,len(input_arr)): #loop from i through the end of the the input array
            if (better_bool):
                current_sum += input_arr[j] #find sub array summation the better way
            else:
                current_sum = sum(input_arr[i:j+1]) #not sure why I need the +1 to satisfy the third test case....
                
            if current_sum > max_sum: 
                max_sum = current_sum
                max_subarray_index_low = i
                max_subarray_index_high = j+1 
    print(input_arr[max_subarray_index_low:max_subarray_index_high])
    print(max_sum)
#problem 4
def kadanes(input_arr):
        local_max = input_arr[0] 
        global_max = input_arr[0]

        max_subarray_index_low = 0
        max_subarray_index_high = 0
        for i in range(1,len(input_arr)):
            local_max = max(input_arr[i], local_max + input_arr[i]) 
            if local_max == input_arr[i]:
                max_subarray_index_low = i
            if local_max > global_max: #determine if the old max is still the max
                global_max = local_max
            if local_max == global_max:
                max_subarray_index_high = i + 1


        print(input_arr[max_subarray_index_low:max_subarray_index_high])
        print(global_max)

def main(argv):
    opts, args = getopt.getopt(argv,"n:i:")
    for opt, arg in opts:
        if opt == '-n':
            function_call = arg
            #determine which function to run

        elif opt == '-i':
            with open(arg) as ifile:
                for line in ifile:
                    input_arr = list(map(int, line.split()))
                    print(input_arr)
                    if function_call == '1':
                        brute_force(input_arr, 0)
                    elif function_call == '2':
                        brute_force(input_arr, 1)
                    elif function_call == '3':
                        #do divide and conquer
                        return(1)
                    elif function_call == '4':
                        kadanes(input_arr)
        else:
            print("Usage: project1.py -n <Algorithim #> -i <inputfile>")
main(sys.argv[1:])


