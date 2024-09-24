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
import openpyxl
from openpyxl import Workbook, load_workbook

dataSet = pd.read_excel("Assignment_1_data.xlsx")

#
#   a) 
#

mean_daily_return_OSEBX=dataSet["OSEBX"].mean()
mean_daily_return_EQUINOR=dataSet["EQUINOR"].mean()

print("Mean dealy return OSEBX: ", mean_daily_return_OSEBX)
print("Mean dealy return EQUINOR: ", mean_daily_return_EQUINOR)

# summarizing all daily returns into array of total annual return: annual return
# when "some variable" equals new year, start new element in array which is summerized as the next 252 days
# return 2001: 137 trading days
# returns the mean annual return using .mean() function

# grupperer år
dataSet["year"] = dataSet["Date"].dt.year
print(dataSet.groupby("year")["OSEBX"].mean())

#
#   b)
#


#lager en i vektor som er N-dimensjonal og kun består av 1ere
i=np.ones(len(dataSet.columns))
print(i)







