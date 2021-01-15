[toc]

### file

```shell
# modify file atime
touch -a —date=“2017-12-12 01:01:01”  xxx

# modify file mtime
touch -m —date=“2017-12-12 01:01:01”  xxx

# compose json
cat << EOF > /tmp/example.json
[{"name": "yiyayiyayo"}]
EOF
```


### string

```shell
# get string range fields
echo {1..5} | cut -d ' ' -f -2
echo {1..5} | cut -d ' ' -f 2-4
```


### time

```shell
# get utc timestamp
date +%s
```


### search

```shell
# grep process
ps -ef | grep [n]ginx

# prevent grep return none 0 if not match，e.g. always return 0
echo aaaaa | grep bb || :
```


### check

```shell
# exeutable exist
command -v rg > /dev/null 2>&1;
type foo >/dev/null 2>&1
hash foo 2>/dev/null
```


### network

```shell
# simple speed test using netcat
## client side
timeout 10 yes|nc -vv -n ADDR 2222 > /dev/null  2>&1
## server side, when transmit is over, you get a result number n(byte),
## to get speed, (n*8/1024/1024)/10.0 （b/s）
nc  -nvv -l -p 2222 > /dev/null


# simple encrypted chat using nc, SuperSecretPWD is the symmetric key
## server
while IFS= read -r userinput;do echo "$userinput" | openssl enc -aes-256-ctr -a -A -k SuperSecretPWD;echo;done | nc -l 8877 | while IFS= read -r serveroutput;do echo "Incoming: $(echo "$serveroutput" | openssl enc -d -a -A -aes-256-ctr -k SuperSecretPWD)";done
## client
while IFS= read -r userinput;do echo "$userinput" | openssl enc -aes-256-ctr -a -A -k SuperSecretPWD;echo;done | nc localhost 8877 | while IFS= read -r serveroutput;do echo "Incoming: $(echo "$serveroutput" | openssl enc -d -a -A -aes-256-ctr -k SuperSecretPWD)";done


# encrypted chat using openssl
## server
openssl req -x509 -nodes -days 364 -newkey rsa:2096 -batch -keyout PrivateKey.key -out PublicCertificate.cert
openssl s_server -cert PublicCertificate.cert -key PrivateKey.key -accept 9876
## client
openssl s_client -connect 192.168.1.10:9876


# encrypted chat using ncat(from nmap) over tls
## server
openssl req -x509 -nodes -days 364 -newkey rsa:2096 -batch -keyout PrivateKey.key -out PublicCertificate.cert
ncat -vl 9876 --ssl --ssl-key PrivateKey.key --ssl-cert PublicCertificate.cert
## client
ncat -v --ssl 192.168.1.10 9876
## or
openssl s_client -connect 192.168.1.10:9876

```


### memory

```shell
# Free pagecache
sync; echo 1 > /proc/sys/vm/drop_caches

# Free dentries and inodes use following command
sync; echo 2 > /proc/sys/vm/drop_caches

# Free pagecache, dentries and inodes in cache memory
sync; echo 3 > /proc/sys/vm/drop_caches
```


### strace

Learn REF http://www.brendangregg.com/blog/2014-05-11/strace-wow-much-syscall.html

```shell
# Slow the target command and print details for each syscall:
strace command
# Slow the target PID and print details for each syscall:
strace -p PID
# Slow the target PID and any newly created child process, printing syscall details:
strace -fp PID
# Slow the target PID and record syscalls, printing a summary:
strace -cp PID
# Slow the target PID and print open() syscalls only:
strace -eopen -p PID
# Slow the target PID and print open() and stat() syscalls only:
strace -eopen,stat -p PID
# Slow the target PID and print connect() and accept() syscalls only:
strace -econnect,accept -p PID
# Slow the target command and see what other programs it launches (slow them too!):
strace -qfeexecve command
# Slow the target PID and print time-since-epoch with (distorted) microsecond resolution:
strace -ttt -p PID
# Slow the target PID and print syscall durations with (distorted) microsecond resolution:
strace -T -p PID
```

最好用 更新的工具， perf_events/ktap/SystemTap/LTTng/dtrace4linux
Strace 可以破解文本、严重拖慢目标线程(可能导致有误导性的输出)，只能用于看system call用




### hardware

lshw, https://ezix.org/project/wiki/HardwareLiSter



### storage


#### hardware

```shell
# show disk spec
sudo hdparm -I /dev/sda
sudo lshw -class disk -class storage

# turn on disk cache
hdparm -W1 /dev/sda
# turn off disk cache
hdparm -W0 /dev/sda

```


#### partition/format/mount

```shell
# first unmount
sudo umount /dev/sdd2
# if above failed
sudo umount -l /mnt/xxx

# partition
sudo parted /dev/sdd mklabel gpt
sudo parted /dev/sdd mkpart primary ext4 0% 100%
sudo partprobe /dev/sdd

# format
sudo mkfs.ext4 /dev/sdd1

# mount
sudo mkdir -p /mnt/data1 
sudo mount /dev/sdd1 /mnt/data1

# write to /etc/fstab
echo '/dev/sdd1 /mnt/data1 ext4 defaults 0 0' >> /etc/fstab
```

注：NTFS在linux下是以fuse的方式在运行，性能损耗很高



#### dd

flags:
• direct (use direct I/O for data)
• dsync (use synchronized I/O for data)
• sync (likewise, but also for metadata)


```shell
# 可以分别关闭、开启磁盘缓存看效果
# 测试throughput(straming I/O)，这个参数需要内存有1G可用
dd if=/dev/zero of=/tmp/dd1G bs=1G count=1 oflag=direct

# 测试latency， time/count
dd if=/dev/zero of=/tmp/dd1G_latency bs=512k count=2048 oflag=direct

# sync; echo 3 > /proc/sys/vm/drop_caches   清空缓存
# 测试读
dd if=/tmp/dd1G_latency of=/dev/null bs=512k count=2048
```
