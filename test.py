import time 
def func(d):
    if d == 5:
        return True
    print(d)
    time.sleep(0.1)
    func(d+1)
    
func(1)