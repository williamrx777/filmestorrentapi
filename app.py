from flask import Flask,render_template,request,redirect,url_for
import requests
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        filmes = request.form['nome']
        return redirect(url_for('filmes',nome=filmes))
    else:    
        return render_template('index.html')
@app.route('/filmes/<nome>')
def filmes(nome=None):
    url = "https://movie-tv-music-search-and-download.p.rapidapi.com/search"

    querystring = {"keyword":nome,"quantity":"10"}

    headers = {
	"X-RapidAPI-Key": "a20c999515msh9ad00c73d2b660ap1c376ajsn2046be0cfe12",
	"X-RapidAPI-Host": "movie-tv-music-search-and-download.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    filme = response.json()
    
    titulo = filme['result'][0]['title']
    torrent = filme['result'][0]['torrent']
    titulo1 = filme['result'][1]['title']
    torrent1 = filme['result'][1]['torrent']
    titulo2 = filme['result'][2]['title']
    torrent2 = filme['result'][2]['torrent']
    titulo3 = filme['result'][3]['title']
    torrent3 = filme['result'][3]['torrent']
    titulo4 = filme['result'][4]['title']
    torrent4 = filme['result'][4]['torrent']
    titulo5 = filme['result'][5]['title']
    torrent5 = filme['result'][5]['torrent']
    titulo6 = filme['result'][6]['title']
    torrent6 = filme['result'][6]['torrent']
    titulo7 = filme['result'][7]['title']
    torrent7 = filme['result'][7]['torrent']
    titulo8 = filme['result'][8]['title']
    torrent8 = filme['result'][8]['torrent']
    titulo9 = filme['result'][9]['title']
    torrent9 = filme['result'][9]['torrent']   
    
    return render_template('filmes.html',
                            nome=nome,
                              titulo=titulo,
                                torrent=torrent,
                                filme=filme,
                                titulo1=titulo1,
                                titulo2=titulo2,
                                titulo3=titulo3,
                                titulo4=titulo4,
                                titulo5=titulo5,
                                titulo6=titulo6,
                                titulo7=titulo7,
                                titulo8=titulo8,
                                titulo9=titulo9,
                                torrent1=torrent1,
                                torrent2=torrent2,
                                torrent3=torrent3,
                                torrent4=torrent4,
                                torrent5=torrent5,
                                torrent6=torrent6,
                                torrent7=torrent7,
                                torrent8=torrent8,
                                torrent9=torrent9
                                )
if __name__ == '__name__':
    app.run(debug=True)