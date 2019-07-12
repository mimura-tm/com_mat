import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import os
import time

def file_read(filename):
	df_read = pd.read_csv(filename,header=None, skiprows=5)
	sw1 = df_read[7] - df_read[8]
	sw2 = df_read[9] - df_read[10]
	sw3 = df_read[11] - df_read[12]
	sw4 = df_read[13] - df_read[14]
	sw5 = df_read[15] - df_read[16]

	return [sw1, sw2, sw3, sw4, sw5]

def threshold(df_threshold,thr_num):
	for i in range(len(df_threshold)):
		if df_threshold.tolist()[i] >= thr_num:
			thres = i
			break
	return thres

def capture(filename):
	a = 0
	while os.path.exists(filename) == False:
		time.sleep(1)
		a = a+1
		print(a)


if __name__ == "__main__":
	for ii in range(6):
		capture("test.csv")
		time.sleep(5)
		df = file_read("test.csv")
		os.rename("test_{}.csv".format(ii))
		par_list = []
		for i in range(5):
			par_list.append(threshold(df[i],1))
		with open("/Users/tm/Desktop/lab/reserch/mec/july/703/param.txt",mode='w') as f:
			for iii in range(5):
				f.write('{}\n'.format(str(par_list[iii])))
	capture("test.csv")
	print('Succes!')
