import requests, re


# 是否是京东链接
def isJDUrl(url):
    if url == '':
        return False
    pattern = re.compile('.jd.')
    pattern_search = re.findall(pattern, url)
    if len(pattern_search) == 0:
        return False
    return True


# 是否是京东联盟jdc链接
def isJDShortUnion(url):
    if url == '':
        return False
    pattern = re.compile('http(s?)://union-click.jd.com/jdc\?d=')
    pattern_search = re.findall(pattern, url)
    if len(pattern_search) == 0:
        return False
    return True


