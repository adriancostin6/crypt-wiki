## How To Encrypt before version control

Encryption/Decryption is done using a python script, prior to version control.

## Benefits

- Hide sensitive information
- Keep stuff that isn't important unencrypted
- Simple, 2 step process
    - Encrypt/Decrypt with python script
    - Add, commit and push

## Automating everything?

Just run *pull/push-notes* for your operating system (batch or shell).

## Like it the manual way? I got you.

### How to encrypt/decrypt from the terminal

- Create .cryptfile (see help section)
- To encrypt, run `python crypt.py -e`
- To decrypt, run `python crypt.py -d`

#### Stop IT. Get some help

Run: `python crypt.py -h` or `python crypt.py --help`

### How to version control

- Add files: `git add .`
- Commit files: `git commit`
- Push to remote repos: `git push`
