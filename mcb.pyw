#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

# Copy/paste requires pyperclip module; command line arguments require sys module.

import shelve, pyperclip, sys 
mcbShelf = shelve.open('mcb')

# TO-DO: Save clipboard content.

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
  mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:

  # TO-DO: List keywords and load content.

  if sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(mcbShelf.keys())))
  elif sys.argv[1] in mcbShelf:
    pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

# It takes what you have copied already, and you can save it to a keyword. 
# Obviously it will save nothing if you have nothing copied.
# But how do you edit the list of keywords/values that you copied...?
# This is an interesting short-term fix but hard to justify over the fetch script from other day.
