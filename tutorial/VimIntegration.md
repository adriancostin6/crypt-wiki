# Integrating it withing VIM

## Step 1 - Setup

Copy the **crypt.vim** file from the repository to your `~/.vim/plugin` folder
if you are on Linux, or inside '~/vimfiles/plugin` if you are on Windows.

The plugin file can be found under **plugin/crypt.vim**.

## Step 2 - Mappings

Add the following to your .vimrc: 

```
"Mapping for encrypting and decrypting files in wiki
nnoremap <Leader><Leader>e :call Crypt()<CR>
runtime crypt.vim
```

## Step 3 - Enjoy

After that, just use: `<Leader><Leader>e` to encrypt/decrypt your Wiki
as specified inside the .cryptfile.
