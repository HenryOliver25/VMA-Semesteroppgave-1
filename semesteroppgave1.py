# Semesteroppgave 1 i VMA
# Bruker git (github.com) til fildeling

# LAGRE ENDRINGRER TIL GITHUB: 
# Åpne terminal i VSCode -> Git bash
# Lagre endringer (CTRL+S)
# $ git add . (legger til alle filer)
# $ git commit -m "din besked/hva du har endret" (legger til beskjed)
# $ git push -u origin main (Pusher endringer til github)

# LAST NED ENDRINGER FRA GITHUB:
# Åpne terminal i VSCode -> Git bash
# $ git pull (henter evt. endringer)

import numpy as np
import pandas as pd
import datetime as dt
import openpyxl
from pandas_datareader import data as pdr
from openpyxl import Workbook, load_workbook

dataSet = pd.read_excel("Assignment_1_data.xlsx")

#
#   a) 
#

mean_daily_return_OSEBX=dataSet["OSEBX"].mean()
mean_daily_return_EQUINOR=dataSet["EQUINOR"].mean()

print("Mean daily return OSEBX: ", mean_daily_return_OSEBX)
print("Mean daily return EQUINOR: ", mean_daily_return_EQUINOR)

# summarizing all daily returns into array of total annual return: annual return
# returns the mean annual return using .mean() function

# groups by year
dataSet["year"] = dataSet["Date"].dt.year
# sum of each year
sum_annual_return_OSEBX = dataSet.groupby("year")["OSEBX"].sum()
sum_annual_return_EQUINOR = dataSet.groupby("year")["EQUINOR"].sum()
# sum of each year divided by no. of years gives mean annual return over the time frame
print(sum_annual_return_OSEBX, sum_annual_return_EQUINOR)
print(sum_annual_return_OSEBX.mean(), sum_annual_return_EQUINOR.mean())

#
#   b)
#

#lager en i vektor som er N-dimensjonal og kun består av 1ere
i=np.ones(len(dataSet.columns))
print(i)







