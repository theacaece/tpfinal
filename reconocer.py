import cv2
import train, detect, config, imutils, argparse

# Funcion que reconoce imagen pasada por parametro
def RecognizeFace(image, faceCascade, eyeCascade, faceSize, threshold):
    found_faces = []
    recognizer = train.trainRecognizer("train", faceSize, showFaces=True)
    gray, faces = detect.detectFaces(image, faceCascade, eyeCascade, returnGray=1)
    for ((x, y, w, h), eyedim)  in faces:
        label, confidence = recognizer.predict(cv2.resize(detect.levelFace(gray, ((x, y, w, h), eyedim)), faceSize))
        if confidence < threshold:
            found_faces.append((label, confidence, (x, y, w, h)))

    return found_faces

def reconocer(imagePath):

    # Lee argumentos
    faceCascade = cv2.CascadeClassifier('cascades/face.xml')
    eyeCascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
    faceSize = config.DEFAULT_FACE_SIZE
    threshold = 500
    
    recognizer = train.trainRecognizer('train', faceSize, showFaces=True)

    # Crea la ventana con el nombre 'Reconocimiento Facial!'
    # cv2.namedWindow("Reconocimiento Facial!", 1)
    # Pasa como parametro la imagen recibida como argumento
    capture = cv2.imread(imagePath)

    if imagePath is None:
      print("La ruta de la imagen se ingreso de forma incorrecta")
      return "La ruta de la imagen se ingreso de forma incorrecta"
    if capture is None:
      print("La ruta de la imagen indicada no existe")
      return "La ruta de la imagen indicada no existe"
    label =""

    img = imutils.resize(capture, height=500)
    for (label, confidence, (x, y, w, h)) in RecognizeFace(img, faceCascade, eyeCascade, faceSize, threshold):
      print(label)

    result = "Rostro No Encontrado"
    if label != "":
     result = "Rostro Reconocido: %s" % (recognizer.getLabelInfo(label))
    else:
      result = "Rostro No Encontrado"
    
    return result


if __name__ == '__main__':

    # Lee argumentos
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True,
    help = "Ruta de la imagen para reconocer")
    args = vars(ap.parse_args())

    faceCascade = cv2.CascadeClassifier('cascades/face.xml')
    eyeCascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
    faceSize = config.DEFAULT_FACE_SIZE
    threshold = 500
    
    recognizer = train.trainRecognizer('train', faceSize, showFaces=True)

    # Crea la ventana con el nombre 'Reconocimiento Facial!'
    # cv2.namedWindow("Reconocimiento Facial!", 1)
    # Pasa como parametro la imagen recibida como argumento
    capture = cv2.imread(args["image"])

    # Inicia bucle
    while True:
        if args["image"] is None:
            print("La ruta de la imagen se ingreso de forma incorrecta")
        if capture is None:
            print("La ruta de la imagen indicada no existe")
            break
        label =""
        img = imutils.resize(capture, height=500)
        
	# Busca el nombre de la persona del rostro que esta en la imagen
        for (label, confidence, (x, y, w, h)) in RecognizeFace(img, faceCascade, eyeCascade, faceSize, threshold):
            font = cv2.FONT_HERSHEY_DUPLEX
            # Coloca rectangulo en el rostro encontrado y reconocido
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # Coloca el nombre de la persona reconocida
            cv2.putText(img, "{}".format(recognizer.getLabelInfo(label)), (x, y-5), font, 1, (0,255,0), 1, cv2.LINE_AA)
            
        # Indica el nombre de la persona reconocida en la imagen pasada por parametro
        titulo_ventana = "Rostro No Encontrado"
        if label != "":
            titulo_ventana = "Rostro Reconocido: %s" % (recognizer.getLabelInfo(label))
	print(titulo_ventana)
	# Crea la ventana con el nombre 'Reconocimiento Facial' y la imagen a reconocer
	cv2.imshow("Reconocimiento Facial", img)
	# Comprueba si se ha pulsado la tecla 'espacio' para salir del bucle
	ch = cv2.waitKey(0)
	# 32 es el simbolo del espacio
	if ch == 32:
            break
        
    # Si se ha salido del bucle, destruye la ventana y finaliza el programa
    cv2.destroyAllWindows()
