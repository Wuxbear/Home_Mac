from multiprocessing import Process, Queue
import time

def reader(queue):
    while True:
        msg = queue.get()
        if (msg == 'DONE'):
            break

def writer(count, queue):
    for i1 in range(0, count):
        queue.put(i1)
    queue.put('DONE')


if __name__ == '__main__':
    for count in [10**4, 10**5, 10**6]:
        queue = Queue()
        reader_p = Process(target = reader, args=((queue),))
        reader_p.daemon = True
        reader_p.start()

        _start = time.time()
        writer(count,queue)
        reader_p.join()
        print("send %s numbers to queue() took %s secs" % (count, (time.time() - _start)))
