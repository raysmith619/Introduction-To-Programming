#
#  xlrd_test.py
# Simple python reading of Excel file
#
import xlrd
data_file = 'sample.xlsx'
book=xlrd.open_workbook(data_file)

# Check number of sheets in the excel
print("Number of sheets:", book.nsheets)

# Print the sheet names
print("Sheet names:", book.sheet_names())

# Get the sheet based on index
sheet=book.sheet_by_index(0)


# Get number of rows and number of columns in an excel sheet
num_rows=sheet.nrows
num_col=sheet.ncols
for row in range(0, num_rows):
    for col in range(0, num_col):
        # Read the contents of a cell
        cell = sheet.cell(row,col) #where row=row number and col=column number

        print(cell.value, end=' ') #to print the cell contents
    print("")
# Get excel sheet by name

sheets = book.sheet_names()
cur_sheet = book.sheet_by_name(sheets[0])

"""
Expected Output
Number of sheets: 1
Sheet names: ['Sheet1']
heading1 heading2 heading3 
1.0 2.0 3.0 
4.0 5.0 6.0 
7.0 8.0 9.0 
10.0 11.0 12.0 
"""
