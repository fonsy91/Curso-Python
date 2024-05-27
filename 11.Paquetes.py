'''
Paquetes:  directorios donde se almacenaran modulos relacionados entre 
si. Sirven para reutilizar y organizar los modulos.

Para crear un paquete solo hay que crear una carpeta con un archivo
__inti__.py

En nuestro caso hemos creado una carpeta PaquetesCalculos y dentro hemos
creado un archivo __init__.py y otro calculosGenerales.py

Dentro de la carpeta PaquetesCalculos puedes agregar carpetas separadas 
cada una haciendo operaciones diferentes, toda la carpeta es para calculos
pero lo puedes dividir en carpetas de diferentes calculos como, operacionesBasicas,
operacionesEstadistica, operacionesLogica, operacionesAvanzadas etc...

'''
from PaqueteCalculos.calculosGenerales import *

potencia(2,3)

'''
Tambien existen los paquetes distribuibles para que diferentes personas 
puedan reutilizar nuestro codigo o incluso nosotros mismos reutilizar nuestro 
codigo en otros proyectos. Estos paquetes se pueden enviar a diferntes personas 
via correo electronico o subiendolo a una plataforma, nos va a permitir empaquetar 
nuestros propios modulos y scripts y enviarlos donde queramos los pasos son los siguientes:

1º Crear el paquete 
2º Instalar el paquete

Con esto este donde este el archivo/paquete instalado vamos a poder usarlo desde 
cualquier sitio

Creamos un archivo setup.py en la raiz del proyecto Este archivo va a describir la configuracion
del paquete distribuible lo hacemos asi:

-------------------------------------
from setuptools import setup

setup {
    name = "calculosGenerales",
    version = "1.0",
    description = "Calculos matematicos",
    author = "Alfonso",
    packages = ["PaquetesCalculos","PaquetesCalculos.calculosGenerales"]
}
--------------------------------------

Despues nos dirigimos hasta ese archivo con terminal y ejecutamos:

python3 setup.py sdist

Esto nos genera dos carpetas: paqueteCalculos.egg-info y dist pues 
dentro de dist nos encontramos con un zip o tar.gz PaqueteCalculos

Con este paquete realizamos la instalacion: 
Nos dirigimos hacia este zip o tar.gz en terminal y ejecutamos:

pip3 install <archivo.zip o tar.gz >

Para desinstalarlo:

pip3 uninstall paqueteCalculos

Gracias a la instalacion podremos usar ese paquete desde cualquier proyecto
o parte del ordenador.

'''
