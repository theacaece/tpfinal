# THEA - Reconocimiento
THEA - Reconocimiento es un software escrito en Python, haciendo uso de la librería Opencv, para el reconocimiento facial.

Utilizar el software es muy sencillo, solo debes seguir estos pasos:

1- Preparar los datos de entrenamiento:
Como todo programa de inteligencia artificial, este necesita datos de los cuales aprender. Estos datos serán las imágenes, en la carpeta "train" se deben encontrar las carpetas con las imágenes de los rostros que utilizaremos para que el software identifique nuevas imágenes desconocidas por el programa.
Lo ideal es que en esta carpeta ingreses todas las que deseas, y recuerda, entre más datos, mucho mejor.

2- Entrenar al programa:
Luego de que dispongamos de los datos, en momentos de entrenar al programa. Esto lo haremos ejecutando el script "train.py".

python train.py

Luego de esto, el programa empezara a ejecutar el entrenamiento. Al finalizar se creara un archivo "train_result.out" el cual contendrá los resultados del entrenamiento, esto nos servirá para una nueva predicción, de esta manera no se tendrá que entrenar al programa cada vez que intente realizar un nuevo reconocimiento facial.

3- Reconocimiento Facial:
Una vez que el programa este entrenado, podemos realizar nuestro primer proceso de reconocimiento facial. Todo lo que tenemos que hacer es ejecutar el siguiente comando en tu terminal en el directorio del programa:

python reconocer.py --image test/barack.jpg

En el comando pueden ver "test/barack.jpg". Aquí debe ir la ruta de la imagen en la que desea reconocer rostros. En el repositorio se encuentran alguna imágenes de prueba.

El resultado:

![""](https://4.bp.blogspot.com/-PTb7_3pbjGw/WzwegSqs5_I/AAAAAAAABRw/xPqsWdX9lHIjDqH90gWBhZ-j14FiQTRVACK4BGAYYCw/s640/Captura1.PNG)

Podemos hacer las todas las pruebas que queramos:

![""](https://1.bp.blogspot.com/-Wz2g0x123Ts/WzwfMGI6wII/AAAAAAAABR8/HDOUznjgkHUK6tQNNvOdzLyCLlXITAklQCK4BGAYYCw/s400/cap.PNG)

![""](https://4.bp.blogspot.com/-7fKEnWmiLH0/WzwfxSd8gBI/AAAAAAAABSI/6DF9qptm0ls4_RdNwaX9xKuvkGxpig3eACK4BGAYYCw/s640/omds.PNG)

