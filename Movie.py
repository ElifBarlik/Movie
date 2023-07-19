import requests
import json

class TheMovie():
    def __init__(self):
        self.apikey = '40cdfcfaf7ccb8c34d1e5f95c3fb088b'
    def getPopuler(self):
        url = 'https://api.themoviedb.org/3/movie/popular?language=en-US&api_key='
        result = requests.get(url+self.apikey)
        result= result.json()
        print("\n\nPOPULER MOVIES\n")
        i=1
        for r in result["results"]:
            print(f"{i}-{r['title']}")
            i+=1
    def getTheaters(self):
        url = 'https://api.themoviedb.org/3/movie/now_playing?language=en-US&api_key='
        result = requests.get(url+self.apikey)
        result= result.json()
        print('\n\nMOVIE IN THEATERS\n')
        for r in result["results"]:
            print(r["title"])
    def searchMovie(self, key):     
        url = f"https://api.themoviedb.org/3/search/movie?query={key}&language=en-US&api_key="
        
        response = requests.get(url+self.apikey)
        response = response.json()
        for r in response["results"]:
            print(r["title"])      

movie=TheMovie()
while(True):
    secim= input('\n\n1-Populer Movies\n2-Movies in Theaters\n3-Search Movies\n4-Exit\n')
    if(secim=='4'):
        break
    else:
        if(secim=='1'):
            movie.getPopuler()
        elif(secim=='2'):
            movie.getTheaters()
        elif(secim=='3'):
            key = input('keyword: ')
            movie.searchMovie(key)
        else:
            print('wrong choice')