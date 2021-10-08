from flask import Flask, request, render_template
from flask import send_file
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    fileList = subprocess.run(['ls', 'streams'], stdout=subprocess.PIPE).stdout.decode('utf8').split("\n")[0:-1]
    streams = []
    id = 0
    for file in fileList :
        id += 1
        name, type = file.split('.')[0:2]
        streams.append({'id' : str(id), 'name' : name, 'type' : type, 'url' : 'http://alexandar.ddns.net:8080/streams?stream={}'.format(file), 'video_codec' : 'NI', 'audio_codec' : 'NI' })
    return render_template('index.html', streams=streams)

@app.route('/player', methods=['GET'])
def player():
    url = request.args.get('url')
    return render_template('player.html', url=url)

@app.route('/streams', methods=['GET'])
def downloadFile ():
    stream = request.args.get('stream')
    path = 'streams/{}'.format(stream)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 