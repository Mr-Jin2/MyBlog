#coding=utf8
'''1.多线程会造成竞争资源错误地被修改'''
import threading
#共享一个计数器
class SharedCounter:
    def __init__(self,initial_value=10):
        self.__p=5

        self._value = initial_value
        self._value_lock =threading.Lock()

    def incr(self,delta=1):
        with self._value_lock:  #这句去掉将value将会出现错乱
            self._value=self._value+delta

    def decr(self,delta=1):
        with self._value_lock:
            self._value=self._value-delta

def change_it(s):
    for i in range(10000):
        s.incr()
        print 'I am %s,num now is %d '%(threading.current_thread().name,s._value)
def chang_it2(s):
    for i in range(10000):
        s.decr()
        print 'I am %s,num now is %d ' % (threading.current_thread().name, s._value)

if __name__ == '__main__':
    s=SharedCounter()
    # t1=threading.Thread(target=change_it,args=(s,),name='thread1')
    # t2=threading.Thread(target=chang_it2,args=(s,),name='thread2')
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # print s._value



