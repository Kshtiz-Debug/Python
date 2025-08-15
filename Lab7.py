import openpyxl
import sys

# Get the value of N from command-line arguments
N = int(sys.argv[1])

# Create a new workbook and select the active sheet
wb = openpyxl.Workbook()
sheet = wb.active

# Set the title of the sheet
sheet.title = "Multiplication Table"

# Initialize the row counter
row = 1

try:
    # Populate the sheet with the multiplication table
    for i in range(1, N + 1):
        for j in range(1, 11):
            result = f"{i} * {j} = {i * j}"
            sheet.cell(row=row, column=1, value=result)
            row += 1

    # Save the workbook to a file
    wb.save("Multiplication.xlsx")
    print(f"Multiplication table from 1*1 to {N}*10 has been saved to Multiplication.xlsx")
except Exception as e:
    print(f"An error occurred: {e}")
