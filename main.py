import os
import json

from flask import Flask, Response

from tiddler import parse_tiddler
from auth import require_auth

app = Flask(__name__)

TIDDLYWIKI_DIRECTORY = os.environ['TIDDLYWIKI_DIRECTORY']

@app.route('/', methods=['GET'])
@require_auth
def root():
    wiki = list(os.walk(TIDDLYWIKI_DIRECTORY + '/tiddlers'))[0]
    tiddlers = []
    for tiddler in wiki[2]:
        if tiddler.startswith('$__'):
            continue
        if '.jpg' in tiddler or '.png' in tiddler:
            continue
        tiddlers.append(tiddler.replace('.tid', ''))
    return Response(json.dumps(tiddlers), mimetype='application/json')

@app.route('/t/<name>', methods=['GET'])
@require_auth
def get_tiddler(name: str):
    filepath = TIDDLYWIKI_DIRECTORY + '/tiddlers/' + name + '.tid'
    if not os.path.exists(filepath):
        return Response(status=404)
    with open(filepath) as file:
        tiddler = file.read()
    tiddler = parse_tiddler(tiddler)
    return Response(json.dumps(tiddler, sort_keys=True), mimetype='application/json')

app.run(host='0.0.0.0')
