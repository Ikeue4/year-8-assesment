import time
start = -50
t = 0
while t != int(start*10):
    b1 = 2
    b2 = 2*int(start)+2
    b3 = 5
    b4 = 2*int(start)-2
    m11 = b1 + b2
    m12 = b2 + b3
    m13 = b3 + b4
    m21 = m11 + m12
    m22 = m12 + m13
    t = m21 + m22
    if t == int(start*11):
        print("succses")
        print("----------\n" + str(t) +"\n" + str(start) + "\n----------\n")
        break
    print("----------\n" + str(t) +"\n" + str(start) + "\n----------\n")
    time.sleep(0.0001)
    start += 1