import os
from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

# Sustituye estos valores con los de tu cuenta de telegram.
api_id = '*******'
api_hash = '*******'
numero_telefono = '*******'

# Solicitar al usuario que introduzca el nombre del grupo
nombre_grupo = input("Introduzca nombre del grupo: ")

# Crear y conectar el cliente
client = TelegramClient('session_name', api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(numero_telefono)
    client.sign_in(numero_telefono, input('Enter the code: '))

# Crear directorio para las imágenes de perfil
if not os.path.exists('profile_pics'):
    os.makedirs('profile_pics')

# Función para obtener la lista de miembros del grupo y descargar sus imágenes de perfil
async def get_group_members_and_download_pics(nombre_grupo):
    dialogs = await client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=200,
        hash=0
    ))
    
    for dialog in dialogs.chats:
        if dialog.title == nombre_grupo:
            group = dialog
            break
    else:
        print(f"Group '{nombre_grupo}' not found")
        return

    users_data = []
    
    async for user in client.iter_participants(group):
        username = user.username if user.username else 'N/A'
        phone = user.phone if user.phone else 'N/A'
        user_data = {
            'id': user.id,
            'username': username,
            'phone': phone,
            'photos': []
        }

        async for photo in client.iter_profile_photos(user):
            photo_path = f'profile_pics/{user.id}_{photo.id}.jpg'
            await client.download_media(photo, photo_path)
            user_data['photos'].append(photo_path)
        
        users_data.append(user_data)
    
    generate_html(users_data)

# Función para generar el archivo HTML
def generate_html(users_data):
    with open('users.html', 'w') as f:
        f.write('<html><body>')
        f.write('<h1>Usuarios del Grupo</h1>')
        f.write('<table border="1">')
        f.write('<tr><th>ID</th><th>Username</th><th>Phone</th><th>Profile Photos</th></tr>')
        
        for user in users_data:
            f.write('<tr>')
            f.write(f'<td>{user["id"]}</td>')
            f.write(f'<td>{user["username"]}</td>')
            f.write(f'<td>{user["phone"]}</td>')
            f.write('<td>')
            for photo in user['photos']:
                f.write(f'<img src="{photo}" width="100" />')
            f.write('</td>')
            f.write('</tr>')
        
        f.write('</table>')
        f.write('</body></html>')

with client:
    client.loop.run_until_complete(get_group_members_and_download_pics(nombre_grupo))

# Cerrar la sesión del cliente
client.disconnect()

