input_arr =  [31,-41,59,26,-53,58,97,-93,-23,84]

#problem 1 and 2
def brute_force(input_arr, better_bool):
    max_sum = 0
    for i in range(0,len(input_arr)): #increase index through the entire input array
        current_sum=0 #reset current_sum between sub arrays
        for j in range(i,len(input_arr)): #loop from i through the end of the the input array
            if (better_bool):
                current_sum += input_arr[j] #find sub array summation the better way
            else:
                current_sum = sum(input_arr[i:j]) 
                
            if current_sum > max_sum: 
                max_sum = current_sum
                max_subarray_index_low = i
                max_subarray_index_high = j+1 
    print(max_sum)
    print(input_arr[max_subarray_index_low:max_subarray_index_high])

#problem 4
def kadanes(input_arr):
        local_max = input_arr[0] 
        global_max = input_arr[0]

        max_subarray_index_low = 0
        max_subarray_index_high = 0
        for i in range(1,len(input_arr)):
            local_max = max(input_arr[i], local_max + input_arr[i]) #local max will be either the current element or the previous subarray plus the current element
            if local_max > global_max:
                global_max = local_max
                max_subarray_index_low = i
            max_subarray_index_high = i

        print(global_max)
        print(input_arr[max_subarray_index_low:max_subarray_index_high])


kadanes(input_arr)
brute_force(input_arr, 'false')


