#!/usr/bin/env bash
set -e

RETURN_CODE_NOT_ENOUGH_PARAMETER=11
RETURN_CODE_DIRECOTYR_NOT_EXISTS=12
HOME_DIR=~

usage () {
  #info $(printf '+%.0s' {1..30})
  echo "Usage: $0 use/update target"
  echo
  exit $RETURN_CODE_NOT_ENOUGH_PARAMETER
}

if [[ $# -ne 2 ]]
then
  usage
fi

action=$1
target=$2

use () {
  backup_dir=${HOME_DIR}/${target}-$(date +%y%m%d%H%M%S)
  if [[ $DEBUG -eq 1 ]]
  then
    echo "backup old $target: mv ${HOME_DIR}/.${target}* ${backup_dir}"
    echo "setup new $target : link $target/* to ${HOME_DIR}/${target}/*"
  else
    mkdir $backup_dir
    mv ${HOME_DIR}/.${target}* ${backup_dir}/
    for item in `ls -A ./$target`
    do
      echo "ln -i -s $(pwd)/$target/$item $HOME_DIR/$item"
      ln -i -s $(pwd)/$target/$item $HOME_DIR/$item
    done
  fi
}

update_vim () {
  if [[ $DEBUG -eq 1 ]]
  then
    echo "cp $HOME_DIR/.vimrc ./$target/"
    echo "cp -rf ${HOME_DIR}/.vim/{ftdetect,ftplugin,templates} ./$target/.vim/"
  else
    cp $HOME_DIR/.vimrc ./$target/
    cp -rf ${HOME_DIR}/.vim/{ftdetect,ftplugin,templates} ./$target/.vim/
  fi
}

update_tmux () {
  if [[ $DEBUG -eq 1 ]]
  then
    echo "cp $HOME_DIR/.tmux*.conf ./$target/"
  else
    cp $HOME_DIR/.tmux*.conf ./$target/
  fi
}

if [[ -d "./$target" ]]
then
  test $action = "use" && $action || ${action}_${target}
else
  echo "directory '$target' does not exists"
  exit $RETURN_CODE_DIRECOTYR_NOT_EXISTS
fi
