# Install the VimWiki plugin

For this section, I am going to be using *vim-plug* to showcase how to install
the plugin. The process is different for other plugin managers, so you will have
to reseach that on your own if you decide to use something else.

Add the following to your *.vimrc*:

```
call plug#begin('/path/to/plug/dir')
Plug 'vimwiki/vimwiki'
call plug#end()

" Wiki settings
let wiki_default = {}
let wiki_default.auto_export = 0
let wiki_default.auto_toc = 0
let wiki_default.syntax = 'markdown'
let wiki_default.ext = '.md'
let wiki_default.nested_syntaxes = {'python': 'python', 'c++': 'cpp', 'sh': 'sh'}

let personal_wiki = copy(wiki_default)
let personal_wiki.path = '~/doc/crypt-wiki/personal/notes/'
let personal_wiki.diary_rel_path = 'diary/'
let personal_wiki.path_html = '~/doc/crypt-wiki/personal/exports/html/'

let gym_wiki = copy(wiki_default)
let gym_wiki.path = '~/doc/crypt-wiki/gym/notes/'
let gym_wiki.diary_rel_path = 'workouts/'
let gym_wiki.path_html = '~/doc/crypt-wiki/gym/exports/html/'

let work_wiki = copy(wiki_default)
let work_wiki.path = '~/doc/crypt-wiki/work/notes/'
let work_wiki.diary_rel_path = 'tracker/'
let work_wiki.path_html = '~/doc/crypt-wiki/work/exports/html/'

let phd_wiki = copy(wiki_default)
let phd_wiki.path = '~/doc/crypt-wiki/phd/notes/'
let phd_wiki.diary_rel_path = 'tracker/'
let phd_wiki.path_html = '~/doc/crypt-wiki/phd/exports/html/'

let g:vimwiki_list = [personal_wiki, gym_wiki, work_wiki, phd_wiki]
```

This setup creates multiple wikis and stores them inside the repository. Using this approach will
allow you to switch between wikis with <Leader>ws.
