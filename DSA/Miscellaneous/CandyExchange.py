'''Alice and Bob have a different total number of candies. You are given two integer arrays aliceSizes and bobSizes where aliceSizes[i] is the number of candies of the ith box of candy that Alice has and bobSizes[j] is the number of candies of the jth box of candy that Bob has.
Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box they have.
Return an integer array answer where answer[0] is the number of candies in the box that Alice must exchange, and answer[1] is the number of candies in the box that Bob must exchange. If there are multiple answers, you may return any one of them. It is guaranteed that at least one answer exists.

Example 1:
Input: aliceSizes = [1,1], bobSizes = [2,2]
Output: [1,2]

Constraints:
        • 1 <= aliceSizes.length, bobSizes.length <= 104
        • 1 <= aliceSizes[i], bobSizes[j] <= 105
        • Alice and Bob have a different total number of candies.
        • There will be at least one valid answer for the given input.'''
class CandyExchange:
    def __init__(self, aliceSizes, bobSizes):
        self.aliceSizes = aliceSizes
        self.bobSizes = bobSizes

    def find_fair_exchange(self):
        sum_alice = sum(self.aliceSizes)
        sum_bob = sum(self.bobSizes)
        delta = (sum_alice - sum_bob) // 2  

        bob_set = set(self.bobSizes)  

        for x in self.aliceSizes:
            y = x - delta
            if y in bob_set:
                return [x, y]

        return []  

alice = [1, 1]
bob = [2, 2]
exchange = CandyExchange(alice, bob)
print("Output:", exchange.find_fair_exchange()) 