import numpy as np # Numpy sirve para arrreglos de numeros, osea matrices o vectores
import matplotlib.pyplot as plt # Matplotlib sirve para graficar
from astropy.io import fits #fits sirve para leer, analizar y escribir archivos FITS, que es el formato que usan los telescopios.

# Está linea sirve para abrir el archivo FITS descargado
fotohubble = "hlsp_heritage_hst_wfc3-ir_m16_f160w_v1_drz.fits"
hdul = fits.open(fotohubble)

# Mostramos qué contiene - se visualiza en consola
hdul.info()

# Acceder a los datos de la imagen
data = hdul[0].data
header = hdul[0].header

print("Tamaño:", data.shape)
print("Mínimo:", np.min(data))
print("Máximo:", np.max(data))
print("Media:", np.mean(data))


vmin, vmax = np.percentile(data, (0.5, 99.4))  # elimina outliers
plt.figure(figsize=(8, 8))
plt.imshow(data, cmap='inferno', origin='lower', vmin=vmin, vmax=vmax)
plt.colorbar(label="Intensidad recortada")
plt.title("Pilares de la Creación (F160W) - Contraste mejorado")
plt.show()
