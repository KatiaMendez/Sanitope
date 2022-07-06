import encodings
import string
import requests as req
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import pandas as pd
import os
from simpledbf import Dbf5
from sqlalchemy import create_engine
import pandas.io.sql as psql


# initializations
app = Flask(__name__)

# Mysql Connection
#app.config['MYSQL_HOST'] = 'localhost' 
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = 'indiceanemia' # nombre de la base de datos
#mysql = MySQL(app)

#conexion = create_engine('mysql+pymysql://root@localhost:3306/indiceanemia')
#con = conexion.raw_connection()
#cur = con.cursor()

# settings
app.secret_key = "mysecretkey"


# rutas
@app.route('/') # respuesta a ruta inicial del servidor  
def Index():
    return render_template('index.html')

@app.route('/quehacemos')
def quienes_somos():
    return render_template('quehacemos.html')

@app.route('/nuestroEquipo')
def nuestro_equipo():
    return render_template('nuestroEquipo.html')

@app.route('/explora')
def explora():
    return render_template('explora.html')

"""
@app.route('/exploraInstitucion')
def explora_institucion():
    cur = mysql.connection.cursor()
    cur.execute('SELECT DISTINCT id, nombre, descripción, años_alcance FROM db_datasets')
    data = cur.fetchall()
    cur.close()   
    return render_template('explorainstitucion.html', datasets = data)

@app.route('/exploraDataset')
def explora_dataset():
    cur = mysql.connection.cursor()
    cur.execute('SELECT DISTINCT id, nombre, descripción, años_alcance FROM db_datasets')
    data = cur.fetchall()
    cur.close()   
    return render_template('exploraDataset.html', datasets = data)
"""
@app.route('/crea')
def crea():
    return render_template('crea.html')

@app.route('/comparte')
def comparte():
    return render_template('comparte.html')

@app.route('/analiza')
def analisis():
    return render_template('analiza.html')

@app.route('/analizapais')
def analisis_pais():
    return render_template('analizapais.html')

@app.route('/analizaregion')
def analisis_region():
    return render_template('analizaregion.html')


"""
@app.route('/descargaDatos/<id1>/<id2>')
def descarga_datos(id1,id2):
    tabla = pd.read_sql_query('SELECT tabla_relacionada FROM db_datasets WHERE id ={0}'.format(id1), con=conexion)
    tabla = tabla.iloc[0]['tabla_relacionada']
    a = pd.read_sql_query('SELECT * FROM `{0}`'.format(tabla), con=conexion)
    print(a)
    if id2 == 'CSV':
        a.to_csv('static/files/Doc/BD'+id1+'/BD'+id1+'.csv', encoding = 'utf-8')
    if id2 == 'SQL':
        a.to_json('static/files/Doc/BD'+id1+'/BD'+id1+'.json')
    if id2 == 'STATA':
        a.to_stata('static/files/Doc/BD'+id1+'/BD'+id1+'.dta')
    else:
        print("no entró a ninguno")
    return render_template('exploraDataset.html')



@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])

"""
"""
@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
          # SET fullname = %s,
           #    email = %s,
           #    phone = %s
         #  WHERE id = %s
"""
        , (fullname, email, phone, id))
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('Index'))

@app.route('/descargas')
def descargas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT DISTINCT Cod_Encuesta, Encuesta, Año FROM db_endes')
    data = cur.fetchall()
    cur.close()
    return render_template('descargas.html', encuestas = data)


@app.route('/descargar_fictec/<id>/<id2>')
def descargar_fictec(id,id2):
    ruta_ftec = 'http://iinei.inei.gob.pe/iinei/srienaho/descarga/FichaTecnica/'+id+'-Ficha.pdf'
    file = req.get(ruta_ftec, allow_redirects=True)
    pdf = open('FichaTecnica'+id2+'.pdf', 'wb')
    pdf.write(file.content)
    pdf.close()
    flash('Descarga realizada correctamente')  
    return redirect(url_for('descargas'))

"""

# iniciamos el servidor
if __name__ == "__main__":
    app.run(port=3000, debug=True)
