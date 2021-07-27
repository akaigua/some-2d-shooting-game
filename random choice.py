#random choice 
#hw = {'reading': 1, 'grammar': 2}
import random
print('Please type your two choices below')

c1 = input('choice 1 = ')
c2 = input('choice 2 = ')
hwp = []

for i in range(1000):
    hwc = random.randint(0,2)
    hwp.append(hwc)
    i += 1
    
if sum(hwp)/ 1000 >= 1:
    print(c1)
else:
    print(c2)