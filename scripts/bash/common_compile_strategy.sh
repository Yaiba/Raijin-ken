# if configure exists in the directory
ls | grep 'configure$'

if [[ $? -eq 0 ]]
then
	# should just call configure
	./configure
else
	# you need to genreate th configure, which you should call 'autoconf' or 'autoreconf -i'
	autoreconf -i
	./configure
fi

make
make insatll
