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
    return render_template('filmes.html', nome=nome, titulo=titulo, torrent=torrent)
if __name__ == '__name__':
    app.run(debug=True)