#!/bin/sh

recursive_sed_replace () {
    echo "do recursive sed replace : $1  -->  $2"
    echo "WARN: only works if current diretory depth is 3"
    if [ $OS_X ]; then
        find . -path ./.git -prune -o -type f -print0 | xargs -0 sed -i '' "s/$1/$2/g"
    else
        find . -path ./.git -prune -o -type f -print0 | xargs -0 sed -i "s/$1/$2/g"
    fi
}
