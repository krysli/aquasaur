import numpy as np
import math
from mpmath import *

TOTALWATER = mpf(5775000000000000000000)
CUPSDRANK = mpf(10)
# Brontosaurus lived 156-145 mya, a total of 11 my
TOTALYEARS = mpf(11000000)

# By Damuth's Law we can estimate there were
# 0.01 to 1 Brontosaurus every square km
# Assume Brontosaurus lived across the Western United States
# This is an area spanning 4.8 million square km
ALL_TOTAL_DINOS = np.array([48000, 480000, 4800000])

# Assume Brontosaurus drank 262 liters a day
CUPS_PERDAY_PERDINO = mpf(1107)

mp.dps = 100
for TOTAL_DINOS in ALL_TOTAL_DINOS:
    print("TOTAL_DINOS", TOTAL_DINOS)
    TOTAL_CUPS_PERDAY = mpf(CUPS_PERDAY_PERDINO*TOTAL_DINOS)
    TOTAL_CUPS_PERYEAR = mpf(TOTAL_CUPS_PERDAY*365)
    TOTAL_CUPS_DRANK = mpf(TOTAL_CUPS_PERYEAR*TOTALYEARS)
    numerator = mpf(fsub(TOTALWATER, CUPSDRANK))
    nprint(numerator, n=100)
    denominator = mpf(TOTALWATER)
    nprint(denominator, n=100)
    p = mpf(fdiv(numerator, denominator))
    nprint(p, n=100)
    nprint(mp.fsub(1, mp.power(p, TOTAL_CUPS_DRANK)), n=100)




