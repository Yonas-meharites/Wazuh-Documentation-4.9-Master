from pygments.style import Style
from pygments.token import Token, Comment, Keyword, Name, String

class PygmentsWazuh(Style):
    styles = {
        Token:                  '',  # Default style for all tokens
        Comment:                'italic #888',  # Italic and grey color for comments
        Keyword:                'bold #005',  # Bold and dark blue color for keywords
        Name:                   'bold #f00',  # Bold and red color for names
        Name.Class:             'bold underline #0f0',  # Bold, underlined, and green color for class names
        Name.Function:          'italic #0f0',  # Italic and green color for function names
        String:                 'bg:#eee #111',  # Light grey background with dark grey text for strings
    }
