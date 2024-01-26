# Second largest element in the array
from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

def findSecondLargest(sequenceOfNumbers):
    lar= sec = float('-inf')
    for num in sequenceOfNumbers:
        if(num> lar):
            sec=lar
            lar=num
        elif (num > sec and num != lar):
            sec= num
    if (sec == float('-inf')):
        return -1
    
    return sec
    pass
