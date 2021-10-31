# Backstory

Storing sensitive notes on version control platforms such as GitHub and GitLab
seemed like a dumb idea at first, because I wouldn't trust them with such data,
not even in a private repository.

This got me thinking about a way of encrypting the sensitive information in
certain notes before pushing to version control, while leaving the non-sensitive
ones in plain text.

After searching available options on the interweb I stumbled upon solutions such
as [git-crypt](https://github.com/AGWA/git-crypt) (didn't fit my needs as I could not compile it and get it to work
on windows for the life of me) and [vim-gnupg](https://github.com/jamessan/vim-gnupg) which I honestly didn't bother trying
because I wanted more of a command line approach as opposed to a Vim plugin experience.

Seeing that I could not find a solution that fit my fancy, I decided to write my
own, ironically in the form of a python script (haven't used python in a while).
The script basically makes use of a already configured GPG key, to encrypt the
directories you list in the .cryptfile. What you end up with is a simple 2 step
workflow for pushing encrypted and plain text notes to version control.

What can I say:

![It's not much, but it's honest work.](https://i.kym-cdn.com/entries/icons/original/000/028/021/work.jpg)
