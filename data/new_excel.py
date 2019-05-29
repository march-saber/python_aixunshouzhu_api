from openpyxl import workbook

wb = workbook.Workbook()
wb.create_sheet("sheet1")
wb.save("wifi.xlsx")
wb.close()