'''
Loading data and training model
'''
import pickle
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from utils import *

'''Path to each folder and files'''
calibra = 'dataset/meas_14_7/data/DATA_MACHINE_7-14/MEAS_1'  # path to
calibra_pairs = 'dataset/meas_14_7/calibration/calibration_15_7'  # path to 
pairs_5200 = 'dataset/meas_7_7/procIMGs'
pairs_1100 = 'dataset/meas_7_7/procIMGs_2'

print('Loading data...')