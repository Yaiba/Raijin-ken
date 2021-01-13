[toc]

### sshconfig
file: ~/.ssh/config


```ini
# reuse ssh connection
# https://puppet.com/blog/speed-up-ssh-by-reusing-connections

Host *
# every 300s send an alive msg, to prevent server disconnet u
ServerAliveInterval 300
ControlPath ~/.ssh/sockets/%r@%h-%p
ControlMaster auto
# stay alive for 600s
ControlPersist 600
```


### login notify

```shell
#/bin/sh
# #######################################
# pam REF: https://askubuntu.com/a/448602
# copy to /etc/ssh, then +x
# add "session optional pam_exec.so type=open_session seteuid /etc/ssh/ubuntu_ssh_login_slack_notify" to /etc/pam.d/sshd
# work on Ubuntu 14.04.5

#echo "User: $PAM_USER" >> /tmp/a.txt
#echo "Ruser: $PAM_RUSER" >> /tmp/a.txt
#echo "Rhost: $PAM_RHOST" >> /tmp/a.txt
#echo "Service: $PAM_SERVICE" >> /tmp/a.txt
#echo "TTY: $PAM_TTY" >> /tmp/a.txt
#echo "Date: `date`" >> /tmp/a.txt
#echo "Server: `uname -a`" >> /tmp/a.txt
#echo >> /tmp/a.txt

host=`hostname`
now=$(date '+%Y-%m-%d %H:%M:%S %Z')
ip=`hostname -I | cut -d " " -f 1`
slack_url="YOUR_SLACK_API"
content='{"text":"'"$PAM_USER"' from '"$PAM_RHOST"' on '"${host}-${ip}"' through '"${PAM_SERVICE}-${PAM_TTY}"' at '"$now"'"}'
curl -X POST -H 'Content-type: application/json' -d "$content" $slack_url
```
