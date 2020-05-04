import time

import matplotlib.pyplot as plt
import random as r
import cv2

# create xLabels
xLabels = [str(x) for x in range(0, 14)]
print(xLabels)

# create list to sore outcomes
outcomes = [0]*14
print(outcomes)

# create video writer
size = (960, 720)
sizePlt =(size[0]/100, size[1]/100)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(r'C:\Users\kevin\Desktop\output\output.avi', fourcc, 120, size, True)

frames = 3000

for i in range(frames):
    outcome = r.randint(1, 6) + r.randint(1, 6)
    outcomes[outcome] += 1

    # convert outcomes list to bar graph
    fig = plt.figure(figsize=sizePlt)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(xLabels, outcomes)
    temp = r'C:\Users\kevin\Desktop\output\temp.png'
    plt.savefig(r'C:\Users\kevin\Desktop\output\temp.png')
    time.sleep(0.01)

    # write to file
    img = cv2.cvtColor(cv2.imread(temp), cv2.COLOR_RGB2BGR)
    out.write(img)

    # clean up
    plt.close(fig)
    print(str(outcomes) + str(i) + " of " + str(frames))

out.release()
