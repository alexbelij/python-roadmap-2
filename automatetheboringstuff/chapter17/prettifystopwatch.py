#!/usr/bin/python
# Linux shebang change it according to your OS
# stopwatch.py - A simple stopwatch program.
import time

# Display the program's instructions.

print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        prettyLapTime = str(lapTime).rjust(10)
        prettyLapNum = str(lapNum).rjust(3)
        prettyTotalTime = str(totalTime).rjust(5)
        print('Lap #%s: %s (%s)' % (prettyLapNum, prettyTotalTime, prettyLapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')