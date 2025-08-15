import random         # So that we can use randint function present in that module
import time         # To know the amt of time prg takes to run
code="0000"           # Coz the lock code would be 4 digit
start=time.time()        # To mark the start time
while True:
    x=f"{random.randint(0,9999):04d}"  #:04d will make that integer look like a string with 4 charachters
    # for example 5 with :04d --------> will look like 0005.
    # Then we just need to check if it is correct or not, by
    if(x==code):
        print(x)
        break

end=time.time()      # To mark the end point
print("The time taken by program is   ",end-start)