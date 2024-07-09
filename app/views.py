from flask import jsonify, request # type: ignore
from app.models import User
from datetime import date

def index():
    return jsonify(
        {
            'mensaje': 'Hola, las API de CYS están on line con Flask'
        }
    )

def services():
    return jsonify(
        {
            "services": [
                {
                    'url': '/api/users/login/',
                    'method': 'POST',
                    'body': 
                        {
                            'Id': 'Id del usuario',
                            'Password': 'Password del usuario'
                        } 
                },
                {
                    'url': '/api/users/list/',
                    'method': 'GET',
                    'body': 
                        {
                            'fromId': 'Id de usuario desde', 
                            'qty': 'Cantidad de usuarios'
                        } 
                },
                {
                    'url': '/api/users/fetch/<str:Id>',
                    'method': 'GET'
                },
                {
                    'url': '/api/users/create/',
                    'method': 'POST',
                    'body': 
                        {
                            'Id': 'Id',
                            'NomApe': 'NomApe',
                            'Direccion': 'Direccion',
                            'Contacto': 'Contacto'
                        }
                },
                {
                    'url': '/api/users/update/<str:Id>',
                    'method': 'PUT',
                    'body': 
                        {
                            'Id': 'Id',
                            'NomApe': 'NomApe',
                            'Direccion': 'Direccion',
                            'Contacto': 'Contacto'
                        }
                },
                {
                    'url': '/api/users/delete/<str:Id>',
                    'method': 'DELETE'
                }
            ]  
        }
    )

def get_user(user_id):
    user = User.get_user_by_id(user_id)
    if not user:
        return jsonify({'msg': 'User not found', 'sts': 1}), 404
    return jsonify(user.serialize())

def get_users():
    users = User.get_users()
    return jsonify([user.serialize() for user in users])

def create_user():
    data = request.json

    user = User.get_user_by_id(data['Id'])
    if user:
        return jsonify({'msg': 'Ya existe User: ' + user.toStringArray(), 'sts': 1})
   
    new_user = User(
        Id=data['Id'],
        NomApe=data['NomApe'],
        Direccion=data['Direccion'],
        Contacto=data['Contacto']
    )
    new_user.add()
    return jsonify({'msg': 'Alta exitosa de User: ' + new_user.toStringArray(), 'sts': 0}), 201

def update_user(user_id):
    user = User.get_user_by_id(user_id)
    if not user:
        return jsonify({'msg': 'No existe User con clave: ' + user_id, 'sts': 1}), 404
   
    data = request.json
    upd_user = User(
        Id=data['Id'],
        NomApe=data['NomApe'],
        Direccion=data['Direccion'],
        Contacto=data['Contacto']
    )
    upd_user.upd()
    return jsonify({'msg': 'Modificación exitosa de User: ' + upd_user.toStringArray(), 'sts': 0})

def delete_user(user_id):
    user = User.get_user_by_id(user_id)
    if not user:
        return jsonify({'msg': 'No existe User con clave: ' + user_id, 'sts': 1}), 404

    user.delete()
    return jsonify({'msg': 'Baja exitosa de User: ' + user.toStringArray(), 'sts': 0})


"""

def get_pending_tasks():
    tasks = Task.get_all_pending()
    return jsonify([task.serialize() for task in tasks])

def get_completed_tasks():
    tasks = Task.get_all_completed()
    return jsonify([task.serialize() for task in tasks])

def get_archived_tasks():
    tasks = Task.get_all_archived()
    return jsonify([task.serialize() for task in tasks])

def get_task(task_id):
    task = Task.get_by_id(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    return jsonify(task.serialize())

def create_task():
    data = request.json
    new_task = Task(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        fecha_creacion=date.today().strftime('%Y-%m-%d'),
        completada=False,
        activa=True
    )
    new_task.save()
    return jsonify({'message': 'Task created successfully'}), 201

def update_task(task_id):
    task = Task.get_by_id(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
   
    data = request.json
    task.nombre = data['nombre']
    task.descripcion = data['descripcion']
    task.save()
    return jsonify({'message': 'Task updated successfully'})

def archive_task(task_id):
    task = Task.get_by_id(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
   
    task.delete()
    return jsonify({'message': 'Movie deleted successfully'})

def __complete_task(task_id, status):
    task = Task.get_by_id(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404

    task.completada = status
    task.activa = True
    task.save()
    return jsonify({'message': 'Task updated successfully'})

def set_complete_task(task_id):
    return __complete_task(task_id, True)

def reset_complete_task(task_id):
    return __complete_task(task_id, False)
"""
