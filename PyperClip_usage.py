import csv
outfile=open("Fruits.csv","w",newline="")
writerobj=csv.writer(outfile,delimiter='.')
writerobj.writerow((1,2,3))
writerobj.writerow([1,2,34,4,5,6])