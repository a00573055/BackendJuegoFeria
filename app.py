from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)

# helper function
def database_conection():
    conn = sqlite3.connect("feriaDelConocimiento.db")
    conn.row_factory = sqlite3.Row  
    return conn

### Admin
# create
@app.route("/Admin/", methods=["POST"])
def create_admin():
    conn = database_conection()
    data = request.get_json()
    conn.execute("insert into Admin (nombre, contrasena, director) values (?,?,?)",(data["nombre"],data["contrasena"],data["director"]))
    conn.commit()
    conn.close()
    return ("New Admin added to database", 201)
# read all
@app.route("/Admin/", methods=["GET"])
def get_all_admin():
    conn = database_conection()
    admins = conn.execute("select * from Admin").fetchall()
    conn.close()
    return jsonify([dict(row) for row in admins])
# read one
@app.route("/Admin/<int:id>", methods=["GET"])
def get_one_admin(id):
    conn = database_conection()
    admin = conn.execute("select * from Admin where id = ?", (id,)).fetchone()
    conn.close()
    if admin:
        return jsonify(dict(admin))
    else:
        return ("ID not found", 404)
#update
@app.route("/Admin/<int:id>", methods=["PUT"])
def update_admin(id):
    conn = database_conection()
    data = request.get_json()
    conn.execute("update Admin set nombre = ?, contrasena = ?, director = ? where id = ?", (data["nombre"],data["contrasena"],data["director"],id))
    conn.commit()
    conn.close()
    return ("Admin updated", 200)
#delete
@app.route("/Admin/<int:id>", methods=["DELETE"])
def delete_admin(id):
    conn = database_conection()
    conn.execute("delete from Admin where id = ?", (id,))
    conn.commit()
    conn.close()
    return ("Admin deleted", 204)

### Jugador
# create
@app.route("/Jugador/", methods=["POST"])
def create_jugador():
    conn = database_conection()
    data = request.get_json()
    conn.execute("insert into Jugador (numero_lista, grupo, genero, monedas, id_docente) values (?,?,?,?,?)",(data["numero_lista"],data["grupo"],data["genero"],data["monedas"],data["id_docente"]))
    conn.commit()
    conn.close()
    return ("New Jugador added to database", 201)
# read all
@app.route("/Jugador/", methods=["GET"])
def get_all_jugador():
    conn = database_conection()
    jugadores = conn.execute("select * from Jugador").fetchall()
    conn.close()
    return jsonify([dict(row) for row in jugadores])
# read one
@app.route("/Jugador/<int:id>", methods=["GET"])
def get_one_jugador(id):
    conn = database_conection()
    jugador = conn.execute("select * from Jugador where id = ?", (id,)).fetchone()
    conn.close()
    if jugador:
        return jsonify(dict(jugador))
    else:
        return ("ID not found", 404)
#update
@app.route("/Jugador/<int:id>", methods=["PUT"])
def update_jugador(id):
    conn = database_conection()
    data = request.get_json()
    conn.execute("update Jugador set numero_lista = ?, grupo = ?, genero = ?, monedas = ?, id_docente = ? where id = ?", (data["numero_lista"],data["grupo"],data["genero"],data["monedas"],data["id_docente"],id))
    conn.commit()
    conn.close()
    return ("Jugador updated", 200)
#delete
@app.route("/Jugador/<int:id>", methods=["DELETE"])
def delete_jugador(id):
    conn = database_conection()
    conn.execute("delete from Jugador where id = ?", (id,))
    conn.commit()
    conn.close()
    return ("Jugador deleted", 204)

### Preguntas
# create
@app.route("/Preguntas/", methods=["POST"])
def create_pregunta():
    conn = database_conection()
    data = request.get_json()
    conn.execute("insert into Preguntas (info_preguntas, nivel) values (?,?)",(data["info_preguntas"],data["nivel"]))
    conn.commit()
    conn.close()
    return ("New Pregunta added to database", 201)
# read all
@app.route("/Preguntas/", methods=["GET"])
def get_all_pregunta():
    conn = database_conection()
    preguntas = conn.execute("select * from Preguntas").fetchall()
    conn.close()
    return jsonify([dict(row) for row in preguntas])
# read one
@app.route("/Preguntas/<int:id>", methods=["GET"])
def get_one_pregunta(id):
    conn = database_conection()
    pregunta = conn.execute("select * from Preguntas where id = ?", (id,)).fetchone()
    conn.close()
    if pregunta:
        return jsonify(dict(pregunta))
    else:
        return ("ID not found", 404)
#update
@app.route("/Preguntas/<int:id>", methods=["PUT"])
def update_pregunta(id):
    conn = database_conection()
    data = request.get_json()
    conn.execute("update Preguntas set info_preguntas = ?, nivel = ? where id = ?", (data["info_preguntas"],data["nivel"],id))
    conn.commit()
    conn.close()
    return ("Preguntas updated", 200)
#delete
@app.route("/Preguntas/<int:id>", methods=["DELETE"])
def delete_pregunta(id):
    conn = database_conection()
    conn.execute("delete from Preguntas where id = ?", (id,))
    conn.commit()
    conn.close()
    return ("Pregunta deleted", 204)

### Sesion
# create
@app.route("/Sesion/", methods=["POST"])
def create_sesion():
    conn = database_conection()
    data = request.get_json()
    conn.execute("insert into Sesion (id_jugador, juegos_completados, monedas_ganadas, fecha) values (?,?,?,?)",(data["id_jugador"],data["juegos_completados"],data["monedas_ganadas"],datetime.today().strftime('%Y-%m-%d')))
    conn.commit()
    conn.close()
    return ("New Sesion added to database", 201)
# read all
@app.route("/Sesion/", methods=["GET"])
def get_all_sesiones():
    conn = database_conection()
    sesiones = conn.execute("select * from Sesion").fetchall()
    conn.close()
    return jsonify([dict(row) for row in sesiones])
# read one
@app.route("/Sesion/<int:id>", methods=["GET"])
def get_one_sesion(id):
    conn = database_conection()
    sesion = conn.execute("select * from Sesion where id = ?", (id,)).fetchone()
    conn.close()
    if sesion:
        return jsonify(dict(sesion))
    else:
        return ("ID not found", 404)
#update
@app.route("/Sesion/<int:id>", methods=["PUT"])
def update_sesion(id):
    conn = database_conection()
    data = request.get_json()
    conn.execute("update Sesion set id_jugador = ?, juegos_completados = ?, monedas_ganadas = ?, fecha = ? where id = ?", (data["id_jugador"],data["juegos_completados"],data["monedas_ganadas"],data["fecha"], id))
    conn.commit()
    conn.close()
    return ("Sesion updated", 200)
#delete
@app.route("/Sesion/<int:id>", methods=["DELETE"])
def delete_sesion(id):
    conn = database_conection()
    conn.execute("delete from Sesion where id = ?", (id,))
    conn.commit()
    conn.close()
    return ("Sesion deleted", 204)

### RespuestaJugador
# create
@app.route("/RespuestaJugador/", methods=["POST"])
def create_rj():
    conn = database_conection()
    data = request.get_json()
    conn.execute("insert into RespuestaJugador (id_jugador, id_sesion, nivel, correctas) values (?,?,?,?)",(data["id_jugador"],data["id_sesion"],data["nivel"],data["correctas"]))
    conn.commit()
    conn.close()
    return ("New RespuestaJugador added to database", 201)
# read all
@app.route("/RespuestaJugador/", methods=["GET"])
def get_all_rj():
    conn = database_conection()
    rj = conn.execute("select * from RespuestaJugador").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rj])
# read one
@app.route("/RespuestaJugador/<int:id>", methods=["GET"])
def get_one_rj(id):
    conn = database_conection()
    rj = conn.execute("select * from RespuestaJugador where id = ?", (id,)).fetchone()
    conn.close()
    if rj:
        return jsonify(dict(rj))
    else:
        return ("ID not found", 404)
#update
@app.route("/RespuestaJugador/<int:id>", methods=["PUT"])
def update_rj(id):
    conn = database_conection()
    data = request.get_json()
    conn.execute("update RespuestaJugador set id_jugador = ?, id_sesion = ?, nivel = ?, correctas = ? where id = ?", (data["id_jugador"],data["id_sesion"],data["nivel"],data["correctas"],id))
    conn.commit()
    conn.close()
    return ("RespuestaJugador updated", 200)
#delete
@app.route("/RespuestaJugador/<int:id>", methods=["DELETE"])
def delete_rj(id):
    conn = database_conection()
    conn.execute("delete from RespuestaJugador where id = ?", (id,))
    conn.commit()
    conn.close()
    return ("RespuestaJugador deleted", 204)

### Recompensas
# create
@app.route("/Recompensas/", methods=["POST"])
def create_recompensa():
    conn = database_conection()
    data = request.get_json()
    conn.execute("insert into Recompensas (nombre, costo) values (?,?)",(data["nombre"],data["costo"]))
    conn.commit()
    conn.close()
    return ("New Recompensas added to database", 201)
# read all
@app.route("/Recompensas/", methods=["GET"])
def get_all_recompensas():
    conn = database_conection()
    recompensa = conn.execute("select * from Recompensas").fetchall()
    conn.close()
    return jsonify([dict(row) for row in recompensa])
# read one
@app.route("/Recompensas/<int:id>", methods=["GET"])
def get_one_recompensa(id):
    conn = database_conection()
    recompensa = conn.execute("select * from Recompensas where id = ?", (id,)).fetchone()
    conn.close()
    if recompensa:
        return jsonify(dict(recompensa))
    else:
        return ("ID not found", 404)
#update
@app.route("/Recompensas/<int:id>", methods=["PUT"])
def update_recompensa(id):
    conn = database_conection()
    data = request.get_json()
    conn.execute("update Recompensas set nombre = ?, costo = ? where id = ?", (data["nombre"],data["costo"], id))
    conn.commit()
    conn.close()
    return ("Recompensas updated", 200)
#delete
@app.route("/Recompensas/<int:id>", methods=["DELETE"])
def delete_recompensa(id):
    conn = database_conection()
    conn.execute("delete from Recompensas where id = ?", (id,))
    conn.commit()
    conn.close()
    return ("Recompensas deleted", 204)

### CanjeRecompensas
# create
@app.route("/CanjeRecompensas/", methods=["POST"])
def create_cr():
    conn = database_conection()
    data = request.get_json()
    conn.execute("insert into CanjeRecompensas (id_jugador, id_recompensa, fecha_canje) values (?,?, ?)",(data["id_jugador"],data["id_recompensa"],datetime.today().strftime('%Y-%m-%d')))
    conn.commit()
    conn.close()
    return ("New CanjeRecompensas added to database", 201)
# read all
@app.route("/CanjeRecompensas/", methods=["GET"])
def get_all_cr():
    conn = database_conection()
    recompensa = conn.execute("select * from CanjeRecompensas").fetchall()
    conn.close()
    return jsonify([dict(row) for row in recompensa])
# read one
@app.route("/CanjeRecompensas/<int:id>", methods=["GET"])
def get_one_cr(id):
    conn = database_conection()
    recompensa = conn.execute("select * from CanjeRecompensas where id = ?", (id,)).fetchone()
    conn.close()
    if recompensa:
        return jsonify(dict(recompensa))
    else:
        return ("ID not found", 404)
#update
@app.route("/CanjeRecompensas/<int:id>", methods=["PUT"])
def update_cr(id):
    conn = database_conection()
    data = request.get_json()
    conn.execute("update CanjeRecompensas set id_jugador = ?, id_recompensa = ? , fecha_canje = ? where id = ?", (data["id_jugador"],data["id_recompensa"], data["fecha_canje"], id))
    conn.commit()
    conn.close()
    return ("CanjeRecompensas updated", 200)
#delete
@app.route("/CanjeRecompensas/<int:id>", methods=["DELETE"])
def delete_cr(id):
    conn = database_conection()
    conn.execute("delete from CanjeRecompensas where id = ?", (id,))
    conn.commit()
    conn.close()
    return ("CanjeRecompensas deleted", 204)
