import flask
from flask import Flask, render_template,request
from sklearn.externals import joblib
import io
import csv
import pandas as pd
from sqlalchemy import create_engine
import pymysql
 
#if __name__ == '__main__':
#    model = joblib.load('model.pkl')
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="demouser",
                               pw="demo123",
                               db="training"))
app = Flask(__name__)
@app.route("/")
@app.route("/index")
def index():
	return flask.render_template('index.html')

import numpy as np

from scipy import misc

import MySQLdb
class Database:

    host = 'localhost'
    user = 'demouser'
    password = 'demo123'
    db = 'training'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def commit(self): 
        try:    
            self.connection.commit()
        except:
            self.connection.rollback()

    def df_to_dql(self,df):
	df.to_sql(con=engine,name='regression_training_set',if_exists='append')

    def insert_row(self, query,row): 
        try:    
            self.cursor.execute(query,row)
            self.connection.commit()
        except:
            self.connection.rollback()

    def insert(self, query): 
        try:    
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()

        def query(self, query):
                cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
                cursor.execute(query)
                return cursor.fetchall()

        def __del__(self):
                self.connection.close()


@app.route('/train', methods=['POST'])
def train_dataset():
    if request.method=='POST':
        file = request.files['dataset']
	if not file: 
		return render_template('index.html', label="No file")
	stream = io.StringIO(file.stream.read().decode("ascii"), newline=None)
	df = pd.read_csv(stream)
	print(df)		
	sqldb = Database()
	df.to_sql(con=engine,name='regression_training_set',if_exists='append',index=False) 
	sqldb.commit()
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method=='POST':
        file = request.files['dataset']
	if not file: 
		return render_template('index.html', label="No file")
	img = misc.imread(file)
	return render_template('index.html', label=label, file=file)


if __name__ == '__main__':
	app.run(host='192.187.114.202', port=8000, debug=True)

