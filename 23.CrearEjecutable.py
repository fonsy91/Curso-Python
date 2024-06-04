'''
Para crear un ejecutable hay que seguir los siguientes pasos:

1º: Instalar pyinstaller: pip install pyinstaller
2º: pyinstaller <Nombre_archivo.py>
3º: Tras el paso dos creara una serie de archivos y carpetas en el directorio donde 
esta el script entonces no debemos fijar en la carpeta dist, la abrimos y nos encontramos 
con muchas carpetas y archivos entre ellos nos encontramos el .exe

Que ocurre que aparece la aplicacion con el terminal por detras y los suyo es que solo se
ejecute la aplicacion en si asique agregamos un modificador a pyinstaller <Nombre_archivo.py>
de la siguiente manera:

pyinstaller --windowed <Nombre_archivo.py>

De todas las maneras aun asi necesita de todos los archivos para compilarse, lo bueno 
es que todo se compilara en un unico archivo .exe y que se puede ejecutar en cualquier ordenador 
ni aun no teniendo python para ello se agrega un modificador mas a la instruccion:

pyinstaller --windowed --onefile <Nombre_archivo.py>

Si quieres agregar un icono especifico al ejecutable lo primero que tienes que hacer es
acompañar a tu script con el icono en cuestion antes de haer ningun comando de creacion del
ejecutable en formato .ico y agregando un modificador mas: 

pyinstaller --windowed --onefile --icon=/logo.ico <Nombre_archivo.py>

'''