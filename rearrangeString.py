class Solution(object):

    # O(n) time complexity. Linear space complexity.
    # Create a min heap of (-freq,char) for each char in str. We use -freq so that the char
    # with the largest frequency will be at the top of the heap.
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        heap = [(-freq, char) for char, freq in collections.Counter(str).items()]
        heapq.heapify(heap)

        # We keep output as a list instead of a string because string construction is costly
        # and we only want to join the individuals chars at the end.
        output = []

        while len(output) < len(str):
            # If heap is empty, return ""
            if not heap: 
                return ""

            # Getting the (negative) frequency and char of the most frequent char in the heap.
            freq, char = heapq.heappop(heap)
            # Create an empty stack
            stack = []
            # Add char to output list.
            output.append(char)
            # We want to find the next k letters. We know that we can't have any repeats 
            # within these k values, so we keep popping from our heap.  
            for j in range(k - 1):
                # If we used up all our chars, we are finished.
                if len(output) == len(str): 
                    return "".join(output)
                # If the heap is empty, we have no more values to use without repeating. 
                # Thus we return ""
                if not heap: 
                    return ""
                # Get our next freq,char pair
                fre, nex = heapq.heappop(heap)
                # Append it to the output.
                output.append(nex)
                # If the (negative) frequency of the next char is less than -1, we keep it
                # and increment its freqency. We push it to the stack.
                if fre < -1: 
                    stack.append((fre+1, nex))

            # We are done with the next k chars, and we add the chars with frequency < -1 back
            # to our heap.
            while stack:
                heapq.heappush(heap, stack.pop())

            # Add the first letter back to the heap.
            heapq.heappush(heap, (freq+1, char))
        
        return "".join(output)
