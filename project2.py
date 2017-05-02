import getopt, sys
from sys import argv

coin_array = [1,3,7,26]
change = 22


def ChangeSlow(coinList, amount):
    
    def recursion(coin_array, amount):

        minCoins = [0 for c in coin_array]
        minCoins[0] = amount
        for coin in coin_array:
            if coin <= amount:
                temp = (recursion(coin_array, amount - coin))
                temp[coin_array.index(coin)] += 1
                if sum(minCoins) > sum(temp):
                    minCoins = temp
                    bestSum = temp
        return (minCoins)
        
    minCoins = recursion(coinList, amount)
    minCoinCount= sum(minCoins)

    f = open(output_filename, 'a')
    f.write("CHANGE SLOW ALGORITHM\n")
    f.writelines([str(coinList), "\n", str(minCoins), "\n", str(minCoinCount), "\n"])
    f.close()
    
def changegreedy(coin_array, change):
    coin_array_length = len(coin_array)
    counter = [0 for x in range(coin_array_length)]
    # subtract 1 to get actual value otherwise
    # it will be out of range
    i = coin_array_length - 1
    # As long as there is a value for change
    # the loop will execute.
    while (change):
        # checks for the largest value coin possible
        # if successful, then subtract the value and
        # increment counter.
        if change >= coin_array[i]:
            change = change - coin_array[i]
            counter[i] += 1
        else:
            i = i - 1
        counterSum = sum(counter)
    # outputs values to file as specified in the instructions
    f = open(output_filename, 'a')
    f.write("GREEDY ALGORITHM\n")
    f.writelines([str(coin_array), "\n", str(counter), "\n", str(counterSum), "\n"])
    f.close()

def changedp(coins, amount):
    coinsUsed = [0]*(amount+1)
    coinCount = [0]*(amount+1)
    usedNum = [0]*(len(coins))
    coinList = []
    def changedp_sub(coins, amount, minCoins, coinsUsed):
        for cents in range (amount+1):
            coinCount = cents
            newCoin = 1
            for j in [c for c in coins if c <= cents]:
                if minCoins[cents-j] + 1 < coinCount:
                    coinCount = minCoins[cents-j]+1
                    newCoin = j
            minCoins[cents] = coinCount
            coinsUsed[cents] = newCoin
        return minCoins[amount]

    def listcoins(coinsUsed, amount, usedNum, coins):
        i = amount
        while i > 0:
            thisCoin = coinsUsed[i]
            coinList.append(thisCoin)
            for j in range (len(usedNum)):
                if thisCoin == coins[j]:
                    usedNum[j]+=1
            i = i - thisCoin
    minCoins = changedp_sub(coins,amount,coinCount,coinsUsed)
    listcoins(coinsUsed,amount,usedNum, coins)
    f = open(output_filename, 'a')
    f.write("CHANGEDP ALGORITHM\n")
    f.writelines([str(coins), "\n", str(usedNum), "\n", str(minCoins), "\n"])
    f.close()


def main(argv):
    opts, args = getopt.getopt(argv,"i:")
    for opt, arg in opts:
        if opt == '-i':
            line_itr = 1
            global output_filename
            output_filename = arg.rsplit('.')[0] + '_change.txt'
            f = open(output_filename, 'w') #create or overwrite file
            f.close()
            with open(arg) as ifile:
                for line in ifile:
                    #could do this with itrtools, but this is a bit more explicit
                    if line_itr % 2 == 1:
                        coin_list = [ int(element) for element in line.split() ] 
                    elif line_itr % 2 == 0:
                        amount = int(line)
                        ChangeSlow(coin_list, amount)
                        changegreedy(coin_list, amount)
                        changedp(coin_list, amount)
                        
                    line_itr += 1
        else:
            print("Usage: project2.py -i <inputfile>")

main(sys.argv[1:])

