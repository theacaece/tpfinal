import imutils
#OpenCV module
import cv2
#Modulo para leer directorios y rutas de archivos
import os
#OpenCV trabaja con arreglos de numpy
import numpy
#Obtener el nombre de la persona que estamos capturando
import sys
nombre = "Juancito"

#Directorio donde se encuentra la carpeta con el nombre de la persona
dir_faces = 'train'
path = os.path.join(dir_faces, nombre)

def guardarImagen(image):
    #Si no hay una carpeta con el nombre ingresado entonces se crea
    if not os.path.isdir(path):
        os.mkdir(path)
    array = numpy.frombuffer(image, dtype='uint8')
    capture = cv2.imdecode(array, -1)
    pin = sorted([int(n[:n.find('.')]) for n in os.listdir(path)
                  if n[0] != '.'] + [0])[-1] + 1

    # Metemos la foto en el directorio
    cv2.imwrite('%s/%s.png' % (path, pin), capture)
