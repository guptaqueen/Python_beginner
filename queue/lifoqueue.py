import queue

lq = queue.LifoQueue()
lq.put("Devops")
lq.put("Helm")
lq.put("Reacts")
lq.put("Angular")

print(lq.queue)

while not lq.empty():
    print(lq.get())
print(lq.qsize())