#!/usr/bin/env python3
import gnupg
import getopt, sys
import os

#############################################
# Define these for proper encryption!
gpg = gnupg.GPG(gnupghome=r'path/to/gnupg/folder')
recipient = "john@mail.com"
#############################################

def encrypt(folders):
    #Iterate over input dirs
    for i in folders:
        #Walk the file tree
        for root, dirs, files in os.walk(i):
            #Iterate through all the files
            for file in files:
                #Encrypt file and write
                fname = os.path.join(root,file)
                with open(fname, 'rb') as f:
                    out_filename = fname + '.gpg'
                    status = gpg.encrypt_file(
                            f, recipients=[recipient],
                            output = out_filename
                            )
                #Remove original file 
                os.remove(fname)

def decrypt(folders): 
    #Iterate over input dirs
    for i in folders:
        #Walk the file tree
        for root, dirs, files in os.walk(i):
            #Iterate through all the files
            for file in files:
                #Encrypt file and write
                fname = os.path.join(root, file)
                with open(fname, 'rb') as f:
                    out_filename = fname.replace('.gpg', '');
                    status = gpg.decrypt_file(
                            f, output = out_filename
                            )

                #Remove original file 
                os.remove(fname)

def usage():
    print(
            '''
Encrypts/Decrypts files in specified root folders and all subfolders.
Usage: python crypt.py
Requires: .cryptfile - one column text file where each row is a dir to encrypt
Options:
       -h | --help          Show help
       -e | --encrypt       Encryption mode
       -d | --decrypt       Decryption mode

Make sure to edit the script and specify the location of your gnupg dir before
running. The script also requires that you define a recipient which is a form of
id for the key that will be used for encryption (an e-mail address should do, or
a fingerprint or a key id). Keys should already be set-up and ready on your system.

Typical gnupg locations include:
    Win: C:\\Users\\<Name>\\AppData\\Roaming\\gnupg
    Linux: ~/.gnupg
Recipient example: Fingerprint, Key ID, e-mail (john@mail.com)
            '''
            )

def main():
    try:
        optlist, args = getopt.getopt(
                sys.argv[1:], 'hed', [ 'help', 'encrypt', 'decrypt' ]
                )
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    folders = []
    try:
        with open(".cryptfile") as f:
            for line in f:
                folders.append(line.strip());
    except FileNotFoundError:
        print(
                '''
ERROR: Cryptfile not found!

Please create a .cryptfile inside the script directory that
specifies which folders you want to encrypt/decrypt. Try again
afterwards.

An cryptfile is a blank text file where each line contains the name of a
directory you want encrypted. Specifying a directory name in the cryptfile
defines a file tree root from which the script will start the encryption
process.

!!Attention!! crypt.py will encrypt all the data in the specified file trees, 
so make sure this is the behavior you want.

Example structure of cryptfile:

folder1
folder2

Make sure to edit the script and specify the location of your gnupg dir before
running. The script also requires that you define a recipient which is a form of
id for the key that will be used for encryption (an e-mail address should do, or
a fingerprint or a key id).

Typical gnupg locations include:
    Win: C:\\Users\\<Name>\\AppData\\Roaming\\gnupg
    Linux: ~/.gnup g
Recipient example: Fingerprint, Key ID, e-mail (john@mail.com)
                '''
                )
        sys.exit(1)

    for o, a in optlist:
        if o in ('-h', '--help'): 
            usage()
            sys.exit()
        elif o in ('-e', '--encrypt'):
            encrypt(folders)
            sys.exit()
        elif o in ('-d', '--decrypt'):
            decrypt(folders)
            sys.exit()
        else:
            assert False, "unrecognized option"
    usage()
    sys.exit(1)

if __name__ == "__main__":
    main()
