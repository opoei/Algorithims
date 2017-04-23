#!/usr/bin/python3
import getopt, sys
from sys import argv

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

# problem 3
def divide_conquer(input_arr):
    # intiialize variables.
    # temp is for the computation below
    mid_point = 0
    left_max_value = 0
    right_max_value = 0
    temp_value = 0
    temp_value1 = 0
    temp_value2 = 0
    mid_max_sum = 0
    right_subarray = 0
    left_subarray = 0
    # first we need to calculate the midpoint of the input array.
    mid_point = int((len(input_arr))/ 2)
    #print("The midpoint is: ", mid_point)
    # verifies that the midpoint is valid
    # then continues if it passes the if statement
    if (mid_point != 0):
        # uses the reversed function in python
        # to check the values against the left half
        for i in reversed(range(mid_point)):
            temp_value += input_arr[i]
            if (temp_value > left_max_value):
                left_max_value = temp_value
                temp_value1 = i
        # had to make sure to reset this value, otherwise it throws the
        # calculation off
        temp_value = 0
        # compare the right half
        for j in range(mid_point, len(input_arr)):
            temp_value += input_arr[j]
            if (temp_value > right_max_value):
                right_max_value = temp_value
                temp_value2 = j + 1 # not entirely sure why there needs to be +1
        # recursive call to be able to go through
        # both halves of the array
        mid_max_sum = right_max_value + left_max_value
        left_subarray = divide_conquer(input_arr[:mid_point])
        right_subarray = divide_conquer(input_arr[mid_point:])

        # determines the largest sub array
        # once found, it prints it
        if (mid_max_sum >= left_max_value) and (mid_max_sum >= right_max_value):
            print (mid_max_sum, input_arr[temp_value1:temp_value2])
        if (left_max_value >= right_max_value) and (left_max_value > mid_max_sum):
            print (left_max_value, left_subarray)
        if (right_max_value >= left_max_value) and (right_max_value > mid_max_sum):
            print (right_max_value, right_subarray)

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
                        divide_conquer(input_arr)
                        #return(1)
                    elif function_call == '4':
                        kadanes(input_arr)
                    else:
                        print("Usage: project1.py -n <Algorithim #> -i <inputfile>")
        else:
            print("Usage: project1.py -n <Algorithim #> -i <inputfile>")

main(sys.argv[1:])
