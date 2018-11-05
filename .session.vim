let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
imap <ú> ú
imap <ù> ù
imap <ø> ø
imap <÷> ÷
imap <ö> ö
imap <õ> õ
imap <ô> ô
imap <ó> ó
imap <ò> ò
imap <ñ> ñ
imap <ð> ð
imap <ï> ï
imap <î> î
imap <í> í
imap <ì> ì
imap <ë> ë
imap <ê> ê
imap <é> é
imap <è> è
imap <ç> ç
imap <æ> æ
imap <å> å
imap <ä> ä
imap <ã> ã
imap <â> â
imap <á> á
nnoremap d :call NotTmuxReminder()
nnoremap <Right> :call NotTmuxReminder()
nnoremap <Up> :call NotTmuxReminder()
nnoremap <Down> :call NotTmuxReminder()
nnoremap <Left> :call NotTmuxReminder()
nnoremap l :call NotTmuxReminder()
nnoremap k :call NotTmuxReminder()
nnoremap j :call NotTmuxReminder()
nnoremap h :call NotTmuxReminder()
vnoremap  :w ! xsel -ib<Home>silent <End>
noremap  :earlier
noremap  :tabprevious
noremap <NL> }
noremap  {
noremap  :tabnext
map  :NERDTreeToggle
vnoremap  :w! /tmp/vim_infile_bash'>:r! sh /tmp/vim_infile_bash'<V'>"_d
noremap  :UndotreeToggle
noremap v :vsplit .
noremap  :vsplit .
noremap h :split .
noremap  :split .
noremap  :later
vnoremap  t :Tabularize /
nmap  , :InteractiveWindow
nnoremap  t mn:tabe %'n
noremap  p VyP
noremap  z zz
noremap  * :noh
noremap  = mnggVG='n
noremap  f :find %:p:h
vnoremap  s :s///g<Left><Left>
nnoremap  s :%s///g<Left><Left>
noremap  J <Down>
noremap  K <Up>
noremap  L <Right>
noremap  H <Left>
noremap  r :source .session.vim
noremap  e :mksession! .session.vim
vnoremap  d "_d
nnoremap  d "_d
nnoremap  q :q
nnoremap  w :w
noremap ! :!
vnoremap * "ny:set hlsearch:let @/ = @n
nnoremap * mkHml`k*`lzt`k
onoremap * mkHml`k*`lzt`k
noremap + $
inoremap ë :m .-2==gi
inoremap ê :m .+1==gi
vnoremap P "_dP
vnoremap Q '>me'<msV"by0qx
xmap S <Plug>VSurround
nnoremap T :tabe %:p:h
vnoremap T :tabe .
onoremap T :tabe .
nmap cS <Plug>CSurround
nmap cs <Plug>Csurround
nmap ds <Plug>Dsurround
vmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
xmap gS <Plug>VgSurround
vnoremap p "_dp
nmap ySS <Plug>YSsurround
nmap ySs <Plug>YSsurround
nmap yss <Plug>Yssurround
nmap yS <Plug>YSurround
nmap ys <Plug>Ysurround
noremap zxcx :q
nnoremap <SNR>90_: :=v:count ? v:count : ''
vnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(expand((exists("g:netrw_gx")? g:netrw_gx : '<cfile>')),netrw#CheckIfRemote())
nnoremap <silent> <Plug>SurroundRepeat .
nnoremap <F3> :CycleColorPrev
nnoremap <F4> :CycleColorNext
nnoremap <silent> <Plug>GitGutterPreviewHunk :GitGutterPreviewHunk
nnoremap <silent> <Plug>GitGutterUndoHunk :GitGutterUndoHunk
nnoremap <silent> <Plug>GitGutterStageHunk :GitGutterStageHunk
nnoremap <silent> <expr> <Plug>GitGutterPrevHunk &diff ? '[c' : ":\execute v:count1 . 'GitGutterPrevHunk'\"
nnoremap <silent> <expr> <Plug>GitGutterNextHunk &diff ? ']c' : ":\execute v:count1 . 'GitGutterNextHunk'\"
xnoremap <silent> <Plug>GitGutterTextObjectOuterVisual :call gitgutter#hunk#text_object(0)
xnoremap <silent> <Plug>GitGutterTextObjectInnerVisual :call gitgutter#hunk#text_object(1)
onoremap <silent> <Plug>GitGutterTextObjectOuterPending :call gitgutter#hunk#text_object(0)
onoremap <silent> <Plug>GitGutterTextObjectInnerPending :call gitgutter#hunk#text_object(1)
noremap <C-Down> }
noremap <C-Up> {
noremap <Down> <Nop>
inoremap  
imap S <Plug>ISurround
imap s <Plug>Isurround
imap  <Plug>Isurround
nnoremap è :GitGutterPrevHunkzz
nnoremap ì :GitGutterNextHunkzz
vnoremap ë :m '<-2gv=gv
vnoremap ê :m '>+1gv=gv
nnoremap ë :m .-2==
nnoremap ê :m .+1==
noremap æ }
noremap ø {
cnoremap w!! w !sudo tee > /dev/null %
cnoreabbr undotree UndotreeToggle
cnoreabbr utree UndotreeToggle
cnoreabbr ss %s
cnoreabbr reload source ~/.vimrc
cnoreabbr Tabe tabe
cnoreabbr Qq qa
cnoreabbr qq qa
cnoreabbr WQ wq
cnoreabbr Wq wq
cnoreabbr Q q
cnoreabbr W w
let &cpo=s:cpo_save
unlet s:cpo_save
set autoindent
set background=dark
set backspace=indent,eol,start
set clipboard=unnamedplus
set fileencodings=ucs-bom,utf-8,default,latin1
set foldlevelstart=20
set guioptions=aegit
set helplang=en
set hlsearch
set incsearch
set laststatus=2
set mouse=a
set printoptions=paper:a4
set ruler
set runtimepath=~/.vim,~/.vim/bundle/Vundle.vim,~/.vim/bundle/vim-airline,~/.vim/bundle/vim-airline-themes,~/.vim/bundle/nerdtree,~/.vim/bundle/vim-gitgutter,~/.vim/bundle/vim-fugitive,~/.vim/bundle/undotree,~/.vim/bundle/simpylfold,~/.vim/bundle/vim-colorschemes,~/.vim/bundle/CycleColor,~/.vim/bundle/vim-surround,~/.vim/bundle/winteract.vim,~/.vim/bundle/tabular,~/.vim/bundle/gruvbox,~/.vim/bundle/vim-colors-plain,~/.vim/bundle/vim-sublime-monokai,/var/lib/vim/addons,/usr/share/vim/vimfiles,/usr/share/vim/vim80,/usr/share/vim/vimfiles/after,/var/lib/vim/addons/after,~/.vim/after,~/.vim/bundle/Vundle.vim,~/.vim/bundle/Vundle.vim/after,~/.vim/bundle/vim-airline/after,~/.vim/bundle/vim-airline-themes/after,~/.vim/bundle/nerdtree/after,~/.vim/bundle/vim-gitgutter/after,~/.vim/bundle/vim-fugitive/after,~/.vim/bundle/undotree/after,~/.vim/bundle/simpylfold/after,~/.vim/bundle/vim-colorschemes/after,~/.vim/bundle/CycleColor/after,~/.vim/bundle/vim-surround/after,~/.vim/bundle/winteract.vim/after,~/.vim/bundle/tabular/after,~/.vim/bundle/gruvbox/after,~/.vim/bundle/vim-colors-plain/after,~/.vim/bundle/vim-sublime-monokai/after
set shiftwidth=4
set softtabstop=4
set splitbelow
set splitright
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set tabstop=4
set ttimeoutlen=50
set wildignore=*.pyc
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/Repos/DinoTerminalGame
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +0 game_engine.py
badd +8 main.py
badd +1 .
argglobal
silent! argdel *
$argadd game_engine.py
edit game_engine.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd t
set winminheight=1 winheight=1 winminwidth=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 102 + 103) / 206)
exe 'vert 2resize ' . ((&columns * 103 + 103) / 206)
argglobal
let s:cpo_save=&cpo
set cpo&vim
nmap <buffer>  hp <Plug>GitGutterPreviewHunk
nmap <buffer>  hu <Plug>GitGutterUndoHunk
nmap <buffer>  hs <Plug>GitGutterStageHunk
nmap <buffer> [c <Plug>GitGutterPrevHunk
nmap <buffer> ]c <Plug>GitGutterNextHunk
xmap <buffer> ac <Plug>GitGutterTextObjectOuterVisual
omap <buffer> ac <Plug>GitGutterTextObjectOuterPending
xmap <buffer> ic <Plug>GitGutterTextObjectInnerVisual
omap <buffer> ic <Plug>GitGutterTextObjectInnerPending
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=b:#,fb:-
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=SimpylFold#FoldExpr(v:lnum)
setlocal foldignore=#
setlocal foldlevel=20
setlocal foldmarker={{{,}}}
set foldmethod=syntax
setlocal foldmethod=expr
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(v:fname,'\\.','/','g')
setlocal indentexpr=GetPythonIndent(v:lnum)
setlocal indentkeys=0{,0},:,!^F,o,O,e,<:>,=elif,=except
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=pydoc
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
setlocal nonumber
setlocal numberwidth=4
setlocal omnifunc=python3complete#Complete
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=4
setlocal noshortname
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=%!airline#statusline(1)
setlocal suffixesadd=.py
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=8
setlocal tagcase=
setlocal tags=
setlocal termkey=
setlocal termsize=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal nowinfixheight
setlocal nowinfixwidth
set nowrap
setlocal nowrap
setlocal wrapmargin=0
5
normal! zo
20
normal! zo
28
normal! zo
let s:l = 22 - ((21 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
22
normal! 016|
wincmd w
argglobal
if bufexists('main.py') | buffer main.py | else | edit main.py | endif
let s:cpo_save=&cpo
set cpo&vim
nmap <buffer>  hp <Plug>GitGutterPreviewHunk
nmap <buffer>  hu <Plug>GitGutterUndoHunk
nmap <buffer>  hs <Plug>GitGutterStageHunk
nmap <buffer> [c <Plug>GitGutterPrevHunk
nmap <buffer> ]c <Plug>GitGutterNextHunk
xmap <buffer> ac <Plug>GitGutterTextObjectOuterVisual
omap <buffer> ac <Plug>GitGutterTextObjectOuterPending
xmap <buffer> ic <Plug>GitGutterTextObjectInnerVisual
omap <buffer> ic <Plug>GitGutterTextObjectInnerPending
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=b:#,fb:-
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=SimpylFold#FoldExpr(v:lnum)
setlocal foldignore=#
setlocal foldlevel=20
setlocal foldmarker={{{,}}}
set foldmethod=syntax
setlocal foldmethod=expr
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(v:fname,'\\.','/','g')
setlocal indentexpr=GetPythonIndent(v:lnum)
setlocal indentkeys=0{,0},:,!^F,o,O,e,<:>,=elif,=except
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=pydoc
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
setlocal nonumber
setlocal numberwidth=4
setlocal omnifunc=python3complete#Complete
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=4
setlocal noshortname
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=%!airline#statusline(2)
setlocal suffixesadd=.py
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=8
setlocal tagcase=
setlocal tags=
setlocal termkey=
setlocal termsize=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal nowinfixheight
setlocal nowinfixwidth
set nowrap
setlocal nowrap
setlocal wrapmargin=0
let s:l = 8 - ((7 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
8
normal! 013|
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 102 + 103) / 206)
exe 'vert 2resize ' . ((&columns * 103 + 103) / 206)
tabnext 1
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToO
set winminheight=1 winminwidth=1
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
