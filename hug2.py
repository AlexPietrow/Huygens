import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#Convert old units to mm
r2mm = 313.946  #Rhennish rod to mm
f2mm = 304.8    #foot to mm
i2mm = 25.4     #inch to mm
p2mm = 26.167   #Rhennish foot to mm

#Table 1
#https://primarysources.brillonline.com/browse/codices-hugeniani/hug-32-ff-030rv;cohu3232011?search=table%20huygens&searchStart=2&searchTotal=7&search-go=&q=table+huygens&sort=true&fq=collection%3A%22codices-hugeniani%22

fo = np.array([1,2,3,4,5,6,7,8,9,10,13,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,110,120,130,140,150,160,170,180,190,200,220,240,260,280,300])*r2mm

fo1 = fo.copy()

do1 = np.array([0.55,0.77,0.95,1.09,1.23,1.34,1.45,1.55,1.64,1.73,1.97,2.12,2.45,2.74,3.09,3.24,3.46,3.67,3.87,4.06,4.24,4.42,4.58,4.74,4.90,5.05,5.20,5.35,5.48,5.74,6.00,6.25,6.48,6.71,6.93,7.14,7.34,7.55,7.75,8.12,8.48,8.83,9.16,9.49,])*p2mm

fe1 = np.array([0.61,0.85,1.05,1.20,1.35,1.47,1.60,1.71,1.80,1.90,2.17,2.33,2.70,3.01,3.30, 3.56,3.81,4.04,4.26,4.47,4.66,4.86,5.04,5.24,5.39,5.56,5.72,5.87,6.03,6.31,6.60,6.88,7.13,7.38,7.62,7.85,8.09,8.31,8.53,8.93,8.33,9.71,10.08,10.44])*p2mm

m1 = np.array([20,28,34,40,44,49,53,56,60,63,72,77,89,100,109,118,126,133,141,148,154,161,166,172,178,183,189,194,199,209,218,227,235,244,252,259,267,274,281,295,308,321,333,345])


#Table 2
# pp497 https://www.biodiversitylibrary.org/item/68458#page/75/mode/1up
fo2 = fo

do2 = np.array([0.55,0.77,0.95,1.09,1.23,1.34,1.45,1.55,1.64,1.73,1.97,2.12,2.45,2.74,3.00,3.24,3.46,3.67,3.87,4.06,4.24,4.42,4.58,4.74,4.90,5.05,5.20,5.35,5.48,5.74,6.00,6.25,6.48,6.71,6.93,7.14,7.34,7.55,7.75,8.12,8.48,8.83,9.16,9.49,])*p2mm

fe2 = do2.copy()

m2 = np.array([22,31,38,45,49,54,58,62,66,69,79,85,98,110,120,130,138,147,155,162,170,177,183,190,196,202,208,214,219,230,240,250,259,268,277,286,294,302,310,325,340,353,366,380])


#table3
# 223 https://www.gutenberg.org/files/54420/54420-h/54420-h.htm
fo3 = np.array([1,2,3,4,5,6,7,8,9,10,15,20,30,40,50,60,70,80,90,100,120])*f2mm

do3 = np.array([0.545,0.76,0.94,1.08,1.21,1.32,1.43,1.53,1.62,1.71,2.10,2.43,3.00,3.43,3.84,4.20,4.55,4.83,5.15,5.40,5.90])*i2mm

fe3 = np.array([0.605,0.84,1.04,1.18,1.33,1.45,1.58,1.69,1.78,1.88,2.30,2.68,3.28,3.76,4.20,4.60,5.00,5.35,5.65,5.95,6.52])*i2mm

m3 = np.array([20,20.5,34.6,40,45,50,53,56.8,60.6,63.8,78,89.5,109,127,142,156,168,179,190,200,220])


#Define linear, quadratic and exponential fit
def lin(x, a,b,c):
    return a * x + b

def quad(x, a,b,c):
    return a * x**2 + c

def expw(x, a,b,c):
    return a * x**b + c

#Plot figure
plt.figure(figsize=(8.27,11.69))

ff =np.arange(3500)/10
popt, pcov = curve_fit(quad, do1/10, fo1/10, p0=[15,0,0])
popt2, pcov = curve_fit(quad, do2/10, fo2/10,  p0=[15,0,0])
print(popt, popt2)

plt.subplot(321)
plt.plot(do1/10,fo1/10,  marker='o', alpha=0.5, color='red', label='M=1.1D')
plt.plot(do2/10,fo2/10,  marker='o', alpha=0.5, color='green', label='M=D')
plt.plot(ff,popt[0]*ff**2, color='red')
plt.plot(ff,popt2[0]*ff**2, color='green')
plt.plot(ff,126.3*ff**2, label='Theoretical', color='black')
plt.xlim(-1,30)
plt.ylim(-500,12000)
plt.ylabel(r'd$_o$ [cm]')
plt.xlabel(r'f$_o$ [cm]')
plt.title('Telescope Focus Vs. Aperture Size')

popt, pcov = curve_fit(quad, fe1/10,fo1/10, p0=[15,0,0])
popt2, pcov = curve_fit(quad, fe2/10,fo2/10, p0=[15,0,0])
print(popt, popt2)

plt.subplot(322)
plt.plot(fe1/10,fo1/10,  marker='o', alpha=0.5, color='red', label='M=1.1D')
plt.plot(fe2/10,fo2/10,  marker='o', alpha=0.5, color='green',label='M=D')
plt.plot(ff,popt[0]*ff**2, color='red')
plt.plot(ff,popt2[0]*ff**2, color='green')
plt.plot(ff,0.15*ff**2, label='Theoretical', color='black')
plt.xlim(-2,30)
plt.ylim(-100,12000)
plt.ylabel(r'f$_o$ [cm]')
plt.xlabel(r'f$_e$ [cm]')
plt.legend()
plt.title('Telescope Focus Vs. Eyepiece Focus')



popt, pcov = curve_fit(quad, m1,fo1/10, p0=[15,0,0])
popt2, pcov = curve_fit(quad, m2,fo2/10, p0=[15,2,0])
print(popt, popt2)

plt.subplot(323)
plt.plot(m1,fo1/10,  marker='o', alpha=0.5, color='red', label='data1')
plt.plot(m2,fo2/10,  marker='o', alpha=0.5, color='green',label='data1')
plt.plot(ff,popt[0]*ff**2, color='red')
plt.plot(ff,popt2[0]*ff**2, color='green')
plt.plot(ff,2.42*ff**2, label='Theoretical', color='black')
plt.ylabel(r'f$_e$ [cm]')
plt.xlabel(r'M [cm]')
plt.title('Magnification Vs. Aperture size')


popt, pcov = curve_fit(lin, do1/10,fe1/10, p0=[15,0,0])
popt2, pcov = curve_fit(lin, do2/10,fe2/10, p0=[15,0,0])
print(popt, popt2)

plt.subplot(324)
plt.plot(do1/10,fe1/10,  marker='o', alpha=0.5, color='red', label='data1')
plt.plot(do2/10,fe2/10,  marker='o', alpha=0.5, color='green',label='data1')
plt.plot(ff,popt[0]*ff, color='red')
plt.plot(ff,popt2[0]*ff, color='green')
plt.plot(ff,29.2*ff, label='Theoretical', color='black')
plt.ylabel(r'f$_e$ [cm]')
plt.xlabel(r'd$_o$ [cm]')
plt.title('Aperture size Vs. Eyepiece Focus')
plt.xlim(-2,30)
plt.ylim(-2,30)


popt, pcov = curve_fit(lin, do1/10,m1, p0=[15,0,0])
popt2, pcov = curve_fit(lin, do2/10,m2, p0=[15,0,0])
print(popt, popt2)

plt.subplot(325)
plt.plot(do1/10,m1,  marker='o', alpha=0.5, color='red', label='data1')
plt.plot(do2/10,m2,  marker='o', alpha=0.5, color='green',label='data1')
plt.plot(ff,popt[0]*ff, color='red')
plt.plot(ff,popt2[0]*ff, color='green')
plt.plot(ff,4.33*ff, label='Theoretical', color='black')
plt.ylabel(r'M [cm]')
plt.xlabel(r'd$_o$ [cm]')
plt.title('Aperture size Vs. Magnification')
plt.xlim(-2,30)
plt.ylim(-2,400)


popt, pcov = curve_fit(lin, fe1/10,m1, p0=[15,0,0])
popt2, pcov = curve_fit(lin, fe2/10,m2, p0=[15,0,0])
print(popt, popt2)

plt.subplot(326)
plt.plot(fe1/10,m1,  marker='o', alpha=0.5, color='red', label='data1')
plt.plot(fe2/10,m2,  marker='o', alpha=0.5, color='green',label='data1')
plt.plot(ff,popt[0]*ff, color='red')
plt.plot(ff,popt2[0]*ff, color='green')
plt.plot(ff,0.15*ff, label='Theoretical', color='black')
plt.ylabel(r'M [cm]')
plt.xlabel(r'f$_e$ [cm]')
plt.title('Eyepiece Focus Vs. Magnification')
plt.xlim(-2,30)
plt.ylim(-2,400)

plt.tight_layout()
plt.show()


