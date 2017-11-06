
import csv
import pandas as pd


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/my-movies')
def list_user_movies():
    my_movies_rated = pd.read_csv('./data/my-ratings.csv', sep=',', header=0)
    all_movies=pd.read_csv('./data/movies.csv', sep=',',header=0)
    my_movies_rated = pd.merge(my_movies_rated, all_movies, on='movieId', how='inner')
    return render_template('my-movies.html', page_title='My Movies', my_movies_rated=my_movies_rated)
