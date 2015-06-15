# -*-coding=utf-8-*-
from tutorial.qrod import QrodItem
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import urllib2
import os
import string


class QrodSpider(BaseSpider):
    name = "qrod"
    allowed_domains = ["qrod.org"]

    start_urls = []
    for i in range(1,10):
        start_urls.append("http://www.weixinqun.cn/weixin/index/id/140/p/"+str(i))

    def downloadImg(self,fileUrl):
        print('download file:'+fileUrl)
        filename =  (fileUrl.replace('/','_').replace(":","-"))
        destFile = open("./qrode/" + (filename), 'wb')
        if (os.path.exists(filename)):
            print('file is exist')
            return
        request = urllib2.Request(fileUrl)
        request.add_header('User-Agent',
                           'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)')
        request.add_header('Accept-Language', 'zh-CN')
        request.add_header('Accept-Encoding', 'gzip, deflate')
        request.add_header('Accept', 'image/jpeg,image/gif');
        print('send request')
        res = urllib2.urlopen(request)
        read = res.read()
        destFile.write(read)
        destFile.flush()
        print('download finish')

    def parse(self, response):
        host = "http://www.weixinqun.cn";
        hxs = HtmlXPathSelector(response)
        xpath = hxs.select("//div[contains(@class,'pop')]")
        for s in xpath:
            # select = xpath.select("//img[contains(@alt,'" + ('微信群二维码').decode('utf-8') + "')]")
            select = xpath.select("//img[@alt='" + ('微信群二维码').decode('utf-8') + "'][@width='160']")
            for img in select:
                img_select = img.select('@src')
                for img_url in img_select:
                    self.downloadImg(host+img_url.extract())

