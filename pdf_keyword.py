#!/usr/bin/python
import tabula
import pandas as pd
#import itertools
y=tabula.read_pdf('path of pdf', pages='all', mutliple_tables=True)

list_bni = y.values.tolist()
#print(list_bni)

for i in list_bni:
	#print(i)
	if 'keyword to search' in i:
		print(i)
		cleanedList = [x for x in i if str(x) != 'nan']
		print(cleanedList)
		index = cleanedList.index('keyword to search')
		z=index+1		
		print(cleanedList[z])		
		
		







