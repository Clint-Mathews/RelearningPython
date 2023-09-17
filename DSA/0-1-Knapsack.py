class KnapSack:
    weights = []
    values = []
    knapSackWeight = 0
    length = 0

    def __init__(self, weights: list, values: list, knapSackWeight: int):
        self.weights = weights
        self.values = values
        self.knapSackWeight = knapSackWeight
        self.length = len(weights)

    def findMaxProfit(self, weights: list, values: list, knapSackWeight: int, length: int) -> int:
        if length == 0 or knapSackWeight == 0:
            return 0
        if weights[length - 1] <= knapSackWeight:
            return max(values[length - 1] + self.findMaxProfit(weights, values, knapSackWeight - weights[length-1], length-1),
                       self.findMaxProfit(weights, values, knapSackWeight, length-1))
        else:
            # el if weights[length -1] > knapSackWeight. i.e. else case!
            return self.findMaxProfit(weights, values, knapSackWeight, length-1)


if __name__ == '__main__':
    weights = [10, 20, 30]
    values = [60, 100, 120]
    knapSackWeight = 50
    knapSack = KnapSack(weights, values, knapSackWeight)
    profit = knapSack.findMaxProfit(knapSack.weights, knapSack.values, knapSack.knapSackWeight, knapSack.length)
    print("Profit: {}".format(profit))
