import numpy as np
import pyne2001
from PSRDist import Distances as D
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
from astropy import units as u
from scipy.optimize import curve_fit

def gauss(x, a, b, c):
    return a * np.exp(-(x-b)**2 / (2*c**2))

names = np.array(["J0636+5128"])
RA = np.array(["06:36:04.847464"])
DC = np.array(["+51:28:59.96547"])
DM = np.array([11.10857])

uhf_msps = SkyCoord(ra = RA, dec = DC, unit = (u.hourangle, u.degree), frame = 'icrs').galactic

L = uhf_msps.l.value
B = uhf_msps.b.value

print(L, B)

dpdf, d = D.dist_pdf(RA, DM, L, B)
dbf = D.dist_bf(RA, DM, L, B)

#plt.figure(figsize = [10,10])

for i in range(len(L)):
    dne2001 = pyne2001.get_dist(L[i], B[i], DM[i])
    popt, pcov = curve_fit(gauss, d[i], dpdf[i], bounds = (0.,100.), p0 = np.array([np.max(dpdf[i]), np.mean(d[i]), np.mean(d[i])]))
    #plt.subplot(3,3,i+1)
    plt.axvline(dne2001[0], color = "tab:green")
    plt.axvline(dbf[i], color = "tab:blue")
    plt.plot(d[i], dpdf[i], color = "tab:blue")
    plt.plot(d[i], gauss(d[i], popt[0], popt[1], popt[2]), color = "tab:orange")
    plt.title(names[i])
    plt.xlabel("D [kpc]")
    plt.ylabel("PDF")
    print names[i], round(dne2001[0],4), round(dbf[i],4), round(popt[1],4), round(popt[2],4), round(abs(dne2001[0]-dbf[i])/popt[2],4)

plt.tight_layout()
plt.savefig("RPPcatMSPs_distPDF_YMW16.pdf")
plt.show()
