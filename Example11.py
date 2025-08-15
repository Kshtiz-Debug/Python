import openpyxl
import sys
N=int(sys.argv[1])
wb=openpyxl.Workbook()
sheet=wb.active
row=1
sheet.title("Multplication Table")


for i in range(1,N+1):
    for j in range(1,11):
        result=f"{i}*{j}={i*j}"
        sheet.cell(row,column=1,value=result)
        row=row+1

wb.save("Multiplication.xslx")
print(f"Multiplication table from 1*1 to {N}*10 has been saved to Multiplication.xslx")


