accessgoogle
============

暂时只能使用最简单用法 

自动搜索可用google ip地址并自动替换hosts文件来访问google的小工具

###使用方法:

linux下执行accessgoogle.sh即可自动完成hosts文件的生成和替换.

分成三步:

>* 默认读取googleips.txt并正则提取可能的 google ip 地址,判断哪些ip地址可用
>* 从可用ip地址中挑选出最快的ip地址和本地hosts文件生成新hosts文件
>* 用新的hosts文件替换本地hosts文件

命令用法:

`#` ./accessgoogle.sh [filepath/urladdress="./googleips.txt"] [max_ip_num=10]
用filepath或者urladdress更换google ip地址来源,程序会自动提取其中的可用ip,
搜索到max_ip_num个可用的ip地址后停止测试,并从这些地址中选出访问最快的生成hosts文件,默认值为10


###windows下使用方法:
由于依赖python,windows用户可以手动安装python后执行accessgoogle.sh中的相关命令生成hosts文件替换本地C:\WINDOWS\system32\drivers\etc目录下同名文件

###最简单用法:
直接用hosts文件替换本地hosts文件:
linux位置:/etc/hosts
windows位置:C:\WINDOWS\system32\drivers\etc,拖入覆盖即可
注:这种方法不保证持续有效性
