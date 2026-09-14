import openpyxl
# file="Data.xlsx"
# workbook = openpyxl.load_workbook(file)
# sheet=workbook['Data'] # or we can use (sheet= workbook.active) if only one workbook available.
#
# #It will insert same data in each cell
# for r in range(1,6):
#     for c in range(1,4):
#         sheet.cell(r,c).value="Welcome"
#
# workbook.save(file)
file="Data.xlsx"
workbook = openpyxl.load_workbook(file)
sheet=workbook['Data2']

sheet.cell(1,1).value=123
sheet.cell(1,2).value="Smith"
sheet.cell(1,3).value="Engineer"

sheet.cell(2,1).value=567
sheet.cell(2,2).value="John"
sheet.cell(2,3).value="Lead"

sheet.cell(3,1).value=547
sheet.cell(3,2).value="Sam"
sheet.cell(3,3).value="Developer"

workbook.save(file) # save the file after entering data
