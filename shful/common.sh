#!/bin/sh

RETURN_CODE_NOT_ENOUGH_PARAMETER=1

if [[ $(uname) == 'Linux' ]]
then
    OS_X=0  # linux
else
    OS_X=1  # mac
fi

# if item in arrary
has () {
        local item=$1; shift
        echo $@ | grep -wq $item
        }

# tput Color Capabilities:
#
# tput setab [1-7] – Set a background color using ANSI escape
# tput setb [1-7] – Set a background color
# tput setaf [1-7] – Set a foreground color using ANSI escape
# tput setf [1-7] – Set a foreground color
# 
# tput Text Mode Capabilities:
# 
# tput bold – Set bold mode
# tput dim – turn on half-bright mode
# tput smul – begin underline mode
# tput rmul – exit underline mode
# tput rev – Turn on reverse mode
# tput smso – Enter standout mode (bold on rxvt)
# tput rmso – Exit standout mode
# tput sgr0 – Turn off all attributes
# 
# Color Code for tput:
# 0 – Black
# 1 – Red
# 2 – Green
# 3 – Yellow
# 4 – Blue
# 5 – Magenta
# 6 – Cyan
# 7 – White

red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
white=`tput setaf 7`

warn () {
    echo -e "${red} $@${white}"
}

ok () {
    echo -e "${green} $@${white}"
}

info () {
    echo -e "${white} $@"
}

notice () {
    echo -e "${yellow} $@${white}"
}

die () {
    warn "$@"; return 0;
}

# simple string matching
startswith () { [ "$1" != "${1#$2}" ]; }
endswith () { [ "$1" != "${1%$2}" ]; }

# simple string split
str_split() {
	if [[ $# -ne 2 ]]
	then
		warn "Usage: str_split target_string delimiter"
		return $RETURN_CODE_NOT_ENOUGH_PARAMETER
	fi
	s=$1
	delimiter=$2
	# could Parameter Expansion to an array
	arr=(${s//$delimiter/ })
	echo "(${arr[@]})"
}

str_split_index() {
	if [[ $# -ne 3 ]]
	then
		warn "Usage: str_split_index target_string delimiter index"
		return $RETURN_CODE_NOT_ENOUGH_PARAMETER
	fi
	s=$1
	delimiter=$2
	# could Parameter Expansion to an array
	#arr=(${s//$delimiter/ })
	index=$3
	echo $(echo "$s" | cut -d "$delimiter" -f $index)
}

# check a program/command exist   https://stackoverflow.com/a/677212
#command -v foo >/dev/null 2>&1 || { echo >&2 "I require foo but it's not installed.  Aborting."; }
#type foo >/dev/null 2>&1 || { echo >&2 "I require foo but it's not installed.  Aborting."; }
#hash foo 2>/dev/null || { echo >&2 "I require foo but it's not installed.  Aborting."; }
