我们测试环境有四个：uat, qa, stg, live

这个项目是把uat的测试的截图全部保存在UAT文件夹，
然后在qa的截图放在QA文件夹，
然后把遍历qa文件夹的文件，和UAT的同名截图进行对比，不同的则提示出来

图片对比用的是pillow库（PIL)
截图用的是webdriver，使用ie浏览器，因为webdriver的截图功能只有在IE下才能实现长截图
