# Crypt Wiki - VimWiki with added support for encryption/decryption

This project is meant to solve an issue I have ran into recently. I wanted to
have a way of version controlling my notes while also retaining my privacy.

## Dependencies

In order to use this repo you will need:

- Vim
- VimWiki
- Python
- pip : `python -m pip install pip`
- python-gnupg : `python -m pip install python-gnupg`

## How to use

In order to use the Crypt Wiki locally, run `git clone https://github.com/adriancostin6/crypt-wiki.git`.

If you want to version control your notes like I do, simply fork this repository, clone your fork and enjoy
version controlled encrypted notes.

## How we got here

If you care for it, you can read the [Backstory](Backstory.md) of how we got here.
I promise not to bore you too much.

## Stop it! Get some help.

All the help you need in order to setup the wiki can be found in the [Tutorial](tutorial/index.md)
section. Some of the topics included are:

- [How to setup VimWiki](tutorial/Setup.md)
- [How to use VimWiki](tutorial/Usage.md)
- [Encryption/Decryption and Version Control](tutorial/Storage.md)


## Typical workflow I would use

I have provided a couple of placeholder directories for you to see how I would
typically organize my notes inside the wiki. This however does not mean that you
shouldn't experiment and find a layout that best fits you.

- [Diary](diary/diary.md)
- [Personal](personal/index.md)
- [Work](work/index.md)


## .cryptfile and encryption/decryption

After taking some notes and separating them in a workflow like above, say you
want to mark some of the folders for encryption. Let's assume that you want
everything under *Work* and *Diary* to be encrypted using GPG. For that you will
use the *cript.py* script in this repository.

Firstly, you will need to setup a *.cryptfile* that contains two lines in it,
each specifying the name of a directory you want to encrypt.

An example .cryptfile has been provided that encrypts the work and diary directory.

```
.cryptfile

work
diary
```

Secondly, you want to modify the script to include the GPG key identifier and
the path to where your GPG folder is stored:

```
#############################################
# Define these for proper encryption!
gpg = gnupg.GPG(gnupghome=r'path/to/folder')
recipient = "john@mail.com"
#############################################
```

Lastly, to encrypt run `python crypt.py -e`. After the files have been encrypted
you can commit and push to version control as normal.

Decryption happens in a similar manner. Once you clone the repo, run
`python crypt.py -d`.

## Day-to-day use

With the proper setup described in the tutorial, opening Vim and using the 
VimWiki shortcuts will work out of the box, placing you inside the *index.md*
file in this directory, which is the Wiki index. You can choose to delete all
the other files such as the *Backstory.md*, *README.md* or the *tutorial* folder,
as these have been in order to showcase how the repository works.

Happy wiki-ing!
