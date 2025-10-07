import numpy as np
from PSRDist import Distances as D
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
from astropy import units as u
from scipy.optimize import curve_fit

def gauss(x, a, b, c):
    return a * np.exp(-(x-b)**2 / (2*c**2))

names = np.array(["PSR J0657-4657", "PSR J1259-8148", "PSR J1346-2610", "PSR J1356+0230", "PSR J1712-1920", "PSR J1823+1208", "PSR J1831-6503", "PSR J2029-4239"])
RA = np.array(["06:57:22.0520894", "12:59:31.5874", "13:46:03.032", "13:56:37.128", "17:12:01.5200", "18:23:18.3156", "18:31:04.4", "20:29:35.1955523"])
DC = np.array(["-46:57:52.6269995", "-81:48:51.3778", "-26:10:18.60", "+02:30:30.50", "-19:20:24.1000", "12:08:38.728", "-65:03:13.7", "-42:39:35.112504"])
DM = np.array([126.059, 44.314, 20.167, 17.794, 49.41, 40.68, 25.715, 10.17])

uhf_msps = SkyCoord(ra = RA, dec = DC, unit = (u.hourangle, u.degree), frame = 'icrs').galactic

L = uhf_msps.l.value
B = uhf_msps.b.value

print(L, B)

dpdf, d = D.dist_pdf(RA, DM, L, B)

plt.figure(figsize = [10,10])

for i in range(len(L)):
    popt, pcov = curve_fit(gauss, d[i], dpdf[i], bounds = (0.,100.), p0 = np.array([np.max(dpdf[i]), np.mean(d[i]), np.mean(d[i])]))
    plt.subplot(3,3,i+1)
    plt.plot(d[i], dpdf[i])
    plt.plot(d[i], gauss(d[i], popt[0], popt[1], popt[2]))
    plt.title(names[i])
    plt.xlabel("D [kpc]")
    plt.ylabel("PDF")
    print names[i], round(popt[1],3), round(popt[2],3)

plt.tight_layout()
plt.savefig("UHFMSPs_distPDF_YMW16.pdf")
plt.show()
