t0 = time.time()
        mins_ind = [0]
        maxs_ind = []
        for i in range(len(prices)-2):
            if (prices[i] >= prices[i+1] < prices[i+2]) or (prices[i] > prices[i+1] <= prices[i+2]):
                mins_ind.append(i+1)
            elif (prices[i] <= prices[i+1] > prices[i+2]) or (prices[i] < prices[i+1] >= prices[i+2]):
                maxs_ind.append(i+1)
    
        maxs_ind.append(len(prices)-1)
        print(time.time() - t0)
        
        most_profit = 0
        for i in mins_ind:
            for j in maxs_ind:
                if j > i and ((prices[j]-prices[i]) > most_profit):
                    most_profit = prices[j] - prices[i]

        print(time.time()-t0)
        return most_profit

print(Solution().maxProfit([7,1,5,3,6,4]))