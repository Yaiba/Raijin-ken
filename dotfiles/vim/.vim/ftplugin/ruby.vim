" File ftplugin/ruby.vim
" Ruby specific settings.
" see also: http://vim.wikia.com/wiki/Keep_your_vimrc_file_clean

setlocal tabstop=2
setlocal shiftwidth=2
setlocal softtabstop=2
setlocal expandtab
setlocal autoindent

autocmd BufWritePre * :%s/\s\+$//e
