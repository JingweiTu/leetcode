class Solution(object):

    # Naive solution O(n) time. Constant space.
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            current_value = numbers[i]
            for j in range(i+1,len(numbers)):
                if current_value + numbers[j] == target:
                    return [i+1, j+1]
                if current_value + numbers[j] > target:
                    break

    # O(n) solution.  Linear space complexity.
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers_set = set(numbers)
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in numbers_set:
                concatenated_numbers = numbers[i+1:len(numbers)]
                complement_index = concatenated_numbers.index(diff)
                ans = [i, complement_index + i + 1]
                return [x +1 for x in ans]