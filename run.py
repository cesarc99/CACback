from flask import Flask # type: ignore
from flask import jsonify # type: ignore
from flask_cors import CORS # type: ignore
from app.views import *
from app.database import *
from app.models import *


app = Flask(__name__)


#Rutas para test y modelos de servicios
app.route('/', methods=['GET'])(index)
app.route('/services/', methods=['GET'])(services)

# Rutas para usuarios
app.route('/api/users/fetch/<string:user_id>', methods=['GET'])(get_user)
app.route('/api/users/list/', methods=['GET'])(get_users)

app.route('/api/users/create/', methods=['POST'])(create_user)
app.route('/api/users/update/<string:user_id>', methods=['PUT'])(update_user)
app.route('/api/users/delete/<string:user_id>', methods=['DELETE'])(delete_user)

"""
# Rutas para usuarios
app.route('/api/users/login/', methods=['POST'])(login)

"""

# Rutas para libros
"""
app.route('/api/books/available/', methods=['GET'])(get_available_books)
app.route('/api/books/borrowed/', methods=['GET'])(get_borrowed_books)
app.route('/api/books/anyState/', methods=['GET'])(get_anyState_books)

app.route('/api/books/fetch/<int:book_id>', methods=['GET'])(get_book)
app.route('/api/books/create/', methods=['POST'])(create_book)

app.route('/api/books/update/<int:book_id>', methods=['PUT'])(update_book)
app.route('/api/books/lend/<int:book_id>', methods=['PUT'])(lend_book)
app.route('/api/books/return/<int:book_id>', methods=['PUT'])(return_book)
app.route('/api/books/delete/<int:book_id>', methods=['DELETE'])(delete_book)

"""

# Database
# test_connection()
create_table_users()
load_users()
create_table_userAccess()
load_access()
# create_table_books()
init_app(app)
CORS(app)


if __name__ == '__main__':
    app.run(debug=True)