import time
import subprocess
"""
start=time.time()
g=100
for i in range(1000):
    if i==g:
        print(i)

end=time.time()
interval=end-start
print("The time taken is about",interval)

"""




class Record:
    start=time.time()

    subprocess.run("Prime.py")
    
    end=time.time()
    interval=end-start
    return interval
    

