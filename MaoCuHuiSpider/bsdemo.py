# coding=utf-8
"""
bs4 测试：看bs能否同时解析多个HTML
测试结果：只能解析一个HTML DOM树
"""
from bs4 import BeautifulSoup

html = """
<html>
     <body>
         <div class="title">标题1</div>
         <div class="title">标题2</div>
     </body>
</html>
<html>
     <body>
         <div class="title">标题3</div>
         <div class="title">标题4</div>
     </body>
</html>
"""

def main():
    soup = BeautifulSoup(html,"lxml")
    titles = soup.select(".title")
    for title in titles:
        print(title.string)

if __name__ == '__main__':
    main()
