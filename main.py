import os
import json

from flask import Flask, request, Response

app = Flask(__name__)

TIDDLYWIKI_DIRECTORY = os.environ['TIDDLYWIKI_DIRECTORY']

@app.route('/', methods=['GET'])
def root():
    wiki = list(os.walk(TIDDLYWIKI_DIRECTORY + '/tiddlers'))[0]
    tiddlers = []
    for tiddler in wiki[2]:
        if tiddler.startswith('$__'):
            # shadow/system tiddler
            continue
        elif '.jpg' in tiddler or '.png' in tiddler:
            # images
            continue
        tiddlers.append(tiddler.replace('.tid', ''))
    return Response(json.dumps(tiddlers), mimetype='application/json')

@app.route('/t/<name>', methods=['GET'])
def get_tiddler(name: str):
    filepath = TIDDLYWIKI_DIRECTORY + '/tiddlers/' + name + '.tid'
    if not os.path.exists(filepath):
        return Response(status=404)
    with open(filepath) as file:
        tiddler = file.read()
    return tiddler

app.run(host='0.0.0.0')
