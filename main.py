import cv2

def coleccionar_datos():
    #aqui es donde se indica que camara se va a usar 0 es la camara de la pc, 1 puede ser una webCam, y asi sucesivamente
    #depende cuantas camaras le tengan a su pc
    captura = cv2.VideoCapture(0)
    captura.set(3, 1280)
    captura.set(4, 720)

    contador = 0

    while True:
        _, frame = captura.read()
        tecla = cv2.waitKey(5)

        #con la tecla de espacio se toman las fotos
        if tecla == 32:
            #aqui es donde se guardan las imagenes en el disco, crear carpeta images,
            #luego renombrar donde dice apartado por el nombre del objeto que les tocó
            #para que se guarden las imagenes con el nombre del objeto
            cv2.imwrite(f"images/apartado_{contador}.jpg", frame)

            contador = contador + 1

        cv2.imshow("Captura", frame)

        #con la tecla de escape se sale del programa
        if tecla == 27:
            break

    captura.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    coleccionar_datos()