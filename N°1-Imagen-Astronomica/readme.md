# ¿Qué es un archivo FITS?
Un archivo FITS (Flexible Image Transport System) es el formato estándar que usan los observatorios y telescopios para guardar datos astronómicos.
Un FITS puede contener:
- Imágenes astronómicas (2D, 3D, etc.).
- Tablas de datos (como catálogos estelares).
- Metadatos: información sobre el telescopio, fecha de observación, coordenadas, filtros, etc.

Cada píxel tiene un valor numérico (no color RGB), y cada detalle técnico queda guardado en la cabecera del archivo.

#### El archivo de ejemplo ` hlsp_heritage_hst_wfc3-ir_m16_f160w_v1_drz.fits ` es una imagen real del Hubble, del programa Hubble Legacy Project (HERITAGE)

--- 
Con las funciones de ` data.shape, np.min(data), np.max(data) y np.mean(data) `, en la terminal se verá: 


```
Tamaño: (4200, 4000)
Mínimo: -4244.612
Máximo: 16348.674
Media: 2.7514105
```

El archivo FITS contiene valores de intensidad (flujo luminoso) captados por el detector del telescopio, píxel por píxel.

Cada valor float32 es la cantidad de luz recibida (en unidades relativas o calibradas, depende del filtro).

En este caso el filtro F160W corresponde al infrarrojo cercano (1.6 μm), o sea: estamos viendo calor, no luz visible.

Los valores negativos se deben a la resta de fondo: el procesamiento original del Hubble le quita la señal promedio del cielo, por eso el fondo puede caer por debajo de cero.

El valor máximo (unos 16 000) marca las zonas más brillantes: las puntas de los pilares y las estrellas.
