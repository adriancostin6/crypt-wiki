# VimWiki setup

## Get Vim

This step should seem pretty obvious. Get it through your distro's package
manager or download it from [https://www.vim.org/](https://www.vim.org/).

# Plugin Manager

It's not required, but is definitely something you will want if you wanna live
the plugin life. You have multiple options here:

- [vim-plug](https://github.com/junegunn/vim-plug)
- [Vundle](https://github.com/VundleVim/Vundle.vim)
- [Pathogen](https://github.com/tpope/vim-pathogen)
- [dein vim](https://github.com/Shougo/dein.vim)
- [Volt](https://github.com/vim-volt/volt)

I'm sure there's more, so I won't bore you. Just google it and figure out
how to get it set up, then read the next section.

# Install the VimWiki plugin

For this section, I am going to be using *vim-plug* to showcase how to install
the plugin. The process is different for other plugin managers, so you will have
to reseach that on your own if you decide to use something else.


Add the following to your *.vimrc*:

```
call plug#begin('/path/to/plug/dir')
Plug 'vimwiki/vimwiki'
call plug#end()

let g:vimwiki_list = [{'path': '/path/to/wiki/folder',
                      \ 'syntax': 'markdown', 'ext': '.md'}]
```

As one can obviously tell, this specifies that we want to install *vimwiki* and
configure it to use *markdown* syntax with the *.md* extension. We alse specify
the folder where our wiki is stored, **this should be the same as the folder where you clone this repo**.

After adding this close and reopen Vim or run the Vim command `:source %` to apply the configuration.

To install the plugin run `:PlugInstall` Vim command.

After doing this, you should be able to use the plugin as specified in
[How to use VimWiki](Usage.md). Happy note-taking.

