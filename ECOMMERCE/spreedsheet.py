import openpyxl as xl

wk = xl.load_workbook("transactions.xlsx")

sheet = wk["Sheet1"]
cell= sheet.cell(1,1)

print(cell.value)