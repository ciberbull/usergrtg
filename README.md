# Usuarios Grupo Telegram
Con este sencillo script podremos obtener un fichero users.html con el listado de los usuarios del grupo de Telegram solicitado, el historico de las fotos de perfil asi como de los telefonos en caso de estar visibles.
Instalación y configuración:
  Creamos un directorio nuevo en nuestro equipo y accedemos a el:
    mkdir grupotg
    cd grupotg
  Clonamos el repositorio para descargarel fichero .py
  Instalamos la dependencia de la libreria necesaria:
   pip install telethon
  Accedemos a https://my.telegram.org/auth?to=apps para cubrir los datos necesarios para la obtecion de los datos de la api de Telegram del perfil que usaremos para la extracción de datos.
  Editamos el fichero .py descargado cambiando los valores de los campos:
   API_ID
   API_HASH
   NUMERO_TELEFONO
   NOMBRE_GRUPO

Para el uso del programa simplemente ejecutamos python fichero.py
