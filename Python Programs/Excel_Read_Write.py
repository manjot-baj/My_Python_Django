import openpyxl
wb = openpyxl.load_workbook('example.xlsx')

# for i in wb:
    # print(i)
s1=wb.get_sheet_by_name("Sheet1")
print(s1["A1"].value)