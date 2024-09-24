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

ex = pd.DataFrame([3, 4, 5, 7, 9])

#print(dataSet["Date"] )
# print(ex.mean())
print("Mean dealy return OSEBX: ", dataSet["OSEBX"].mean())
print("Mean dealy return EQUINOR: ", dataSet["EQUINOR"].mean())


# summarizing all daily returns into array of total annual return: annual return
# when "some variable" equals new year, start new element in array which is summerized as the next 252 days
# return 2001: 137 trading days
# returns the mean annual return using .mean() functio



