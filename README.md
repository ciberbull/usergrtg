# Usuarios Grupo Telegram
Con este sencillo script podremos obtener un fichero users.html con el listado de los usuarios del grupo de Telegram solicitado, el historico de las fotos de perfil asi como de los telefonos en caso de estar visibles.
Instalación y configuración.<br>

  Creamos un directorio nuevo en nuestro equipo y accedemos a el:<br>
    mkdir grupotg<br>
    cd grupotg<br>
    
  Clonamos el repositorio para descargar el fichero usuariostg.py<br>
  git clone https://github.com/ciberbull/usergrtg.git
  Instalamos la dependencia de la libreria necesaria:<br>
   pip install telethon<br>
   
  Accedemos a https://my.telegram.org/auth?to=apps para cubrir los datos necesarios para la obtecion de los datos de la api de Telegram del perfil que usaremos para la extracción de datos, editamos el fichero usuariostg.py descargado cambiando los valores de los campos:<br>
  
   API_ID<br>
   API_HASH<br>
   NUMERO_TELEFONO<br>
   NOMBRE_GRUPO<br>

Para el uso del programa simplemente ejecutamos python usuariostg.py
