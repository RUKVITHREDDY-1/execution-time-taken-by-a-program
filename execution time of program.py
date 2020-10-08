import time
def timing(f):
    def wrap(*args,**kwargs):
        time1=time.time()
        ret=f(*args,**kwargs)
        time2= time.time()
        ms=(time2-time1)*1000.0
        print('Time tookZ{:.3f}ms'.format(ms))
        return ret
    return wrap
@timing
def test():
    x=0
    for i in range(100000):
        x+=i
        return x
output =test()
print(output)