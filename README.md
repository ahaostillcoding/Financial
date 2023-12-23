# Financial
uniapp实现理财记账本(湖科大安卓课设)



## 一。注册登录

### 1.注册

![image-20231223174143404](https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora%E5%9B%BE%E7%89%87/image-20231223174143404.png)

![image-20231223174211823](https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora%E5%9B%BE%E7%89%87/image-20231223174211823.png)



### 2。登录

![image-20231223174025830](https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora%E5%9B%BE%E7%89%87/image-20231223174025830.png)

## 二.用户管理

![image-20231223174042809](https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora%E5%9B%BE%E7%89%87/image-20231223174042809.png)

![image-20231223172538557](https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora%E5%9B%BE%E7%89%87/image-20231223172538557.png)![image-20231223172703750](https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora%E5%9B%BE%E7%89%87/image-20231223172703750.png)

## 三。记账功能



![image-20231223172747771](https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora%E5%9B%BE%E7%89%87/image-20231223172747771.png)

### 1.支出

![image-20231223172829002](https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora%E5%9B%BE%E7%89%87/image-20231223172829002.png)

### 2.收入

![image-20231223172842221](https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora%E5%9B%BE%E7%89%87/image-20231223172842221.png)

## 四。记录明细

![image-20231223172943013](https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora%E5%9B%BE%E7%89%87/image-20231223172943013.png)

### 点击日期切换查看日期

![image-20231223173012030](https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora%E5%9B%BE%E7%89%87/image-20231223173012030.png)

### 点击行修改数据

![image-20231223173036111](https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora%E5%9B%BE%E7%89%87/image-20231223173036111.png)

## 五。支出/收入排行榜

### 可按周/月/年来查看收入/支出的分类排行榜

![image-20231223173102384](https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora%E5%9B%BE%E7%89%87/image-20231223173102384.png)

## 六。数据导出

>  python写的后端接口，文件在了static/python底下

### 导出为excel

​	主要通过python库中的**Pandas**转换json数据成为excel数据并保存。用fastapi做的接口。生成文件后上传阿里云oss



### 导出为txt

​	同样用fastapi做接口，将json数据直接保存为txt为后缀的文件即可，同样生成文件后上传oss

![image-20231223173159296](https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora%E5%9B%BE%E7%89%87/image-20231223173159296.png)

