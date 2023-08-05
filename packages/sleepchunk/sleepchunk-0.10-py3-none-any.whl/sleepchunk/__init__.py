import sys
from math import floor
from random import randrange
from time import sleep as sleep_


def sleep_with_statusbar(maxrange):
    try:
        if isinstance(maxrange, float):
            sleeplittle = floor(maxrange)
            sleep(maxrange - sleeplittle)
            maxrange = int(sleeplittle)
        if maxrange > 0:
            for i in range(maxrange + 1):
                try:
                    sys.stdout.write("\r")
                    sys.stdout.write(f"[{'=' * i}] {i} / {maxrange}")
                    sys.stdout.flush()
                    maxrangex = 20
                    if isinstance(maxrangex, float):
                        sleeplittle = floor(maxrangex)
                        sleep_((maxrangex - sleeplittle) / 20)
                        maxrangex = int(sleeplittle)

                    if maxrange > 0:
                        for _ in range(maxrangex):
                            try:
                                sleep_(0.05)
                            except:

                                return
                except:
                    return
        sys.stdout.write("\r")
        sys.stdout.write(f"                   ")
        sys.stdout.flush()
    except:
        return


def sleep(secs):
    try:
        if secs == 0:
            return
        maxrange = 20 * secs
        if isinstance(maxrange, float):
            sleeplittle = floor(maxrange)
            sleep_((maxrange - sleeplittle) / 20)
            maxrange = int(sleeplittle)

        if maxrange > 0:
            for _ in range(maxrange):
                try:
                    sleep_(0.05)
                except:
                    return
    except:
        return


def sleep_random(start=2, end=3, with_statusbar=False):
    schlafzeit = randrange(int(start * 1000), (end * 1000)) / 1000
    if not with_statusbar:
        sleep(schlafzeit)
    else:
        sleep_with_statusbar(schlafzeit)
