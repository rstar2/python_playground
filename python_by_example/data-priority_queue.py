# Implementing a Priority Queue


import heapq


class Item:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name


class PrirityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, priority: int, item: Item):
        # heap always is will "smallest" item in front
        # the real item stored in the heap will be a tuple - for easier comparings,
        # e.g wrap the real item, so that:
        # 1. use '-priority' so the bigger the priority the closer to the head in the heap is the heap_item
        # 2. use '++self._index' so that heap_items with the same priority could be easily compared
        #    otherwise a heap_item (1, Item("111")) cannot be compared to another (1, Item("222"))
        #    and the heap cannot decide hopw to sort them
        #    but (1, 10, Item("111")) can be compared to (1, 20, Item("222")) - later put items will be behind
        self._index += 1
        heap_item = (-priority, self._index, item)
        heapq.heappush(self._queue, heap_item)

    def pop(self) -> Item:
        #  check if the queue/heap is not empty
        if len(self._queue) == 0:
            return None

        # get the head heap item
        heap_item_head = heapq.heappop(self._queue)

        # return the real wrapped item - e.g. the last-item in the tupple/iterable
        return heap_item_head[-1]


queue = PrirityQueue()

queue.push(1, Item("Rumen"))
queue.push(1, Item("Neshev"))
queue.push(5, Item("Now"))
queue.push(4, Item("Before1"))
queue.push(4, Item("Before2"))

while True:
    item = queue.pop()
    if item is None:
        break
    print(item)
