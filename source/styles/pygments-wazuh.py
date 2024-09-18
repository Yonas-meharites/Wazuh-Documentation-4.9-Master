from pygments.style import Style
from pygments.token import Token, Comment, Keyword, Name, String, Error, Generic, Number, Operator

class YourStyle(Style):
    styles = {
        Token:                  '',
        Comment:                'italic #888',
        Keyword:                'bold #005',
        Name:                   '#f00',
        Name.Class:             'bold #0f0',
        Name.Function:          '#0f0',
        String:                 'bg:#eee #111'
    }
