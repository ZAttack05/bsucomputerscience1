import random

f=open("integers.txt",'w')
count = 0
while count < 500:
    for i in range(random.randint(2, 20)):
        f.write(str(random.randint(1,1000))+' ')
        count += 1
        if count >= 500:
            break
    f.write('\n')
f.close()
        
print(count)

