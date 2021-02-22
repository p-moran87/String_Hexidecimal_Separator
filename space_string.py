import csv
import numpy as np

with open("C:\\Users\\pmoran\\Desktop\\P1-PROJECTS\\HKMC\\HKMC_NX4_Long_artf673925\\SAW2\\SAW2_HKMC_NX4_LONG_64x64_config_img5_2kb.txt") as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		s = row[0]
	s = " ".join(s[i:i+2] for i in range(0, len(s), 2))
	print(s)

file = open("C:\\Users\\pmoran\\Desktop\\P1-PROJECTS\\HKMC\\HKMC_NX4_Long_artf673925\\SAW2\\testfile.txt","w") 
file.write(s) 
file.close() 