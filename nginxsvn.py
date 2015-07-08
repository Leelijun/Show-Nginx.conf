import pysvn
import datetime
import sys
import os
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
 
def code2html(code, lang):
    lexer = get_lexer_by_name(lang, encoding='utf-8', stripall=True)
    formatter = HtmlFormatter(linenos=False,encoding='utf-8',noclasses="True",style="native")
    result = highlight(code, lexer, formatter)
    return result
 
def demo(file,filename):
    html = """
    <html>
        <head>
            <title>Pygments_example</title>
        </head>
        <body>
        %s
        </body>
    </html>
    """%code2html(file, 'nginx')
    with open(filename+'.html','w')  as data:
        data.write(html)
        
if __name__ == '__main__':
    client = pysvn.Client()
    client.update('/disk1/nginx')
    entry= client.info('/disk1/nginx')
    print  'SVN PATH',entry.url
    print  'SVN VERSION',entry.commit_revision.number
    print  'SVN AUTHOR',entry.commit_author
    print  'SVN DATE', datetime.datetime.fromtimestamp(entry.commit_time)
    with open('/disk1/nginx/nginx.conf') as data:
          Nginx_online=data.read()
          NginxOnline='NginxOnline'
    demo(Nginx_online,NginxOnline)
