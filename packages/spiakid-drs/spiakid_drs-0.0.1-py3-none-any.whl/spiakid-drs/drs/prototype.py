#!/usr/bin/env python
#
import h5py
import sys
import numpy as np
import pandas as pd

def read_hdf(fileName):
    print('reading file '+fileName)
    fh5=h5py.File(fileName,'r')

    
if __name__ == "__main__":
    read_hdf(sys.argv[1])
