# random selection by weight application
# get the idea from leetcode chanllege

class random_selection():
    def __init__(self, w: List[int]):
        """
        :type: w List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum
        
    def pickIndex(self):
        """
        :type: get the index of random selection
        """
        target = self.total_sum * random.random()
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low)//2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
    