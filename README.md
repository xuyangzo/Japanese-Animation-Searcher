# Japanese Animation Searcher version 1.3
## Xuyang Zou (Lynch)


**v1.3 NEW FEATURES**
- Add `A1-Picture` to `Supported Corporations`
- Add `Every Possible Animation` of `A1-Picture` to `Random Search` functionality 
- Optimize algorithm to skip items that have already been searched
- Modified GUI to make it looks better

<br><br><br>


## Table of Contents

1. introduction
    1. Purpose
    2. Architecture
    3. Functionality
    4. Test Result  
    <br>
2. Design Instruction
    1. Build `spyder.py`
    2. Build `random_search.py`
    3. Build `GUI.py`
    4. Build `main.py`
    <br>
3. Specific Case Warning
    1. Unsupported Websites
    2. Internet Connection
    3. Mac High Sierra Error Message
    <br>
4. Test
    1. Test Environment
    2. Web Interface Test
    3. Message Board Test

<br><br><br>


# 1. Introduction

## Purpose
1. This Python script is used for obtaining basic information about Japanese animations from official websites of Japanese Animation companies like Kyoto Animation, A-1 Pictures. Japanese introductions are with translation
2. This Python script provides Website Search, Deep Search and Random Search
<br>

## Architecture
1. This Python script is designed and implemented with Python 3.6
    1. Documentation of Python 3.6: [http://devdocs.io/python~3.6/](http://devdocs.io/python~3.6/)
    2. No existing code or template used. Everything is `from scratching`
       
2. The `GUI.py` is structured with the following features
    1. GUI 
        - Header/Greeting
        - Profile Image
        - Input Field
            1. Input field for target website
            2. Path selector for target directory
        - Search Buttons
            1. Website Search button
            2. Deep Search button
            3. Random Search button
            4. Quit button
        - Developer Information
    2. Functions for different kinds of searching
        - Function for Website Search
        - Function for Deep Search
        - Function for Random Search
       
3. The `spyder.py` is implemented with following components
    1. Function to retrieve HTML content from given websites
    2. Function to parse and retrieve introduction/images from given websites
    3. Function to retrieve URLs from given website
    4. Function to translate Japanese into English
    5. Function to output HTML content into local file
    6. Test code only for Spyder

4. The `random_search.py` is implemented with following components
    1. Built-in library for all the stored websites
    2. Function to randomly select one of the URLs
<br>

## Functionality
1. Search for animations based on given website
2. Deep Search for animations based on given website
    1. Doing normal Search first
    2. Then going to other URLs in given website and doing normal search
    3. Stop when reach the predetermined number of `searched page` or `successed page`
3. Random Search
    1. Select one URL from the URL library randomly
    2. Doing normal Search on that website
<br>

## Test Result
1. Successful with all tests
2. For more information, please refer to the Test section

<br><br><br>


# 2. Design Instruction

## Build spyder.py
1. Spyder is one of the most important part of this Python script
2. First, need to retrieve HTML content from target website
    1. In `getHTML()`, import `urllib.request`
    2. Build the header for `Request` to `simulate browsers` for the purpose of anti-spyder
        - `Anti-spyder` is violating the website!
        - If retrieving large amount of data, this will cause harm!
        - In no case should anyone retrieve data from a website rather than normal browsering
    3. Use given URL and header to construct a `Request`
    4. Use `urllib.request.urlopen()` to open the `Request` and read the data
    5. Use `utf-8` to decode the data
3. Parse HTML content to obtain necessary information 
    1. Set `Regular Expression` for different websites
        - Based on the implementation of different websites, need different `Regular Expression`
        - `Nippon Animation` has two different `Regular Expression`
        - `Kyoto Animation` also has two different `Regular Expression`
        - `A-1 Pictures` has only one `Regular Expression`
        - The most tricky part is that different `Regular Expression` will result in different data read in as well as different data content format, which will be discussed in detail later
    2. For every Search request, parse each `Regular Expression` 
        - Since `Regular Expression` is exactly fit for certain website, unless two different animation companies use the same structure for their websites, only one of those `Regular Expression` will actually make sense
        - Store all the imformation in a list
4. Retrieve necessary information and output in target file
    1. Build an opener to retrieve images
        - Set the same `header` as did in `getHTML()` section
        - `opener = urllib.request.build_opener()`
        - `opener.addheaders = [(your header)]`
        - `urllib.request.install_opener(opener)`
    2. For each piece of data stored in previous list
        - Check if the image already exists
            1. If the image already exists, do nothing
            2. Otherwise, retrieve image to target directory based on different websites
        - Check if the output file exists
            1. If the output file already does not exist, create the output file 
            2. check if the animation name already exists in output file
                1. If the the animation name already exists, do nothing
                2. Otherwise, write data to the output file
        - If the story is in `Japanese`, translate it into `English`
            1. Import Google's `Translator` module
            2. In `translatorGoogle()`, translate Japanese to English
        - Do not forget to eliminate unnecessary `tabs`, `newline characters` and `enter characters`
5. Retrieve URLs from given HTML content
    1. Set different `Regular Expression` to parse URLs for different websites
        - `Nippon Animation` has one kind of `Regular Expression`
        - `Kyoto Animation` has one kind of `Regular Expression`
        - `A-1 Pictures` has one kind of `Regular Expression`
    2. Parse the HTML content for each `Regular Expression`
<br>

## Build random_search.py
1. Obtain websites from official websites of Japanese animation companies
2. Store all the website URLs in the module
3. Randomly select one of the URLs
<br>

## Build GUI.py
1. Get `absolute path` to resource
    1. Works for `dev` and `PyInstaller`
2. Create GUI window
    1. Import `tkinter`
    2. Initialize window
        - `root = Tk()`
        - Set `title` and `geometry`
    3. Set `Frame`
    4. Set `Greeting Label` to be `row=0` and `column=1`
    5. Present image use `PhototImage`, set it to be `row=1` and `column=1`
    6. Create `Entry` for target website, set it to be `row=2`, `column=1` and `sticky=E`
    7. Create `Entry` and `Button` for target directory
        - Set the `Entry` to be `row=3` and `column=1`
        - Set the `Button` to be `row=3` and `column=1`
        - Use `padx` and `pady` to adjust the layout
    8. Add buttons
        - Set the `Search Button` to be `row=4`, `column=1` and `sticky=W`
        - Set the `Deep Search Button` to be `row=4`, `column=1` and `sticky=E`
        - Set the `Random Search Button` to be `row=5`, `column=1` and `sticky=W`
        - Set the `Quit Button` to be `row=5`, `column=1` and `sticky=E`
        - Use `padx` and `pady` to adjust the layout
    9. Add developer's info
    10. Add `grid` and run the `mainloop`
3. Process input
    1. Select user entered path to target directory
        - In `selectPath()`, obtain the user selected path to target directory
        - Based on the scope, such function has to be declared in `ProcessGUI()`
    2. Evaluate `Entry`
        - If path is not given, show a `messagebox` of error
        - Otherwise, get the entry and call `getHTML()`
            1. Enclose the `getHTML()` function with `try-except-finally` block
            2. If the user enter incorrect URL, should show a `messagebox` of `ValueError`
        - If the content of HTML is retrieved successfully, call `getImage2()`
            1. Enclose the `getImage2()` function with `try-except-finally` block
            2. If `HTTPError`, show a `messagebox` of `Warning`
            3. Otherwise, show a `messagebox` of `Success`
    3. Random Search
        - If path is not given, show a `messagebox` of error
        - Otherwise, call `selectURL()` and call `getHTML()`
            1. Enclose the `getHTML()` function with `try-except-finally` block
            2. If the user enter incorrect URL, should show a `messagebox` of `ValueError`
            3. If `HTTPError`, show a `messagebox` of `Warning`
        - If the content of HTML is retrieved successfully, call `getImage2()`
            1. Enclose the `getImage2()` function with `try-except-finally` block
            2. If `HTTPError`, show a `messagebox` of `Warning`
            3. If `UnicodeEncodeError`, show a `messagebox` of `Warning`
            4. If `URLError`, show a `messagebox` of `Warning`
            5. Otherwise, show a `messagebox` of `Success` 
    4. Deep Search
        - If path is not given, show a `messagebox` of error
        - Otherwise, delcare `MAX_SEARCHED_PAGE` and `MAX_PASSED_PAGE`
        - Get and push root URL
        - While the URL list is not empty
            1. Randomly select one url to parse
            2. call `selectURL()` and call `getHTML()`
                1. Enclose the `getHTML()` function with `try-except-finally` block
                2. If the user enter incorrect URL, should show a `messagebox` of `ValueError`
                3. If `HTTPError`, show a `messagebox` of `Warning`
            3. If the content of HTML is retrieved successfully, call `getImage2()`
                1. Enclose the `getImage2()` function with `try-except-finally` block
                2. If `HTTPError`, show a `messagebox` of `Warning`
                3. If `UnicodeEncodeError`, show a `messagebox` of `Warning`
                4. If `URLError`, show a `messagebox` of `Warning`
                5. Otherwise, show a `messagebox` of `Success` 
        - Increment `searched_page` and `passed_page` based on different situations
<br>

## Build main.py
1. Simply call `ProcessGUI()`

<br><br><br>



# 3. Specific Case Warning

## Unsupported Websites
1. Supported websites for current version (v1.3) of `Japanese Animation Searcher`
    1. Nippon Animation
    2. Kyoto Animation
    3. A-1 Pictures
2. Search under unsupported websites might not give the correct outcome

## Internet Connection
1. `Japanese Animation Searcher` needs Internet connection to be able to parse and download information
2. A poor Internet Connect might cause the program to halt for a very long time without any error messages

## Mac High Sierra Error Message
1. For Mac user using High Sierra System, the console will display the following error message when entering target directory
    - objc[25154]: Class FIFinderSyncExtensionHost is implemented in both /System/Library/PrivateFrameworks/FinderKit.framework/Versions/A/FinderKit (0x7fff91c6db68) and /System/Library/PrivateFrameworks/FileProvider.framework/OverrideBundles/FinderSyncCollaborationFileProviderOverride.bundle/Contents/MacOS/FinderSyncCollaborationFileProviderOverride (0x117a1ccd8). One of the two will be used. Which one is undefined.
2. The error is related to High Sierra System itself and cannot be resolved


<br><br><br>



# 4. Tests

## Test Environment
1. MacBook Pro 13-inch
2. 2560 x 1600 Resolution
3. Intel Iris Plus Graphics 640 1536 MB
<br>

## Spyder Test
1. Tested websites
    1. `http://www.nippon-animation.co.jp/work/meisaku/`
    2. `http://www.kyotoanimation.co.jp/en/works/`
    3. `http://www.nippon-animation.co.jp/work/family/`
    4. `http://a1p.jp/works/`
    5. `http://www.kyotoanimation.co.jp/en/works/hyouka/`
    6. `http://a1p.jp/works/fairytail2018/`
    7. `http://a1p.jp/works/doukyusei/`
    8. `http://a1p.jp/works/oreimo-anime/`
    9. `http://www.nippon-animation.co.jp/work/1893/`
    10. `http://www.nippon-animation.co.jp/work/1751/`
    11. `http://www.nippon-animation.co.jp/work/1423/`
    12. `http://www.nippon-animation.co.jp/work/5858/`
    13. `http://www.nippon-animation.co.jp/work/1688/`
    14. `http://www.nippon-animation.co.jp/work/1542/`
    15. `http://www.kyotoanimation.co.jp/en/works/euphonium2/`
    16. `http://www.kyotoanimation.co.jp/en/works/freeES/`
    17. `http://www.kyotoanimation.co.jp/en/works/k-onMovie/`
2. `getHTML()` Test
    1. `getHTML()` works correctly for every website listed above
3. `getImage2()` Test
    1. `getImage2()` works correctly for every website listed above
4. `getURL()` Test
    1. `getURL()` works correctly for every website listed above
5. `translatorGoogle()` Test
    1. `translatorGoogle()` works correctly for every website listed above
6. `printData()` Test
    1. `printData()` works correctly for every website listed above
<br>

## Random Search Test
1. `selectURL()` Test
    1. `selectURL()` works correctly
<br>

## GUI Test
1. Overall Layout Test
    1. The overall layout looks reasonable
2. Search Tests
    1. Tested Websites
        - `http://www.nippon-animation.co.jp/work/meisaku/`
        - `http://www.kyotoanimation.co.jp/en/works/`
        - `http://www.nippon-animation.co.jp/work/family/`
        - `http://a1p.jp/works/`
        - `http://www.kyotoanimation.co.jp/en/works/hyouka/`
        - `http://a1p.jp/works/fairytail2018/`
        - `http://a1p.jp/works/doukyusei/`
        - `http://a1p.jp/works/oreimo-anime/`
        - `http://www.nippon-animation.co.jp/work/1893/`
        - `http://www.nippon-animation.co.jp/work/1751/`
        - `http://www.nippon-animation.co.jp/work/1423/`
        - `http://www.nippon-animation.co.jp/work/5858/`
        - `http://www.nippon-animation.co.jp/work/1688/`
        - `http://www.nippon-animation.co.jp/work/1542/`
        - `http://www.kyotoanimation.co.jp/en/works/euphonium2/`
        - `http://www.kyotoanimation.co.jp/en/works/freeES/`
        - `http://www.kyotoanimation.co.jp/en/works/k-onMovie/`
    2. `Website Search` Test
        - Image is retrieved correctly to target directory
        - Output file is created correctly
        - Information is written to output file correctly
    3. `Random Search` Test
        - Image is retrieved correctly to target directory
        - Output file is created correctly
        - Information is written to output file correctly
    4. `Deep Search` Test
        - Image is retrieved correctly to target directory
        - Output file is created correctly
        - Information is written to output file correctly
        - URLs are retrieved correctly
        - Number of `passed_page` and `searched_page` match the final output
<br>

## Error Tests
1. Incorrect Path Test
    1. A `messagebox` of `Failed` saying `Please enter correct path` is showed
2. Empty Path Test
    1. A `messagebox` of `Failed` saying `Please enter correct path` is showed
3. Incorrect URL Test
    1. A `messagebox` of `Failed` saying `Please enter correct url` is showed
4. Http Error Test
    1. A `messagebox` of `Warning` saying `DETECT Http Error` is showed
5. Unicode Encode Error Test
    1. A `messagebox` of `Warning` saying `ASCII codec cannot encode characters` is showed
6. URL Error Test
    1. A `messagebox` of `Failed` saying `No host given` is showed
7. Value Error Test
    1. A `messagebox` of `Failed` saying `Fail to obtain url` is showed