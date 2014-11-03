accessgoogle
============

自动搜索可用google ip地址并自动替换hosts文件来访问google的小工具

Windows下暂时只能使用最简单用法,也可以手动执行python googleip.py [ipfile path]之后再用当前目录的hosts文件替换 

###使用方法:

linux下执行accessgoogle.sh即可自动完成hosts文件的生成和替换.

分成三步:

>* 默认读取googleips.txt并正则提取可能的 google ip 地址,判断哪些ip地址可用
>* 从可用ip地址中挑选出最快的ip地址和本地hosts文件生成新hosts文件
>* 用新的hosts文件替换本地hosts文件

命令用法:

```bash
# ./accessgoogle.sh [filepath/urladdress="./googleips.txt"]
```

用filepath或者urladdress更换google ip地址来源,程序会自动提取其中的可用ip,


###最简单用法:
直接用hosts文件替换本地hosts文件:
linux位置:/etc/hosts
windows位置:C:\WINDOWS\system32\drivers\etc,拖入覆盖即可
注:这种方法不保证持续有效性


由于某些特殊原因,这里的googleips.txt文件只提供了10个有效谷歌ip地址`[至2014年11月3日有效]`,如果这里的ip地址均不可用或者愿意提供给作者新的可用google ip地址,欢迎练习本人.邮箱地址:hscaizh@gmail.com.

