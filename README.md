# Cryptwiki

Cryptwiki is meant to solve an issue I have ran into recently. I wanted to
have a way of version controlling my notes while also retaining my privacy.

This repository provides some scripts for version controlling a directory structure, with support for recursive GPG
encryption via the *crypt.py* script. Version control is supported via the *push/pull-notes* scripts (shell or batch,
depending on operating system).

## Possible applications

As the name of the repo suggests, the main use-case for which I developed this convenient system is in order to easily
create and store my notes online. Some of them contain sensitive information, justifying the need for the recursive
encryption script. 

The workflow I use is based on [vimwiki](https://github.com/vimwiki/vimwiki). Mainly, my notes are organized into separate directories based on the different
categories I wish to take notes in, then these directories are ecrypted and version controlled and everything is
integrated nicely with Vim. I have provided instructions for how to achieve this in the [Tutorial](tutorial/index.md) section.

That being said, using Vim is definitely not required, just convenient to me. They are just text files after all, you
can use any text editor for taking them.

## How to use

- Fork this repository
- Start taking notes and store them in the arrangement that best suits you
- Add the folders you wish to encrypt to the *.cryptfile*
- Use version control scripts to store the notes in the repository. (Tip: Make the repo private :) )

## Dependencies

- Python
- pip : `python -m pip install pip`
- python-gnupg : `python -m pip install python-gnupg`

**Happy wiki-ing!**
