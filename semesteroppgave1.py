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

#print("Mean daily reutrn", dataSet[0][1],": ", dataSet["OSEBX"].mean())

