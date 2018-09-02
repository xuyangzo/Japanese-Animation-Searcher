import re
import urllib.request
import os
from translate import Translator


"""
one way to get HTML page
"""
def getHTML(myurl):

    # declare url and simulate browsers
    myheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

    # open url
    req = urllib.request.Request(url=myurl, headers=myheaders)
    data = urllib.request.urlopen(req).read()

    data = data.decode('utf-8')

    return data


"""
Retrieve data
Solved 403 forbidden problem when urlretrieving
"""
def getImage2(data, path):

    # achieve image urls

    imglist = []


    # search with regex
    regexWebsite = []

    """
    NIPPON Animation:
    Name --> singleimg[0]
    Image --> singleimg[1]
    Broadcasting Period --> singleimg[2]
    Number of Episodes --> singleimg[3]
    Original Author --> singleimg[4]
    Broadcaster --> singleimg[5]
    Airtime --> singleimg[6]
    Story --> singleimg[7]
    """
    nippon = re.compile(r'<a href=\"/work/\">作品紹介</a> &gt; (.*)</p>[\s\S]*<div class=\"work-img\">\n'
                            + r'<img width=\"\d+\" height=\"\d+\" src=\"(.+.[jp][pn]g)\"[\s\S]*'
                            + r'<li><dl><dt><span>放送期間</span></dt><dd>(.*)</dd></dl></li>[\s\S]*'
                            + r'<li><dl><dt><span>話　数</span></dt><dd>(.*)</dd></dl></li>[\s\S]*'
                            + r'<li><dl><dt><span>原　作</span></dt><dd>(.*)</dd></dl></li>[\s\S]*'
                            + r'<li><dl><dt><span>放送局</span></dt><dd>(.*)</dd></dl></li>[\s\S]*'
                            + r'<li><dl><dt><span>放送時間</span></dt><dd>(.*)</dd></dl></li>'
                            + r'[\s\S]*<div class="story">\n?(.*)\n?</div>'
                            )

    """
    NIPPON Animation 2:
    Name --> singleimg[0]
    Image --> singleimg[1]
    Broadcasting Period --> singleimg[2]
    Number of Episodes --> singleimg[3]
    Original Author --> singleimg[4]
    Broadcaster --> singleimg[5]
    Airtime --> singleimg[6]
    Story --> singleimg[7]
    """
    nippon2 = re.compile(r'<a href=\"/work/\">作品紹介</a> &gt; (.*)</p>[\s\S]*<div class=\"work-img\">\n'
                        + r'<img width=\"\d+\" height=\"\d+\" src=\"(.+\.[jp][pn]g)\"[\s\S]*'
                        + r'<li><dl><dt><span>放送期間</span></dt><dd>(.*)</dd></dl></li>[\s\S]*'
                        + r'<li><dl><dt><span>話　数</span></dt><dd>(.*)</dd></dl></li>[\s\S]*'
                        + r'<li><dl><dt><span>原　作</span></dt><dd>(.*)</dd></dl></li>[\s\S]*'
                        + r'<li><dl><dt><span>放送局</span></dt><dd>(.*)</dd></dl></li>[\s\S]*'
                        + r'<li><dl><dt><span>放送時間</span></dt><dd>(.*)</dd></dl></li>'
                        + r'[\s\S]*<div class="story">\n?([\s\S]*)\n?</div>\n</section>\n\n\n'
                        )

    """
    Kyoto Animation: 
    Name --> singleimg[0]
    Image --> singleimg[1]
    Story --> singleimg[2]
    """
    kyoto = re.compile(r'<h2>(.*)</h2>[\s\S]*<div class=\"worksImg\">\r\n\t*' +
                       r'<img src=\"(.*\.jpg)\"[\s\S]*' +
                       r'<p class=\"story\">([\s\S]*)</p>\r\n\t*<time>')

    """
    Kyoto Animation 2: 
    Name --> singleimg[0]
    Image --> singleimg[1]
    Story --> singleimg[2]
    """
    kyoto2 = re.compile(r'<h2>(.*)</h2>[\s\S]*<div class=\"worksImg\">\r\n\t*' +
                       r'<img src=\"(.*\.jpg)\"[\s\S]*' +
                       r'<p class=\"story\">\r\n *([\s\S]*)</p>\r\n\t* *<time>')

    regexWebsite.append(nippon)
    regexWebsite.append(nippon2)
    regexWebsite.append(kyoto)
    regexWebsite.append(kyoto2)

    # select decode method
    for imgre in regexWebsite:
        imglist += imgre.findall(data)

    # process image
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    # deal with first imglist
    for singleimg in imglist:

        # check if the image exists
        if not os.path.exists(path + "/" + singleimg[0]+".jpg"):
            # NIPPON Animation
            if len(singleimg) is 8:
                urllib.request.urlretrieve(singleimg[1], "{0}/{1}.jpg".format(path, singleimg[0]))
            elif len(singleimg) is 3:
                urllib.request.urlretrieve("http://www.kyotoanimation.co.jp/" + singleimg[1],
                                           "{0}/{1}.jpg".format(path, singleimg[0]))

        # check if name exists
        if not os.path.exists(path+"/result.txt"):

            # declare output file
            outFile = open(path + "/result.txt", "a")

            if len(singleimg) is 8:
                # process potential <br> tag in Story
                strx = str(singleimg[7])
                strx = strx.replace("<br>", "")
                strx = strx.replace("<br />", "")

                # translate the story
                translation = translatorGoogle(strx)

                # print
                print("Name: " + singleimg[0] + "\n\n" +
                      "Broadcasting Period: " + singleimg[2] + "\n\n" +
                      "Number of Episodes: " + singleimg[3] + "\n\n" +
                      "Original Author: " + singleimg[4] + "\n\n" +
                      "Broadcaster: " + singleimg[5] + "\n\n" +
                      "Airtime: " + singleimg[6] + "\n\n" +
                      "Story: \n" + strx + "\n\n" +
                      "Story Translation: \n" + translation + "\n\n" +
                      "====================================================================" +
                      "\n\n\n\n",
                      file=outFile)

            elif len(singleimg) is 3:
                # process potential <br> tag in Story
                strx = str(singleimg[2])
                strx = strx.replace("<br />", "")
                strx = strx.replace("\t", "")
                strx = strx.replace("\r", "")
                strx = strx.replace("\n", "")
                strx = strx.replace("<br>", "\n")

                # print
                print("Name: " + singleimg[0] + "\n\n" +
                      "Story: \n" + strx + "\n\n" +
                      "====================================================================" +
                      "\n\n\n\n",
                      file=outFile)

            outFile.close()
        else:
            inFile = open(path+"/result.txt", "r")
            allText = inFile.read()

            if singleimg[0] not in allText:
                # declare output file
                outFile = open(path+"/result.txt", "a")

                if len(singleimg) is 8:
                    # process potential <br> tag in Story
                    strx = str(singleimg[7])
                    strx = strx.replace("<br>", "")
                    strx = strx.replace("<br />", "")

                    # translate the story
                    translation = translatorGoogle(strx)
                    translation.replace("&#39; ", "")

                    # print
                    print("Name: " + singleimg[0] + "\n\n" +
                          "Broadcasting Period: " + singleimg[2] + "\n\n" +
                          "Number of Episodes: " + singleimg[3] + "\n\n" +
                          "Original Author: " + singleimg[4] + "\n\n" +
                          "Broadcaster: " + singleimg[5] + "\n\n" +
                          "Airtime: " + singleimg[6] + "\n\n" +
                          "Story: \n" + strx + "\n\n" +
                          "Story Translation: \n" + translation + "\n\n" +
                          "===================================================================="+
                          "\n\n\n\n",
                          file=outFile)

                elif len(singleimg) is 3:
                    # process potential <br> tag in Story
                    strx = str(singleimg[2])
                    strx = strx.replace("<br />", "")
                    strx = strx.replace("\t", "")
                    strx = strx.replace("\r", "")
                    strx = strx.replace("\n", "")
                    strx = strx.replace("<br>", "\n")

                    # print
                    print("Name: " + singleimg[0] + "\n\n" +
                          "Story: \n" + strx + "\n\n" +
                          "====================================================================" +
                          "\n\n\n\n",
                          file=outFile)

                outFile.close()

            inFile.close()

    return imglist

"""
Get more urls when given url
"""
def getURL(data):

    # set regex for different website
    rawURL = []
    urllist = []
    nippon = re.compile(r'<dt><a href=\"(.*)\">.*</a></dt>\n<dd class=')
    kyoto = re.compile(r'<li class=\"\">\r\n\t*<a href=\"(.*)\" title=')

    rawURL.append(nippon)
    rawURL.append(kyoto)

    for singleURL in rawURL:
        obtainedSTR = singleURL.findall(data)
        obtainedSTR = ["http://www.kyotoanimation.co.jp" + url if "www" not in url else url for url in obtainedSTR]
        urllist += obtainedSTR

    return urllist

"""
Translate Japanese to English using Google Translator
Need to connect to Internet to use it
"""
def translatorGoogle(text):
    translator = Translator(to_lang="en", from_lang="ja")
    translation = translator.translate(text)
    return translation


"""
Save output to local file
For test only
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
    website0 = "http://www.nippon-animation.co.jp/work/meisaku/"
    website1 = "http://www.kyotoanimation.co.jp/en/works/"
    website2 = "http://www.nippon-animation.co.jp/work/family/"

    test = "http://www.kyotoanimation.co.jp/en/works/euphoniumMovie/"

    # declare output file
    outFile = open("/Users/lynch0114/Downloads/output2.txt", "w")
    outFile.truncate()

    data = getHTML(website2)
    print(data, file=outFile)

    # save image
    getImage2(data, "/Users/lynch0114/Downloads/test")
    # ConvertAll(path="images/", new_path="ConvertedImages/")

    # translatorGoogle("あなたはおばあちゃん")

if __name__ == "__main__":
    main()