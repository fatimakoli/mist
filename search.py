from flask import Flask, request, render_template, url_for, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

app.config['MONGO_DBNAME'] = 'searches'
app.config['MONGO_URI'] = 'mongodb://<mist>:<mist>@ds159507.mlab.com:59507/searches'

@app.route("/", methods=['GET'])
def home(): 
	return render_template('home.html')

@app.route("/searches", methods=['POST'])
def search():
	words = mongo.db.search
	words.insert({'word' : request.form['text']})
	results = words.find()
	return render_template('search.html', text=request.form['text'], tasks=results)

@app.route("/deleted")
def startover():
	words = mongo.db.search
	words.remove()
	results = words.find()
	#return render_template('search.html', tasks=results)
	return redirect(url_for('home'))

'''
@app.route("/add")
def add():
	words = mongo.db.search
	words.insert({'word': 'yes'})
	words.insert({'word': 'say'})
	words.insert({'word': 'uh'})
	return 'Added Users!'

@app.route("/find")
def find():
	words = mongo.db.search
	cedric = words.find_one({'word' : 'ew'})
	return 'You found ' + cedric['word'] 

@app.route("/delete")
def delete():
	words = mongo.db.search
	kelly = words.find_one({'word': 'ew'})
	words.remove(kelly)
	return "Removed"
#}
'''

if __name__== "__main__":
	app.run(debug=True)
