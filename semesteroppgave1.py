# Semesteroppgave 1 i VMA
# Bruker git (github.com) til fildeling

# LAGRE ENDRINGRER TIL GITHUB: 
# Åpne terminal i VSCode -> Git bash
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

excel_file = "Assignment_1_data.xlsx"
dataSet = pd.read_excel(excel_file)

print(dataSet)

