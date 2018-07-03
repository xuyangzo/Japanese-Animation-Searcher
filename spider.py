import re
import urllib.request
import os


"""
one way to get HTML page
"""
def getHTML(myurl):

    # declare url and simulate browsers
    myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

    # open url
    req = urllib.request.Request(url=myurl, headers=myheaders)
    data = urllib.request.urlopen(req).read()

    data = data.decode('utf-8')

    return data


"""
Another way to get image
But not fully implemented yet
"""
def getHTML2(myurl):

    # declare url and simulate browsers
    headers = [("Host","img0.imgtn.bdimg.com"),
                         ("Connection", "keep-alive"),
                         ("Cache-Control", "max-age=0"),
                         ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"),
                         ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"),
                         ("Accept-Encoding","gzip,deflate,sdch"),
                         ("Accept-Language", "zh-CN,zh;q=0.8"),
                         ("If-None-Match", "90101f995236651aa74454922de2ad74"),
                         ("Referer","http://image.baidu.com/i?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&word=%E4%BA%A4%E9%80%9A&ie=utf-8"),
                         ("If-Modified-Since", "Thu, 01 Jan 1970 00:00:00 GMT")]


    opener = urllib.request.build_opener()
    opener.addheaders = headers
    data = opener.open(myurl)

    # data = data.decode('utf-8')
    for item in data:
        print(item)

    return data.read()



"""
Retrieve data
解决了urlretrieve时403 forbidden的问题
"""
def getImage2(data, path):

    # achieve image urls

    imglist = []


    # search with regex
    decode_imgre = []
    imgre0 = re.compile(r'src=\"//(gif-jpg\.com.+\.jpg)\" alt=\"(\d*[A-Z]*-\d+)\"')
    imgre1 = re.compile(r'src=\"(.+\.jpg.*)\" alt="(\d*[A-Z]*-\d+).*"')
    imgre2 = re.compile(r'src=\"(.+\.jpg.*)\" .* alt=\".*【(\d*[A-Z]*-\d+)】.*\"')
    imgre3 = re.compile((r'file=\"(.+\.png)\" .* alt="(\d*[A-Z]*-\d+)"'))
    imgre4 = re.compile(r'alt=\"(\d*[A-Z]*-\d+)\" data-original="//(.+\.jpg)"')
    imgre5 = re.compile(r'src=\"(.+\.jpg.*)\" .* alt=\".*(\d*[A-Z]+-\d+).*"')
    decode_imgre.append(imgre0)
    decode_imgre.append(imgre1)
    decode_imgre.append(imgre2)
    decode_imgre.append(imgre3)
    decode_imgre.append(imgre4)
    decode_imgre.append(imgre5)

    # select decode method
    for imgre in decode_imgre:
        imglist += imgre.findall(data)

    current_path = os.path.dirname(__file__)
    print(current_path)


    # process image
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    # deal with first imglist
    for singleimg in imglist:

        # check if the file exists
        if os.path.exists(path+singleimg[0]+".jpg") or os.path.exists(path+singleimg[1]+".jpg"):
            return []
        # if the file does not exist
        else:
            # deal with special url
            if "http" not in singleimg[0]:
                urllib.request.urlretrieve("http://"+singleimg[0], "{0}/{1}.jpg".format(path, singleimg[1]))
            elif "." not in singleimg[0]:
                urllib.request.urlretrieve(singleimg[1], "{0}/{1}.jpg".format(path, singleimg[0]))
            else:
                urllib.request.urlretrieve(singleimg[0], "{0}/{1}.jpg".format(path, singleimg[1]))

    return imglist


"""
Get more urls when given url
"""
def getURL(data):

    # set regex
    urlgre = re.compile(r'href=\"(http:.+\.html)\"')
    urllist = urlgre.findall(data)

    return urllist



"""
将番号打印在本地txt文档里
"""
def PrintData(myurl, outFile):

    # achieve data
    data = getHTML(myurl)

    # process 番号
    m = re.findall("(\d*)([A-Z]+)-(\d+)", data)
    dataList = []
    if len(m):
        for item in m:
            if item[1] != "UTF" :
                wholestr = item[0] + item[1] + "-" + item[2]
                if(wholestr not in dataList):
                    dataList.append(wholestr)
                    print(wholestr, file=outFile)



"""
main function only for test
"""
def main():

    # declare url
    myurl1 = "http://www.zhucai8.cc/"  # 番号库
    myurl2 = "http://www.zhizhubt.net/60525.html"       # 宅男福利
    myurl3 = "https://www.zhaifanshe.com/fhku/page/2"           # 宅番社
    myurl4 = "http://lianlianyingshi8.com/category/259luxu"          #恋恋番号网
    myurl5 = "https://www.8550.org/names/"

    # declare output file
    # outFile = open("output.txt", "w")
    # outFile.truncate()

    data = getHTML(myurl5)

    print(getImage2(data))
    # ConvertAll(path="images/", new_path="ConvertedImages/")

if __name__ == "__main__":
    main()