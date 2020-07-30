import requests
import bs4
import time

#爬虫开始
def crawl(url):
    try :
        r = requests.get(url,timeout = 12)
        r.encoding = 'utf-8'
        t = r.text
        soup = bs4.BeautifulSoup(t,'html.parser')
        return soup
    except :
        print('爬虫失败')
        #爬虫结束
        return False
        
#取得老hosts
def gethosts(hostsfile):
    #读到原hosts内容
    with open(hostsfile,'r') as fd:
        old_hosts = fd.readlines()
    print('已经读到原hosts文本')
    return old_hosts

#修改老hosts并写入新的hosts
def writehosts(old_hosts, nh, hostsfile):
    #删除老hosts中第23行到40行（具体要修改多长，需要自己在hosts文件里面看长度）
    for i in range(23,41)[::-1]:
        del old_hosts[i]
    #在被删除原ip地址的区域增加新的github ip
    old_hosts.append(nh)
    #把列表内容全部连接起来
    new_hosts = ''.join(old_hosts)
    #复写入文件
    with open(hostsfile,'w') as fd:
        fd.write(new_hosts)
    print('复写成功')

#主函数
def main():
    #hosts路径（根据实际情况修改）
    hostsfile = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    url = 'https://github.com/521xueweihan/GitHub520'
    soup = crawl(url)

    if soup:
        #如果爬虫成功，会得到soup，则接着找soup里面的“pre”标签并存到nh里面
        nh = soup.find_all('pre')[0].text
        note = '更新了新的ip地址'
    else:
        #如果爬虫失败，不会得到任何标签内容，则使用默认的nh值
        nh='''# GitHub520 Host Start
185.199.108.154  github.githubassets.com
199.232.68.133   camo.githubusercontent.com
199.232.68.133   github.map.fastly.net
199.232.69.194   github.global.ssl.fastly.net
140.82.113.3     github.com
140.82.112.5     api.github.com
199.232.68.133   raw.githubusercontent.com
199.232.68.133   user-images.githubusercontent.com
199.232.68.133   favicons.githubusercontent.com
199.232.68.133   avatars5.githubusercontent.com
199.232.68.133   avatars4.githubusercontent.com
199.232.68.133   avatars3.githubusercontent.com
199.232.68.133   avatars2.githubusercontent.com
199.232.68.133   avatars1.githubusercontent.com
199.232.68.133   avatars0.githubusercontent.com
# Star me GitHub url: https://github.com/521xueweihan/GitHub520
# GitHub520 Host End
'''

        note = '使用默认ip地址'
    old_hosts = gethosts(hostsfile)
    writehosts(old_hosts, nh, hostsfile)
    print('{},3秒后自动关闭'.format(note))
    time.sleep(3)

#执行主函数
if __name__ == '__main__':
    main()
