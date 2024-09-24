import numpy as np
import pandas as pd
import openpyxl
from openpyxl import Workbook, load_workbook

# testtest

excel_file = "Assignment_1_data.xlsx"
dataSet = pd.read_excel(excel_file)

print(dataSet)

