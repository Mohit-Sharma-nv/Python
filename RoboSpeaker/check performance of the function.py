from time import time

def performance(fn):
    def wrapper(*args,**kwargs):
        t1 = time()
        result = fn(*args,**kwargs)
        t2 = time()
        print(f"Its took {t2-t1} sec")
        return result
    return wrapper()

@performance
def long_time():
    for i in range(100000):
        i*5

long_time