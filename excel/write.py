import openpyxl

wb = openpyxl.Workbook()

wb.get_sheet_names()
# ['Sheet']

sheet = wb.get_active_sheet()
sheet.title = 'Spam Bacon Eggs Sheet'

wb.get_sheet_names()
# ['Spam Bacon Eggs Sheet']


# write/save changes
wb.save("example2.xlsx")
