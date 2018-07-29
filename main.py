import json

from flask import Flask, Response, request, jsonify

from tiddler import all_tiddlers, contents_of_tiddler, search_all_tiddlers
from auth import require_auth

app = Flask(__name__)

@app.route('/', methods=['GET'])
@require_auth
def root():
    return jsonify(all_tiddlers())

@app.route('/t/<name>', methods=['GET'])
@require_auth
def get_tiddler(name: str):
    tiddler = contents_of_tiddler(name)
    if not tiddler:
        return '', 404
    return jsonify(contents_of_tiddler(name))

@app.route('/search')
@require_auth
def search():
    query = request.args.get('query')
    if not query:
        return 'missing query', 400
    matches = search_all_tiddlers(query)
    return jsonify(matches)

app.run(host='0.0.0.0')
