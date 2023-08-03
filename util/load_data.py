import json
import pandas as pd

usaGovPath = "data/usagov.txt"

with open(usaGovPath) as file:
    usaGovRecords = [json.loads(line) for line in file.readlines()]

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
movieUsers = pd.read_table('data/movieLens/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
movieRatings = pd.read_table('data/movieLens/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('data/movieLens/movies.dat', sep='::', header=None, names=mnames)
