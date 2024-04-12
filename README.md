# pasos a seguir

## instalar python

## clonar el repositorio

```
git clone https://github.com/EmonterrosoF/capturador-fotogramas

```

- abrir vscode
- abrir la carpeta clonada
- abrir la terminal de vscode
  - ejecutar `pip install virtualenv`
  - luego `python -m venv env`
  - despues `env/Scripts/activate`
  - luego `pip install -r .\requirements.txt`
  - y por ultimo ejecutar `python main.py`
- luego ejecutado el programa
  - leer los comentarios en el codigo
  - para salir del programa se presiona la tecla escape
  - para tomar una foto se presiona la tecla de espacio

### Extras

- si no es tan buena la camara de la pc usar el programa iriun WebCam link https://iriun.com/ que utiliza la camara del celular como webcam

```python
captura = cv2.VideoCapture(0)
```

- en esta parte del codigo el parametro 0 es para la camara integrada de la pc, si se quiere usar otra camara se le coloca 1, o si no tiene camara la pc y se usa una webcam el parametro tiene que ser 0

# POR LO MENOS TOMAR UNAS 250 A 300 FOTOS POR OBJETO EN DIFERENTES ANGULOS O POSICIONES
