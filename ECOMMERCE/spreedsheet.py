import openpyxl as xl

wk = xl.load_workbook("transactions.xlsx")

sheet = wk["Sheet1"]
cell= sheet["a1"]

print(cell.value)

for  row in range(2,sheet.max_row + 1):#looping through each row in the sheet 1
  
    cell = sheet.cell(row  ,3)
  
    corected_price = float(cell.value)*0.9
    corrected_price_cell = sheet.cell(row,4)
    corrected_price_cell.value=corected_price


wk.save("transactions2.xlsx")