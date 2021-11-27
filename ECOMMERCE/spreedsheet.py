import openpyxl as xl

wk = xl.load_workbook("transactions.xlsx")

sheet = wk["Sheet1"]
cell= sheet["a1"]

for  row in range(1,sheet.max_row + 1):#looping through each row in the sheet 1
    print(row)
    cell = sheet.cell(row  ,3)
    print(cell)