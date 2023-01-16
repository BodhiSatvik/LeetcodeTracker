class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # turn list into maxHeap
        # for i in range(len(stones)):
        #     stones[i] *= -1
        # heapq.heapify(stones)

        # while len(stones) > 1:
        #     y = heapq.heappop(stones)
        #     x = heapq.heappop(stones)
        #     if x != y:
        #         heapq.heappush(stones, y-x)
        
        # return -heapq.heappop(stones) if stones else 0
        heap = []
        heapq.heapify(heap)
        for i in stones:
            heapq.heappush(heap, -1*i)
        # print(heap[0])
        
        # heapq._heapify_max(stones)
        while len(heap) > 1:
            y = heapq.heappop(heap)    # get y value, it is destroyed regardless of conditions
            x = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, y-x)
        return -heap[0] if heap else 0


        
