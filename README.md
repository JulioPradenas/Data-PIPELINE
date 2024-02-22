Este pipeline está diseñado para manejar diversas tareas de preprocesamiento en cualquier conjunto de datos dado. Veamos cómo contribuye cada paso del pipeline al proceso de preprocesamiento en general:

El pipeline comienza identificando las características numéricas y categóricas en el conjunto de datos.

A continuación, el pipeline aborda cualquier valor faltante presente en las características numéricas. Rellena estos valores faltantes con el valor medio de cada característica numérica respectiva (puedes modificar este paso según tu forma deseada de completar los valores faltantes de una característica numérica). Se asegura de que los datos faltantes no obstaculicen los análisis y cálculos posteriores.

Luego, el pipeline identifica y maneja los valores atípicos dentro de las características numéricas utilizando el método del Rango Intercuartílico (IQR). El cálculo de los cuartiles y el IQR determina los límites superior e inferior para los valores atípicos. Cualquier valor fuera de estos límites se reemplaza con el valor medio de la respectiva característica numérica. Este paso ayuda a prevenir la influencia de valores extremos en los análisis y la construcción de modelos posteriores.

Después de manejar los valores faltantes y los valores atípicos, el pipeline normaliza las características numéricas. Este proceso garantiza que todas las características numéricas contribuyan igualmente a los análisis posteriores, evitando sesgos causados por magnitudes variables.

El pipeline procede a manejar los valores faltantes en las características categóricas. Rellena estos valores faltantes con el valor de moda, que representa la categoría más frecuente.





