#problem1

input_arr =  [31,-41,59,26,-53,58,97,-93,-23,84]

def brute_force(input_arr, better_bool)
{
    max_sum = 0
    for i in range(0,len(input_arr)): #increase index through the entire input array
        current_sum=0 #reset current_sum between sub arrays
        for j in range(i,len(input_arr)): #loop from i through the end of the the input array
            if (better_bool is true):
                current_sum += input_arr[j] #find sub array summation the better way
            else:
                current_sum = sum(input_arr[i:j]) 
                
            if current_sum > max_sum: 
                max_sum = current_sum
                max_subarray_index_low = i
                max_subarray_index_high = j+1 
    print(max_sum)
    print(input_arr[max_subarray_index_low:max_subarray_index_high])
}

def divide_conquer(input_arr)
{
    


        
}



