import matplotlib.pyplot as plt
from math import pi, sqrt
import xlsxwriter
from math import asin
import csv as csv


###########################################################################################################################

#Constantes et variables 

seconds_in_a_year = 86400*365 

#Correction de lechelle de temps en heure

echelle = 3600
n_iter = 8840        #seconds_in_a_year / echelle


G = 6.674e-11 * echelle**2                       # Constante gravitationnelle
#m_terre = 5.974e24                  # masse de la terre
m_soleil = 1.989e30                 # masse du soleil

   #86400 #10 #31536000
position_x_terre_initial = 149600000000.0  # position en x (m) (distance entre le soleil et la terre)
position_y_terre_initial = 0.0             # position en y (m)
vitesse_x_initial = 0.0
vitesse_terre = ((2*pi*position_x_terre_initial)/(seconds_in_a_year)) * echelle
vitesse_y_initial = 1*vitesse_terre
dt = 1                                  #pas de temps (1 seconde)
#k = (4*(pi**2))/(G * m_soleil)

x = [position_x_terre_initial]
y = [position_y_terre_initial]
vx = [vitesse_x_initial]
vy = [vitesse_y_initial]
acceleration_initial_x = -1*(x[0] * G * m_soleil)/((x[0]**2 + y[0]**2)**(3/2))
acceleration_initial_y = -1*(y[0] * G * m_soleil)/((x[0]**2 + y[0]**2)**(3/2))
ax = [acceleration_initial_x]
ay = [acceleration_initial_y]
#r = [position_x_terre_initial]

###########################################################################################################################

#Simulation de lorbite et creation dun file

with open('orbite.csv','w') as csv_file:
    
    fieldnames = ['Temps', 'Position x', 'Position y']
    
    csv_writer = csv.writer(csv_file, delimiter='\t' )
    
    for i in range(1,(n_iter)+1):
    
        x.append(x[i-1] + vx[i-1] * dt)
        y.append(y[i-1] + vy[i-1] * dt)
        vx.append(vx[i-1] + ax[i-1] * dt)
        vy.append(vy[i-1] + ay[i-1] * dt)
        ax.append(-1*(x[i] * G * m_soleil)/((x[i]**2 + y[i]**2)**(3/2)))
        ay.append(-1*(y[i] * G * m_soleil)/((x[i]**2 + y[i]**2)**(3/2)))
      
        csv_writer.writerow([i, x[i-1], y[i-1]])



###########################################################################################################################

#Calcul de la periode

# for i in range (1, seconds_in_a_year+1):
#     if y[i] < 0:
#         if y[i+1] >= 0:
#             print(i+1)




###########################################################################################################################
    
#Calcul du demi-axe

# def demi_axe_value(list):

#     max_value = max(list)
#     min_value = min(list)
#     demi_axe = (max_value - min_value) / 2
#     return f"max value : {max_value} min value: {min_value} , demi_axe = {demi_axe}"

# print(demi_axe_value(x))
# print(demi_axe_value(y))




###########################################################################################################################

#Representation graphique 

plt.rcParams["figure.figsize"] = [9,9]
plt.plot(x, y, linestyle='dotted', color='b')
plt.plot(0, 0, 'bo')  # position du soleil

plt.xlabel('Position en x')
plt.ylabel('Position en y')
plt.title('Position de la Terre')
plt.grid(True)
plt.show()


# plt.plot(y, linestyle='dotted', color='b')


###########################################################################################################################

#Extraction des donees dans un document excel 

#workbook = xlsxwriter.Workbook('Positions de la terre en x et y.xlsx')
#worksheet = workbook.add_worksheet()
#workbook.use_zip64()

#row = 0
#row2 = 0
#columx = 0
#columy = 1

#for i in x:
    #worksheet.write(row, columx, i)
    #row += 1
    #if row % 1048576 == 0:
        #columx += 2
        #row -= 1048576
#for j in y:
    #worksheet.write(row2, columy, j)
    #row2 += 1
    #if row2 % 1048576 == 0:
        #columy += 2
        #row2 -= 1048576

#workbook.close()

###########################################################################################################################
    
#Calcul de laire balaye

aire_balaye_1 = asin(y[86400]/position_x_terre_initial) * (position_x_terre_initial**2)/2

print(aire_balaye_1)






###########################################################################################################################