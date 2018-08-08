from gevent import monkey; monkey.patch_socket()
import gevent

def f(n):
    for i in range(n):
        gevent.sleep(0)
        print gevent.getcurrent(), i

g1 = gevent.spawn(f, 50000)
g2 = gevent.spawn(f, 50000)
g3 = gevent.spawn(f, 50000)
g1.join()
g2.join()
g3.join()