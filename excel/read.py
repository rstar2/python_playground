import openpyxl

# open Excel document (Worksbook objet)
wb = openpyxl.load_workbook('example.xlsx')

#  get the Excel Sheets (Worksheet object)
print(wb.get_sheet_names())

# get the default Sheet
activeSheet = wb.get_active_sheet()

# get a Sheet
sheet = wb.get_sheet_by_name('Sheet1')



