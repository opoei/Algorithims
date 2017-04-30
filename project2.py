
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
    
        
    return(recursion(coinList, amount))


coin_array =[1,2,3,4]

print (ChangeSlow(coin_array, 11))
