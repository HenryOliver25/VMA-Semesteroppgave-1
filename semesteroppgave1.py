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

# using pandas data frame to calculate mean values.
# instead, averages can be found by creating a vector (ex. i), 
# do the transpose of i (i') and multiplying it by the y vector
# and dividing it by the number of daily returns (no. of columns), 
# which will get you the mean daily return

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
print("Mean annual return OSEBX: ", sum_annual_return_OSEBX.mean(), "\nMean annual return EQUINOR: ", sum_annual_return_EQUINOR.mean())


#
#   b)
#
#lager en i vektor som er N-dimensjonal og kun består av 1ere
#i=np.ones(len(dataSet.columns))
#print(i)

daily_return_OSEBX=dataSet["OSEBX"]
daily_return_EQUINOR=dataSet["EQUINOR"]

N_O=len(daily_return_OSEBX) #lenght of vector daily return OSEBX
N_E=len(daily_return_EQUINOR) #lenght of vector daily returns EQUINOR
vector_mean_daily_return_OSEBX=np.full(N_O, mean_daily_return_OSEBX) #vector of mean daily returns, OSEBX
vector_mean_daily_return_EQUINOR=np.full(N_E, mean_daily_return_EQUINOR) #vector of mean daily returns, EQUINOR
print("vector with OSEBX`s mean daily return is:", vector_mean_daily_return_OSEBX)
print("vector with EQUINOR`s mean daily return is:", vector_mean_daily_return_EQUINOR)
print("the lenght of OSEBX`s vector of mean daily return:", len(vector_mean_daily_return_OSEBX))
print("the lenght of Equinor`s vector of mean daily return:", len(vector_mean_daily_return_EQUINOR))


#
#c)
#use the equation from the assignment, where i is a 4404x1 matrix consisting off one, and i^T is its transposed
#y is repesented by daily returns 
#1/N represents 1/4404, because there are 4404 rows  

#make a coloumn vector of ones 
i=np.ones((4404, 1)) #i

#the transposed of the one_vector, the transposed of i. 
i_transposed=np.transpose(i) #i^T

#matrix multiplication of the ones matrix and its transposed, it gived a 4404x4404 matrix, ii^T
iiT=np.dot(i, i_transposed) 

#multiply ii^T with y (daily_return_OSEBX), gives a vector where all the elements is the sum of all components in y. 
iiTy_OSEBX=np.dot(iiT, daily_return_OSEBX) #matrix multiplication of the 4404x4404 ones-matrix times the  daily_return matrix (y)


avarage_OSEBX=(1/N_O)*(iiTy_OSEBX)
#devide the new vector by numbers of rows of y (N=4404), and you get a vector where each element is the avarage of the elemnts in y. 

solution_OSEBX=daily_return_OSEBX-avarage_OSEBX
print("the solution shows us how much the daily return off the OSEBX deviates from the mean daily return:")
print(solution_OSEBX)
#utrykket er en ny vektor som viser avviket fra gjennomsnittet

#does the same for EQUINOR
#creating a vector that summarize all components in the daily return vector for Equinor. 
iiTy_EQUINOR=np.dot(iiT, daily_return_EQUINOR)

#find the the avarage. devide each element by number of rows (4404), and get the means of the elemtents in y. 
avarage_EQUINOR=(1/N_E)*iiTy_EQUINOR

solution_EQUINOR=daily_return_EQUINOR-avarage_EQUINOR

print("the solution shows us how much the daily return of EQUINOR-stock deviates from the mean daily returns")
print(solution_EQUINOR)

#
#d)
#show that M=I-(1/N)ii^T
#create identity matrix, I
I=np.identity(4404)

#creating matrix M
M=I-(1/N_O)*i*i_transposed

#1 show that M is symmetric
#mean that M=M^T
M_transponert=M.transpose


#2
#show M is idempotent
if M.all()==(M*M).all():
    print("ja")
else: 
    print("nein")









