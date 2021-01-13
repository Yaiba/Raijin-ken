[toc]


### config

```shell
# proxy
git config --global https.proxy http://127.0.0.1:1080
git config --global --unset http.proxy

git config --global https.proxy https://127.0.0.1:1080
git config --global --unset https.proxy

git config --global http.https://github.com.proxy socks5://127.0.0.1:1080
git config --global --unset http.https://github.com.proxy)
```

### commit

```shell
# update author date while amend
git commit --amend --date="$(date -R)" -m

```
