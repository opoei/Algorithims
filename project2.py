def changedp(coins, amount, minCoins, coinsUsed):
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

amount = 29
coins = [1,3,7,12]
coinsUsed = [0]*(amount+1)
coinCount = [0]*(amount+1)
usedNum = [0]*(len(coins))
coinList = []

print("Algorithm changedp")
minCoins = changedp(coins,amount,coinCount,coinsUsed)
listcoins(coinsUsed,amount,usedNum, coins)
print(coins)
print(usedNum)
print(minCoins)
#print(coinList)
