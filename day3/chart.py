#openpyxl:
#import openpyxl #below line is to import only needed one
from openpyxl.chart import BarChart,Reference
import openpyxl.workbook

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(10):
    sheet.append([i])

values = Reference(sheet, min_col=1, min_row=1,max_col=1,max_row=10)
chart = BarChart()
chart.add_data(values)
chart.title= "BAR-CHART"

chart.x_axis.title= "X_AXIS"
chart.y_axis.title= "Y_AXIS"

sheet.add_chart(chart, "E5")

wb.save("barchart.xlsx")
print("Bar chart created...open barchart.xlsx")