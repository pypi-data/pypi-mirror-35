
# for template types as list, dict @t is the type of list arg and @k, @v of dict args
TYPED_API = {
    # methods
    'global': {
        'exit':  ['Int', 'Void'],
        'to_string': ['Any', 'String']
    },

    'io': {
        'display':     ['*Any', 'Void'],
        'read':        ['String'],
        'read_file':   ['String', 'String'],
        'write_file':  ['String', 'String', 'Void']
    },

    'system': {
        'args':         [['List', 'String']]
    },

    'regexp': {
        'compile':      ['String', 'Regexp'],
        'escape':       ['String', 'String']
    },

    'math': {
        'tan':          ['Number', 'Float'],
        'sin':          ['Number', 'Float'],
        'cos':          ['Number', 'Float'],
        'ln':           ['Number', 'Float'],
        'log':          ['Number', 'Number', 'Float']
    },

    'List': {
        'push':       ['@t', 'Void'],
        'pop':        ['@t'],
        'insert':     ['@t', 'Void'],
        'insert_at':  ['@t', 'Int', 'Void'],
        'concat':     [['List', '@t'], ['List', '@t']],
        'repeat':     ['Int', ['List', '@t']],
        'push_many':  [['List', '@t'], 'Void'],
        'remove':     ['@t', 'Void'],
        'length':     ['Int'],
        'join':       [['List', 'String'], 'String'],
        'map':        [['Function', '@t', '@y'], ['List', '@y']],
        'filter':     [['Function', '@t', 'Boolean'], ['List', '@t']]
    },

    'Dictionary': {
        'keys':       ['List', '@k'],
        'values':     ['List', '@v'],
        'length':     ['Int']
    },
    'String': {
        'find':       ['String', 'Int'],
        'to_int':     ['Int'],
        'split':      ['String', ['List', 'String']],
        'c_format':   [['Array', 'String'], 'String'],
        'upper':      ['String'],
        'lower':      ['String'],
        'title':      ['String'],
        'center':     ['Int', 'String', 'String'],
        'find_from':  ['String', 'Int', 'Int'],
        'length':     ['Int'],
    },
    'Set': {
        '|':           [['Set', '@t'], ['Set', '@t']],
        'add':         ['@t', 'Void'],
        'remove':      ['@t', 'Void'],
        '&':           [['Set', '@t'], ['Set', '@t']],
        '^':           [['Set', '@t'], ['Set', '@t']],
        '-':           [['Set', '@t'], ['Set', '@t']]
    },
    'Int': {'to_int': ['Int'], 'to_float': ['Float']},
    'Float': {'to_int': ['Int'], 'to_float': ['Float']},
    'Array': {
        'length':      ['Int'],
        'index':       ['@t', 'Int'],
        'count':       ['@t', 'Int']
    },

    'Tuple': {
        'length':       ['Int']
    },

    'Regexp': {
        'match':        ['String', 'RegexpMatch'],
        'groups':       ['String', ['String']]
    },

    'RegexpMatch': {
        'group':        ['Int', 'String']
    },

    '_generic_List':    ['List', '@t'],
    '_generic_Set':     ['Set', '@t'],
    '_generic_Array':   ['Array', '@t'],
    '_generic_Tuple':   ['Tuple', '@t'],
    '_generic_Dictionary': ['Dictionary', '@k', '@v'],
    # 'List#pop':        [_, '@t'],
    # 'List#insert':     [_, 'Null'],
    # 'List#remove':     [_, 'Null'],
    # 'List#remove_at':  [_, 'Null'],
    # 'List#length':     [_, 'Int'],
    # 'List#concat_one': [_, 'List<@t>'],
    # 'List#concat':     [_, 'List<@t>'],
    # 'List#[]':         [_, '@t'],
    # 'List#[]=':        [_, 'Null'],
    # 'List#slice':      [_, 'List<@t>'],

    # 'Dict#keys':       [_, 'List<@k>'],
    # 'Dict#values':     [_, 'List<@v>'],
}

# useful for error messages

ORIGINAL_METHODS = {
    'List': {
        'push':       'append(element)',
        'pop':        'pop',
        'insert':     'insert(element)',
        'insert_at':  'insert(element, index)',
        'concat':     '+',
        'repeat':     '*',
        'push_many':  'extend(other)',
        'remove':     'remove',
        'length':     'len',
        'map':        'list comprehension / map',
        'filter':     'list comprehension / filter'
    },

    'Dictionary': {
        'keys':       'keys',
        'values':     'values',
        'length':     'len'
    },

    'Int': {
        'to_int':     'int',
        'to_float':   'float'
    },
    'Float': {
        'to_int':     'int',
        'to_float':   'float'
    },
    'String': {
        'find':       'index(substring)',
        'join':       'join(elements)',
        'split':      'split(delimiter)',
        'c_format':   '%',
        'format':     'format(*elements)',
        'upper':      'upper',
        'lower':      'lower',
        'title':      'title',
        'center':     'center',
        'find_from':  'index(substring, index)',
        'to_int':     'int'
    },
    'Set': {
        '|':           '|',
        'add':         'add(element)',
        'remove':      'remove(element)',
        '&':           '&',
        '^':           '^',
        '-':           '-'
    },

    'Array': {
        'length':      'len',
        'find':        'find(element)',
        'count':       'count(element)'
    },

    'Tuple': {
        'length':       'len'
    },

    'Regexp': {
        'match':        'match(value)',
        'groups':       'find_all(value)'
    },

    'RegexpMatch': {
        'group':        'group(z)'
    }
}
