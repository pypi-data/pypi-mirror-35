class InvalidParseModeError(Exception):
    pass

name = "text2ml"

def format(text, entities, parse_mode):
    if parse_mode.lower() == 'html':
        return text2html(text, entities)
    elif parse_mode.lower() == 'markdown':
        return text2markdown(text, entities)
    else:
        raise InvalidParseModeError('Invalid parse_mode "%s"' % parse_mode)


def text2html(text, entities):
    len_s = 0
    for entity in entities:
        if entity['type'] == 'bold':
            text = text[:entity['offset'] + len_s] + '<b>' + text[entity['offset'] + len_s:]
            len_s += 3
            text = text[:entity['offset'] + entity['length'] + len_s] + '</b>' + text[entity['offset'] + entity['length'] + len_s:]
            len_s += 4

        elif entity['type'] == 'italic':
            text = text[:entity['offset'] + len_s] + '<i>' + text[entity['offset'] + len_s:]
            len_s += 3
            text = text[:entity['offset'] + entity['length'] + len_s] + '</i>' + text[entity['offset'] + entity['length'] + len_s:]
            len_s += 4

        elif entity['type'] == 'code':
            text = text[:entity['offset'] + len_s] + '<code>' + text[entity['offset'] + len_s:]
            len_s += 6
            text = text[:entity['offset'] + entity['length'] + len_s] + '</code>' + text[entity['offset'] + entity['length'] + len_s:]
            len_s += 7

        elif entity['type'] == 'pre':
            text = text[:entity['offset'] + len_s] + '<pre>' + text[entity['offset'] + len_s:]
            len_s += 5
            text = text[:entity['offset'] + entity['length'] + len_s] + '</pre>' + text[entity['offset'] + entity['length'] + len_s:]
            len_s += 6

        elif entity['type'] == 'text_link':
            text = text[:entity['offset'] + len_s] + '<a href="{}">'.format(entity['url']) + text[entity['offset'] + len_s:]
            len_s += len('<a href="{}">'.format(entity['url']))
            text = text[:entity['offset'] + entity['length'] + len_s] + '</a>' + text[entity['offset'] + entity['length'] + len_s:]
            len_s += 4

    return text


def text2markdown(text, entities):
    len_s = 0
    for entity in entities:
        if entity['type'] == 'bold':
            text = text[:entity['offset'] + len_s] + '*' + text[entity['offset'] + len_s:]
            len_s += 1
            text = text[:entity['offset'] + entity['length'] + len_s] + '*' + text[entity['offset'] + entity['length'] + len_s:]
            len_s += 1

        elif entity['type'] == 'italic':
            text = text[:entity['offset'] + len_s] + '_' + text[entity['offset'] + len_s:]
            len_s += 1
            text = text[:entity['offset'] + entity['length'] + len_s] + '_' + text[entity['offset'] + entity['length'] + len_s:]
            len_s += 1

        elif entity['type'] == 'code':
            text = text[:entity['offset'] + len_s] + '`' + text[entity['offset'] + len_s:]
            len_s += 1
            text = text[:entity['offset'] + entity['length'] + len_s] + '`' + text[entity['offset'] + entity['length'] + len_s:]
            len_s += 1

        elif entity['type'] == 'pre':
            text = text[:entity['offset'] + len_s] + '```' + text[entity['offset'] + len_s:]
            len_s += 3
            text = text[:entity['offset'] + entity['length'] + len_s] + '```' + text[entity['offset'] + entity['length'] + len_s:]
            len_s += 3

        elif entity['type'] == 'text_link':
            text = text[:entity['offset'] + len_s] + '[' + text[entity['offset'] + len_s:]
            len_s += 2
            text = text[:entity['offset'] + entity['length'] + len_s] + ']' + '({})'.format(entity['url']) + text[entity['offset'] + entity['length'] + len_s:]
            len_s += len('({})'.format(entity['url']))

    return text
