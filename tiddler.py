from datetime import datetime

def parse_tiddler(raw_text: str):
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
