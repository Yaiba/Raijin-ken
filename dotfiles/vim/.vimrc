" File ~/.vimrc
" Global settings for all files (but may be overridden in ftplugin).
" for some help, try :help XX
"
set shell=/bin/bash
let mapleader=";"
" don't need any help!
inoremap <F1> <nop>
nnoremap <F1> <nop>
vnoremap <F1> <nop>

" use junegunn/vim-plug as plugin manager
" Automatic installation
if empty(glob('~/.vim/autoload/plug.vim'))
    silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
        \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
    autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif
call plug#begin('~/.vim/plugged')

" enable vim help for vim-plug itself, :help plug-options
Plug 'junegunn/vim-plug'

" fzf   fuzzy finder
" install use fzf
"Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
" installed using Homebrew
Plug '/usr/local/opt/fzf'
Plug 'junegunn/fzf.vim'
" [Buffers] Jump to the existing window if possible
let g:fzf_command_prefix = 'Fzf'
let g:fzf_buffers_jump = 1
map \ :FzfFiles<cr>
" Command for git grep
" - fzf#vim#grep(command, with_column, [options], [fullscreen])
command! -bang -nargs=* GGrep
  \ call fzf#vim#grep(
  \   'git grep --line-number '.shellescape(<q-args>), 0,
  \   { 'dir': systemlist('git rev-parse --show-toplevel')[0] }, <bang>0)
" with ripgrep
let g:rg_command = '
  \ rg --column --line-number --no-heading --fixed-strings --ignore-case --no-ignore --hidden --follow --color "always"
  \ -g "*.{js,json,php,md,styl,jade,html,config,py,cpp,c,go,hs,rb,conf}"
  \ -g "!{.git,node_modules,vendor}/*" '
" search with provide arg
command! -bang -nargs=* Rg call fzf#vim#grep(g:rg_command .shellescape(<q-args>).'| tr -d "\017"', 1, <bang>0)
" search with word under the cursor
command! -bang -nargs=* RG call fzf#vim#grep(g:rg_command .shellescape(expand('<cword>')).'| tr -d "\017"', 1, <bang>0)

" directory tree
Plug 'scrooloose/nerdtree'
  map <F1> :NERDTreeToggle<cr>:set rnu<cr>
  let NERDTreeShowBookmarks=1
  let NERDTreeShowFiles=1
  let NERDTreeShowHidden=1
  let NERDTreeShowLineNumbers=1
  let NERDTreeWinPos=0
  let NERDTreeAutoCenter=1
  let NERDTreeHighLightCursorline=1

" git support for nerdtree
Plug 'Xuyuanp/nerdtree-git-plugin'

" Loaded when clojure file is opened
Plug 'tpope/vim-fireplace', { 'for': 'clojure' }

Plug 'vim-scripts/Tagbar'
  map <silent>  <F2>  :Tagbar<cr>
  let g:tagbar_ctags_bin="/usr/local/bin/ctags"

Plug 'vim-scripts/ShowTrailingWhitespace'

" :h bufferline
Plug 'bling/vim-bufferline'
" automatically echo to command bar
let g:bufferline_echo=1

" just gitbranch
Plug 'itchyny/vim-gitbranch'

" lightline
Plug 'itchyny/lightline.vim'
  if !has('gui_running')
      set t_Co=256
  endif
  " anytime have question, try `:h g:lightline.KEY`
  let g:lightline = {
      \ 'colorscheme': 'seoul256',
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ],
      \             [ 'gitbranch', 'readonly', 'filename', 'modified' ] ],
      \   'right': [ [ 'lineinfo' ],
      \              [ 'percent' ],
      \              [ 'fileformat', 'fileencoding', 'filetype', ],
      \              [ 'linter_warnings', 'linter_errors', 'linter_ok', ] ]
      \ },
      \ 'tabline': {
      \   'left': [ [ 'tabs' ], [ 'bufferline' ] ],
      \   'right': [ [ 'close' ] ],
      \ },
      \ 'component': {
      \   'nothing': 'nothing',
      \ },
      \ 'component_function': {
      \   'gitbranch': 'gitbranch#name',
      \   'bufferline': 'LightlineBufferline',
      \ },
      \ 'component_type': {
      \   'linter_warnings': 'warning',
      \   'linter_errors': 'error'
      \ },
      \ 'component_expand': {
      \   'linter_warnings': 'LightlineLinterWarnings',
      \   'linter_errors': 'LightlineLinterErrors',
      \   'linter_ok': 'LightlineLinterOK'
      \ },
      \}
  let g:lightline.separator = {
    \   'left': '', 'right': ''
    \}
  let g:lightline.subseparator = {
    \   'left': '', 'right': ''
    \}
  function! LightlineBufferline()
    call bufferline#refresh_status()
    let b = g:bufferline_status_info.before
    let c = g:bufferline_status_info.current
    let a = g:bufferline_status_info.after
    let alen = strlen(a)
    let blen = strlen(b)
    let clen = strlen(c)
    let w = winwidth(0) * 4 / 11
    if w < alen+blen+clen
        let whalf = (w - strlen(c)) / 2
        let aa = alen > whalf && blen > whalf ? a[:whalf] : alen + blen < w - clen || alen < whalf ? a : a[:(w - clen - blen)]
        let bb = alen > whalf && blen > whalf ? b[-(whalf):] : alen + blen < w - clen || blen < whalf ? b : b[-(w - clen - alen):]
        return (strlen(bb) < strlen(b) ? '...' : '') . bb . c . aa . (strlen(aa) < strlen(a) ? '...' : '')
    else
        return b . c . a
    endif
  endfunction
  function! LightlineLinterErrors() abort
    let l:counts = ale#statusline#Count(bufnr(''))
    let l:all_errors = l:counts.error + l:counts.style_error
    let l:all_non_errors = l:counts.total - l:all_errors
    return l:counts.total == 0 ? '' : printf('%d ✗', all_errors)
  endfunction
  function! LightlineLinterWarnings() abort
    let l:counts = ale#statusline#Count(bufnr(''))
    let l:all_errors = l:counts.error + l:counts.style_error
    let l:all_non_errors = l:counts.total - l:all_errors
    return l:counts.total == 0 ? '' : printf('%d ◆', all_non_errors)
  endfunction
  function! LightlineLinterOK() abort
    let l:counts = ale#statusline#Count(bufnr(''))
    let l:all_errors = l:counts.error + l:counts.style_error
    let l:all_non_errors = l:counts.total - l:all_errors
    return l:counts.total == 0 ? '✓ ' : ''
  endfunction
  autocmd User ALELint call lightline#update()
  " always show tabline
  set showtabline=2

Plug 'edkolev/tmuxline.vim'

Plug 'airblade/vim-gitgutter'

Plug 'w0rp/ale'
let g:ale_sign_column_always = 1
let g:ale_sign_error = '✗'
let g:ale_sign_warning = '⚡'
"let g:ale_echo_msg_error_str = 'E'
"let g:ale_echo_msg_warning_str = 'W'
nmap ]e :ALENextWrap<cr>
nmap [e :ALEPreviousWrap<cr>
nmap <Leader>f <Plug>(ale_fix)
nmap <Leader>l :ALEToggleBuffer<CR>
nmap <Leader>d :ALEDetail<CR>
let g:ale_linters = {
    \ 'json': ['fixjson'],
    \ 'python': ['flake8', 'pylint',],
    \ }
let g:ale_fixers = {
    \ 'python': ['autopep8',],
    \ }

" All of your Plugins must be added before the following line
call plug#end()
" Put your non-Plugin stuff after this line
" --------------------------------------------------------------

set laststatus=2 " Always display the statusline in all windows
set guifont=Inconsolata\ for\ Powerline:h14
set noshowmode " Hide the default mode text (e.g. -- INSERT -- below the statusline)
" set powerline done
" -------------------------------------------------------------

" Grey code when line characters exceed 79
augroup indicate_exceed
    autocmd!
    " highlight characters past column 79
    autocmd FileType * highlight Excess ctermbg=DarkGrey guibg=Black
    autocmd FileType * match Excess /\%79v.*/
    autocmd FileType * set nowrap
augroup END

" CORE SETTING
filetype plugin indent on  " required
syntax on
"set background=dark          "solarized
"set colorcolumn=79           "彩色显示第79列
"set cursorline               "设置光标行高亮显示
"set cursorcolumn             "光标垂直高亮
set ttyfast
set ruler
"set backspace=indent,eol,start
set fileencodings=utf-8,ucs-bom,cp936,gb18030,big5,euc-jp,eur-kr,latin1
set fenc=utf-8
" This allows buffers to be hidden if you've modified a buffer
set hidden
set encoding=utf-8
set laststatus=2
set number
"set relativenumber
set ignorecase      "大小写敏感，聪明感知（小写全搜，大写完全匹配）
set smartcase
set incsearch
set showmatch
set hlsearch
set foldmethod=manual          "代码折叠
set foldlevel=99
set numberwidth=4   "行号宽度
set expandtab
set tabstop=8
set shiftwidth=2
set softtabstop=2
set autoindent
set modeline
set backspace=indent,eol,start " backspace over everything in insert mode
" ctags, ptags
set tags=./tags;/
" ----------------------------------------------------------------------

" all maps
" for buffer nav
nnoremap <leader>l :bnext<cr>
nnoremap <leader>h :bprevious<cr>
nnoremap <leader>d :bdelete<cr>
" execute ctags
nmap <silent> <F8> :!ctags -R --python-kinds=-i --fields=+iaS --extra=+q .<CR>
" make search result int the middle
nnoremap n nzz
nnoremap N Nzz
"insert mode cursor move
inoremap <c-j> <down>
inoremap <c-k> <up>
inoremap <c-l> <right>
inoremap <c-h> <left>
" no high light
nnoremap <leader><space> :noh<cr>
" paste mode
"nmap <leader>p :set paste<cr>
"nmap <leader>P :set nopaste<cr>
set pastetoggle=<F3>
"nmap <leader>t :!pytags <cr>

"for tags jumping
" for jump tag to right new window
set splitright
nnoremap <c-w><c-[> :vsp<cr>:exec("tj ".expand("<cword>"))<cr>
nnoremap <c-]> g<c-]>
vnoremap <c-]> g<c-]>
" ---------------------------------------------------------------------------

" languange template
if has("autocmd")
  augroup templates
    " read in template file
    " BufNewFile . = each time we edit a new file
    " silent! execute = execute silently, ignore errors if no template exists
    " 0r = read file and insert content at top (0) in the new file
    " expand(":e") = get extension of current filename
    " see also http://vim.wikia.com/wiki/Use_eval_to_create_dynamic_templates
    autocmd BufNewFile *.* silent! execute '0r ~/.vim/templates/tpl.'.expand("<afile>:e")
    " replace content
    autocmd BufNewFile * %substitute#\[:VIM_EVAL:\]\(.\{-\}\)\[:END_EVAL:\]#\=eval(submatch(1))#ge
  augroup END
endif

command! TODO noautocmd vimgrep /TODO\|FIXME\|XXX/j ** | cw
command! TODOS noautocmd vimgrep /TODO\|FIXME\|XXX\|NOTE/j ** | cw

" auto trim trailing space when save
"autocmd BufWritePre * :%s/\s\+$//e
