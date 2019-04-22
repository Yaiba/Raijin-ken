" File ftplugin/clojure.vim
" Clojure specific settings.
" see also: http://vim.wikia.com/wiki/Keep_your_vimrc_file_clean

setlocal tabstop=4
setlocal shiftwidth=4
setlocal softtabstop=4
setlocal expandtab
setlocal autoindent

nmap <c-c><c-k> :Require<cr>
let g:clojure_fuzzy_indent = 1
let g:clojure_fuzzy_indent_patterns = ['^with', '^def', '^let']
au BufWritePre * :%s/\s\+$//e
