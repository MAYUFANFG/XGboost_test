![Git_command](https://github.com/MAYUFANFG/XGboost_test/blob/main/Git_command.png)
### 情境1
在電腦本機創建倉庫->資料放到github上
###### 1.電腦本機初始化設定
```
git init
```
###### 2.在github上創建一個倉庫
###### 3.添加一個新的遠端倉庫
```
git remote add origin 遠端倉庫網址(https://github.com/username/repository.git)
```
###### 4.確認遠端倉庫已經被正確添加到電腦本機
```
git remote -v
```
###### 5.將(原有的)電腦本機資料推送到github
```
git push -u origin master(分支名)
```
###### 5-1 若發現  ```error: failed to push some refs to 'https://github.com/username/repository.git'```
> 1.先用```git branch -a```查看當前的分支
> 如果你不在 “master” 分支上，你可以使用 ```git checkout master``` 命令來切換到 “master” 分支。

>2.若git branch -a 未查到任何分支，表示本地電腦上只列出的在電腦本機的分支，以及你已經拉取到本地的遠端分支。
>遠端倉庫的分支，沒有拉取到本地。因此執行：
```
git fetch origin
```

>3.接著執行``` git branch -a ```就可以看到在電腦本機的分支了



資料來源：
https://www.maxlist.xyz/2018/11/02/git_tutorial/
