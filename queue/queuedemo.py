import queue

q = queue.Queue()
q.put('Python')
q.put('Djano')
q.put('DRF')
q.put('DOcker for Django')

print(q.queue)
# q.queue.clear()

print(q.qsize())

while not q.empty():
    print(q.get())

print(q.qsize())