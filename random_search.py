import random


"""
randomly select 1 url to search
"""
def selectURL():

    allURl = []

    # Nippon Animation Meisaku
    allURl.append("http://www.nippon-animation.co.jp/work/1893/")
    allURl.append("http://www.nippon-animation.co.jp/work/1875/")
    allURl.append("http://www.nippon-animation.co.jp/work/1859/")
    allURl.append("http://www.nippon-animation.co.jp/work/1791/")
    allURl.append("http://www.nippon-animation.co.jp/work/1765/")
    allURl.append("http://www.nippon-animation.co.jp/work/1751/")
    allURl.append("http://www.nippon-animation.co.jp/work/1730/")
    allURl.append("http://www.nippon-animation.co.jp/work/1713/")
    allURl.append("http://www.nippon-animation.co.jp/work/1678/")
    allURl.append("http://www.nippon-animation.co.jp/work/1658/")
    allURl.append("http://www.nippon-animation.co.jp/work/1627/")
    allURl.append("http://www.nippon-animation.co.jp/work/1601/")
    allURl.append("http://www.nippon-animation.co.jp/work/1582/")
    allURl.append("http://www.nippon-animation.co.jp/work/1558/")
    allURl.append("http://www.snippon-animation.co.jp/work/1532/")
    allURl.append("http://www.nippon-animation.co.jp/work/1511/")
    allURl.append("http://www.nippon-animation.co.jp/work/1486/")
    allURl.append("http://www.nippon-animation.co.jp/work/1473/")
    allURl.append("http://www.nippon-animation.co.jp/work/1446/")
    allURl.append("http://www.nippon-animation.co.jp/work/1423/")
    allURl.append("http://www.nippon-animation.co.jp/work/1408/")
    allURl.append("http://www.nippon-animation.co.jp/work/1387/")
    allURl.append("http://www.nippon-animation.co.jp/work/1370/")
    allURl.append("http://www.nippon-animation.co.jp/work/1307/")
    allURl.append("http://www.nippon-animation.co.jp/work/1285/")
    allURl.append("http://www.nippon-animation.co.jp/work/1061/")
    allURl.append("http://www.nippon-animation.co.jp/work/962/")
    allURl.append("http://www.nippon-animation.co.jp/work/843/")

    # Nippon Animation Family
    allURl.append("http://www.nippon-animation.co.jp/work/5808/")
    allURl.append("http://www.nippon-animation.co.jp/work/5858/")
    allURl.append("http://www.nippon-animation.co.jp/work/5884/")
    allURl.append("http://www.nippon-animation.co.jp/work/6078/")
    allURl.append("http://www.nippon-animation.co.jp/work/5807/")
    allURl.append("http://www.nippon-animation.co.jp/work/4139/")
    allURl.append("http://www.nippon-animation.co.jp/work/6085/")
    allURl.append("http://www.nippon-animation.co.jp/work/3564/")
    allURl.append("http://www.nippon-animation.co.jp/work/1928/")
    allURl.append("http://www.nippon-animation.co.jp/work/1920/")
    allURl.append("http://www.nippon-animation.co.jp/work/1916/")
    allURl.append("http://www.nippon-animation.co.jp/work/1912/")
    allURl.append("http://www.nippon-animation.co.jp/work/1906/")
    allURl.append("http://www.nippon-animation.co.jp/work/1871/")
    allURl.append("http://www.nippon-animation.co.jp/work/1855/")
    allURl.append("http://www.nippon-animation.co.jp/work/1847/")
    allURl.append("http://www.nippon-animation.co.jp/work/1839/")
    allURl.append("http://www.nippon-animation.co.jp/work/1811/")
    allURl.append("http://www.nippon-animation.co.jp/work/1777/")
    allURl.append("http://www.nippon-animation.co.jp/work/1722/")
    allURl.append("http://www.nippon-animation.co.jp/work/1709/")
    allURl.append("http://www.nippon-animation.co.jp/work/1700/")
    allURl.append("http://www.nippon-animation.co.jp/work/1696/")
    allURl.append("http://www.nippon-animation.co.jp/work/1688/")
    allURl.append("http://www.nippon-animation.co.jp/work/1674/")
    allURl.append("http://www.nippon-animation.co.jp/work/1670/")
    allURl.append("http://www.nippon-animation.co.jp/work/1654/")
    allURl.append("http://www.nippon-animation.co.jp/work/1644/")
    allURl.append("http://www.nippon-animation.co.jp/work/1640/")
    allURl.append("http://www.nippon-animation.co.jp/work/1636/")
    allURl.append("http://www.nippon-animation.co.jp/work/1597/")
    allURl.append("http://www.nippon-animation.co.jp/work/1578/")
    allURl.append("http://www.nippon-animation.co.jp/work/1569/")
    allURl.append("http://www.nippon-animation.co.jp/work/1554/")
    allURl.append("http://www.nippon-animation.co.jp/work/1550/")
    allURl.append("http://www.nippon-animation.co.jp/work/1546/")
    allURl.append("http://www.nippon-animation.co.jp/work/1542/")
    allURl.append("http://www.nippon-animation.co.jp/work/1528/")
    allURl.append("http://www.nippon-animation.co.jp/work/1524/")
    allURl.append("http://www.nippon-animation.co.jp/work/1520/")
    allURl.append("http://www.nippon-animation.co.jp/work/1507/")
    allURl.append("http://www.nippon-animation.co.jp/work/1503/")


    # kyoto animation
    allURl.append("http://www.kyotoanimation.co.jp/en/works/euphonium2/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/koeMovie/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/phantom/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/highspeed/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/kyokaiMovie/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/freeES/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/tamakoMovie/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/chuni02/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/kyokai/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/chuniMovie/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/free/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/tamako/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/chuni/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/hyouka/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/k-onMovie/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/nichijou/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/k-on02/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/haruhiDMovie/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/muntoMovie/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/k-on/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/muntoTV/")

    # randomly select one url
    myurl = random.choice(allURl)

    return myurl


"""
Select regular expression to use for specific url
Not implemented in current program
"""
def selectRegex(myurl):

    imgre1 = 'src=\"//(gif-jpg\.com.+\.jpg)\" alt=\"(\d*[A-Z]+-\d+)\"'       # 番号库
    imgre2 = 'src=\"(.+\.jpg.*)\" alt="(\d*[A-Z]+-\d+).*"'         # 宅番社
    imgre3 = 'src=\"(.+\.jpg.*)\" .* alt=\".*【(\d*[A-Z]+-\d+)】.*\"'       # 恋恋番号网
    imgre4 = 'file=\"(.+\.png)\" .* alt="(\d*[A-Z]+-\d+)"'       # 宅男福利

    regex = []
    regex.append(imgre1)
    regex.append(imgre2)
    regex.append(imgre3)
    regex.append(imgre4)


    if "zhizhu" in myurl:
        return regex[3]
    elif "zhaifanshe" in myurl:
        return regex[2]
    elif "lianlianyingshi" in myurl:
        return regex[1]
    elif "zhucai" in myurl:
        return regex[0]
    else:
        return ""


"""
main() function only for test
"""
def main():
    myurl = selectURL()
    print(selectRegex(myurl))

if __name__ == "__main__":
    main()