
from requests_html import HTMLSession
import re
import sys
import wget

if len(sys.argv)>=2:
    session = HTMLSession()
    for i in range(1,len(sys.argv)):
        url = 'https://www.instagram.com/'+f'{sys.argv[i]}'+'/?__a=1'
        link = session.get(url)
        if(link.status_code == 200):
            html = link.text
            img = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-]?',html)
            wget.download(img[1])
            print('')
        else:
            print('Invalid Username')
    
    session.close()

else:
    print('Required username|\'s')


