from parser import *
import matplotlib.pyplot as plt

tracks = parse('*/*/*.wav')

sortof0 = map(lambda x: x[:, 0], tracks)
for i in range(len(sortof0)):
    sortof0[i].sort()

sortof1 = map(lambda x: x[:, 1], tracks)
for i in range(len(sortof1)):
    sortof1[i].sort()

for i in range(5):
    arr = sortof0[i]
    plt.plot(range(len(arr)), arr)
    plt.draw()
    plt.plot(range(len(arr)), sortof0[i+5])
    plt.draw()
    plt.show()

'''
for i in range(len(sortof1)):
    arr = sortof1[i]
    plt.plot(range(len(arr)), arr)
    plt.draw()
    if i == 4 or i == 9:
        plt.show()
'''
