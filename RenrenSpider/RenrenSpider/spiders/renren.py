# -*- coding: utf-8 -*-
import scrapy

# 模拟登录人人网:通过cookie模拟登陆
class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/275083355']

    cookies = {
        "JSESSIONID": "abcjfsaRnyq-7bwOT2JVw",
        "__utma": "151146938.1497419691.1562665337.1562898985.1562898985.1",
        "__utmc": "151146938",
        "__utmz": "151146938.1562898985.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/",
        "_de": "A1F468A6CCE38E6FA6BF0ADA288B2DD9",
        "_ga": "GA1.2.1497419691.1562665337",
        "_gid": "GA1.2.765298501.1562899248",
        "_r01_": "1",
        "anonymid": "jxvmjpb4-4g4lyl",
        "ch_id": "10050",
        "depovince": "BJ",
        "first_login_flag": "1",
        "ick": "41ea6c00-9037-421d-90ac-a8741d61ad95",
        "ick_login": "996dba3a-b53b-43b2-a5e5-2059a4784921",
        "id": "244631764",
        "jebe_key": "b08b8edf-02c1-484b-80ac-4aaff60feb52%7C9479ee29f04b348563b2a795a33f0ccd%7C1562899075678%7C1%7C1562899158511",
        "jebe_key": "b08b8edf-02c1-484b-80ac-4aaff60feb52%7C9479ee29f04b348563b2a795a33f0ccd%7C1562899075678%7C1%7C1562899158513",
        "jebecookies": "e18b29cc-15dd-4fbe-8077-ae154ee1d88e|||||",
        "ln_hurl": "http://hdn.xnimg.cn/photos/hdn521/20120107/2305/h_main_aI41_7a870002aeca2f75.jpg",
        "ln_uact": "suting503@126.com",
        "loginfrom": "null",
        "p": "bca4b90f338107bfd6e06ff7e1a4811b4",
        "societyguester": "231677a619c7ef4af6c141c175b7284b4",
        "t": "231677a619c7ef4af6c141c175b7284b4",
        "ver": "7.0",
        "wp_fold": "0",
        "xnsid": "1b68b84e"
    }

    # 源码解析：遍历start_urls，发送请求
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url,cookies=self.cookies,callback=self.parse_page)



    def parse_page(self, response):
        with open("index-renren3.html", "w",encoding="utf-8") as filename:
            filename.write(response.body.decode("utf-8"))
