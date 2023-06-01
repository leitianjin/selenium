#  读取xsheet
import openpyxl


wds=openpyxl.load_workbook("xsheet.xlsx")

sheets=wds["5月份"]

rows=sheets.rows

print(rows)
for i in rows:

    for j in i:

          print(j.max_culum)
    
