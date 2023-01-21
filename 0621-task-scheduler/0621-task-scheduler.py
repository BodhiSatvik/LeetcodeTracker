class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Use a max heap. Use the task that is most frequent
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)
        
        queue = deque()
        cycle = 0
        
        while heap or queue:
            cycle += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:         # make sure count != 0
                    queue.append([cnt, cycle + n])
            if queue and queue[0][1] == cycle:
                heapq.heappush(heap, queue.popleft()[0])
        return cycle
        