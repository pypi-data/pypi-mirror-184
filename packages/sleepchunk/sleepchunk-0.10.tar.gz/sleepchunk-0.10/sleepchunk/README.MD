# Sleeps in chunks of 0.05 seconds / ctrl+c to exit without throwing an Exception / status bar 

```python
# Tested with:
# Python 3.9.13
# Windows 10

pip install sleepchunk

from sleepchunk import sleep, sleep_with_statusbar, sleep_random
sleep(secs=3)
sleep_with_statusbar(maxrange=10) # [======] 6 / 10
sleep_random(start=2, end=3, with_statusbar=False)
sleep_random(start=2, end=3, with_statusbar=True)
sleep(secs=0)

```



