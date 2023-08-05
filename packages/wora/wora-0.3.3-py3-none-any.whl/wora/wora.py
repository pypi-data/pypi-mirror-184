from datetime import datetime

def timestamp(fmt: str) -> str:
    ''' Format timestamps for the current datetime '''
    return datetime.now().strftime(fmt)

def insert_every(n, s, sep=' '):
    ''' Insert a string s for every n characters '''
    return sep.join(s[i:i+n] for i in range(0, len(s), n))
