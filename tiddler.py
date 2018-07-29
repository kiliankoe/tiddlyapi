import os
from datetime import datetime

TIDDLYWIKI_DIRECTORY = os.environ['TIDDLYWIKI_DIRECTORY']

def all_tiddlers(include_system=False, include_images=False):
    tiddlers = os.listdir(TIDDLYWIKI_DIRECTORY + '/tiddlers/')
    if not include_system:
        tiddlers = [tid for tid in tiddlers if not tid.startswith('$__')]
    if not include_images:
        tiddlers = [tid for tid in tiddlers if not '.jpg' in tid
                                            and not '.png' in tid]
    tiddlers = [tid.replace('.tid', '') for tid in tiddlers]
    return tiddlers

def contents_of_tiddler(name: str):
    filepath = TIDDLYWIKI_DIRECTORY + '/tiddlers/' + name + '.tid'
    if not os.path.exists(filepath):
        return None
    with open(filepath) as file:
        tiddler = file.read()
    return _parse_tiddler(tiddler)

def search_all_tiddlers(query: str):
    tiddlers = all_tiddlers()
    matches = []
    for tiddler in tiddlers:
        with open(TIDDLYWIKI_DIRECTORY + '/tiddlers/' + tiddler + '.tid') as file:
            contents = file.read()
            if query.lower() in contents.lower():
                matches.append(tiddler)
    return matches

def _parse_tiddler(raw_text: str):
    meta = []
    content = ''
    lines = raw_text.split('\n')
    for idx, line in enumerate(lines):
        if line is not '':
            meta.append(line)
        else:
            content = '\n'.join(lines[idx+1:])
            break

    tiddler = {
        'content': content
    }

    for m in meta:
        m = m.split(': ')
        tiddler[m[0]] = m[1]

    if 'created' in tiddler:
        tiddler['created'] = datetime.strptime(tiddler['created'], '%Y%m%d%H%M%S%f').strftime('%Y-%m-%dT%H:%M:%SZ')
    if 'modified' in tiddler:
        tiddler['modified'] = datetime.strptime(tiddler['modified'], '%Y%m%d%H%M%S%f').strftime('%Y-%m-%dT%H:%M:%SZ')
    if 'tags' in tiddler:
        tags = tiddler['tags'].split(' ')
        if len(tags) is 1 and tags[0] is '':
            tags = []
        tiddler['tags'] = tags
    return tiddler
