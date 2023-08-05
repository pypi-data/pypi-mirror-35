import requests, re, time
import OneKeyTcn.ReleaseSwitch
import OneKeyTcn.IdentifyURLUtil as IdentifyURLUtil


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Connection': 'keep-alive',
}


# 迭代溯源
# 支持插入log方法已经插入中断逻辑的溯源
def iterateRedirect(url, pausefunc=None, logfunc=None):
    try:
        # 由中断方法判定
        if pausefunc != None and pausefunc(url):
            return url
        req = requests.get(url, headers=headers, allow_redirects=False)
        status_code = req.status_code
        if logfunc != None:
            logfunc(status_code)
        # 302 表示重定向，在返回的headers里Location处标识
        if status_code == 302 or status_code == 301:
            if logfunc != None:
                logfunc(req.headers)
                logfunc('检测到重定向，正在帮您溯源...')
            return iterateRedirect(req.headers['Location'], pausefunc, logfunc)
        else:
            if logfunc != None:
                logfunc(req.headers)
                logfunc('溯源成功！原始地址为：【' + url + '】')
            return url
    except:
        return url


# 批量溯源，找到原文中url的原地址
def batchRedirect(text, logfunc=None, delay=0):
    results = text
    # pattern = re.compile('http(s)://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?')
    pattern = re.compile('[a-zA-z]+://[^\s]*')
    items = re.findall(pattern, text)
    for item in items:
        redirect = iterateRedirect(item, logfunc=logfunc)
        if logfunc != None:
            logfunc(item)
            logfunc(redirect)
        results = results.replace(item, redirect)
        time.sleep(delay)

    if logfunc != None:
        logfunc(results)
    return results


# http://union-click.jd.com/jdc?d=ftKbOO  --->https://union-click.jd.com/jda?e=99_2|99_2|1_2_2|tagA&p=AyIHVCtaJQMiQwpDBUoyS0IQWhkeHAxbSkAYCllHGAdFBwtJQBkAWAtTYFpFEE8HC0BMXhEFA0pXRk5KQh5JXxxVC0QeQV1XZgVYC0kOEgZUGloUBhoFQkkfGUdRQwEMC0ZHHgVlayFtSk4dXEg5TgVQWyhvHmJCe0c3TVcZbBEGVRJHFAQOBFYKWBYJFwBeH10lAyIEVBtbFgAUD1ASayUCFjcedVolAyIHURlYFgQTDlUdUxABIgdTKwBAbBVXVhhYFAIbUgcYCxwyIjdlK2sUMhI3Cl8GSA%3D%3D&t=W1dCFFlQCxxOGA5YRE5XDVULR0VeUAxSFksdd0pQQgFHRVdcS0NLQwRAVlsYDF4HSAxAWQpeD0pHc1cWSwcZAhMGVBpaEQoQEAdfV1BBVlNCSwhQDhA%3D&a=fCg9UgoiAwwHO1BcXkQYFFlgdXpyfVFdQVwzVRBSUll%2bAQAPDSwjLw%3d%3d&refer=norefer&d=ftKbOO
# 还原jdc短链为长链接
def recoverJDC(url):
    try:
        req = requests.get(url, headers, allow_redirects=False)
        status_code = req.status_code
        print(status_code)
        if status_code == 200:
            html = req.text
            print(html)
            pattern = re.compile('(?<=var hrl=\').*?(?=\')')
            items = re.findall(pattern, html)
            print(items)
            if len(items) == 1:
                return items[0]
        return url
    except:
        return url



if OneKeyTcn.ReleaseSwitch.debugBackDoor:
    str = '''A、常规签到-京豆
    领京豆 
    http://t.cn/RdNtSt1
    京东会员 
    http://t.cn/RpFEyqd
    京豆乐园 http://t.cn/RuLvpAU
    每日福利 http://t.cn/RH151So
    拍拍签到 http://t.cn/R33hjAY
    京豆寻宝 http://t.cn/RdNtStm'''
    # print(iterateRedirect('http://t.cn/RdNtSt1'))
    # print(IdentifyURLUtil.isJDUrl('https://bean.m.jd.com/rank/index.action'))
    print(batchRedirect(str, logfunc=print, delay=1))
