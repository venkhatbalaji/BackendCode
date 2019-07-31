import requests
import json

def getMovieDetails(movieName, number):
    try:
        if isinstance(number,int) and isinstance(movieName,str):
            endpoint = 'https://jsonmock.hackerrank.com/api/movies/search/?'
            paramdict = {'Title':movieName, 'page':number}
            responsedata = requests.get(endpoint, params=paramdict).content
            movieData = json.loads(responsedata.decode('utf-8'))
            return movieData['data']
        else:
            print('Provide a Proper Input')
    except Exception as Ex:
        print(Ex)

def iterateMovie(movieData):
    try:
        Titles = []
        for data in movieData:
            Titles.append(data['Title'])
        Titles.sort()
        for data in Titles:
            print(data)
    except Exception as Ex:
        print(Ex)
