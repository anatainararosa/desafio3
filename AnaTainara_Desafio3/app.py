from flask import Flask, render_template

app = Flask(__name__)

#INDEX
@app.route ("/home")
def index ():
	return render_template('index.html')


#QuemSomos
@app.route ("/quemsomos")
def index ():
	return render_template('quemsomos.html')

#Contatos
@app.route ("/contatos")
def index ():
	return render_template('contatos.html')