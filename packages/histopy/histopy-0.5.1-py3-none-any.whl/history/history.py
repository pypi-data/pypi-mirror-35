'''
BASH-esque history for the Python3 interactive interpreter.

Quickstart: 
    -Try history.history(), equivalent to bash $ history
    -Try history.recall(n), equivalent to bash $ !n
'''

import readline
import inspect

def _hprint(hlist):
    '''takes an enumerated list of lines and prints number, tab, line
    '''
    for i, line in hlist:
        print('{}\t{}'.format(i, line))

def _get_history_full():
    '''returns an enumerated list of history (numbered from the absolute
    beginning)
    '''
    hlen = readline.get_current_history_length()
    h = []
    for i in range(hlen): h.append(readline.get_history_item(i+1))
    return list(enumerate(h))

def _broken_get_history_full():
    '''this seems to only grab every other line?? no idea why it's not 
    equivalent to the explicit loop in _get_history_full.
    '''
    hlen = readline.get_current_history_length()
    history = [readline.get_history_item(i+i) for i in range(hlen)]
    return history

def _get_history_current():
    h = []
    hfull = _get_history_full()
    for i, line in hfull:
        if (line.lower().startswith('quit()') or 
                line.lower().startswith('exit()')):
            h = []
        else:
            h.append((i, line))
    return h

def history():
    '''Print all commands entered in current session
    '''
    _hprint(_get_history_current())

def history_full():
    '''Print all commands entered ever
    '''
    _hprint(_get_history_full())

def recall(n):
    '''execute command n from the full history
    '''
    _exec_lines([_get_history_full()[n]])

def recall_range_old(n1, n2):
    '''Execute commands between n1 and n2 (python slice style)
    This currently stops executing if it hits a command that throws an error
    '''
    exec('\n'.join(item[1] for item in _get_history_full()[n1:n2]))


def recall_range(n1, n2):
    full_queue = _get_history_full()[n1:n2]
    current_queue = []
    while full_queue:
        current_queue.append(full_queue.pop(0))
        while full_queue and full_queue[0][1][0].isspace():
            current_queue.append(full_queue.pop(0))
        current_queue = _exec_lines(current_queue)

def _exec_lines(lines):
    top_globals = inspect.stack()[-1].frame.f_globals
    exec_string = '\n'.join([line[1] for line in lines])
    try:
        exec(exec_string, top_globals)
    except Exception as err:
        if err.args[0] == 'unexpected EOF while parsing':
            return lines
        else:
            raise
    return [(0,'')]


def find(term):
    '''print lines matching term. For now it's a simple string find, case-
    insensitive by default.
    '''
    _hprint([
        (i, line) for i, line in _get_history_current()
        if term.lower() in line.lower()
        ])



                



