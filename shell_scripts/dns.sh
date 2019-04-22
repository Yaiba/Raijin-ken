#!/bin/sh

dns () {
	if [[ $# -ne 3 ]]
  then
		warn "Usage: dns set/remove [ip] [host]"
		return $RETURN_CODE_NOT_ENOUGH_PARAMETER
  fi
	COMMAND=$1
	IP=$2
	HOST=$3
	command_${COMMAND}_dns $IP $HOST
}

command_set_dns () {
}

command_remove_dns () {
}
