# Integrating it withing VIM

For a more integrated approach, you can add the following mappings to your .vimrc

```
"cd to working dir of current file for the current window
nnoremap <leader>cd :lcd %:h<CR>

"Mapping for encrypting and decrypting files in wiki
nnoremap <Leader><Leader>e :! python crypt.py -e
nnoremap <Leader><Leader>d :! python crypt.py -d
```

This allows you to do the following sequence of commands to encrypt the 
folders you chose in the *.cryptfile*:

```
<Leader>ww - open wiki index
<Leader>cd - change Vim dir to wiki index
<Leader><Leader>e - encrypt folders
<Leader><Leader>d - decrypt folders
```
