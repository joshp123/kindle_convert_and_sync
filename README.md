Short script to take a folder with .epub formatted e-books, convert them to
azw3, and sync them to your kindle.

It will eject your kindle after syncing the files.

Required packages:
    - python >= 3.8 (I recommend installing with pyenv)
    - calibri (brew cask install calibri), open source tool for managing ebooks

Usage:
    - Ensure all your ebooks are in the root of a single directory (i.e. no
      nesting)
    - Ensure your Kindle is connected via USB
    - Go to the directory containing your .epubs
    - Run `python convert_ebooks.py`

Features:
    - Uses azw3 format for now, which is allegedly better for formatting than
      .mobi, and also supports Goodreads integration on Kindle
    - Uses USB syncing instead of e-mail (which in theory means that your files
      will show up as books on your Kindle instead of "Personal Documents"
