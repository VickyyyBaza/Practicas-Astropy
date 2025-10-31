import numpy as np # Numpy sirve para arrreglos de numeros, osea matrices o vectores
import matplotlib.pyplot as plt # Matplotlib sirve para graficar
from astropy.io import fits #fits sirve para leer, analizar y escribir archivos FITS, que es el formato que usan los telescopios.

# Abrimos el archivo FITS que descargaste
archivo = "hlsp_heritage_hst_wfc3-ir_m16_f160w_v1_drz.fits"
hdul = fits.open(archivo)

# Mostramos qué contiene
hdul.info()
