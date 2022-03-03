import time
import matplotlib.pyplot as pn
a = 0
b = 1
y = 0
gr = [0]
print("Enter the number to which will be calculate Fibonacci number graph:")
amount = input()
amount = int(amount)

while b < amount:
    b = a + b
    y = b
    gr.append(y)
    a = a + b
    y = a
    gr.append(y)
    time.sleep(0.1)
pn.plot(gr)
pn.show() 


 


 