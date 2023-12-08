# Web-Crawler---Hot-Comments-in-NetEase-Cloud-Music

Steps
1. Check the source code of the web page to see if it contains the required information, if so, skip to 3.
2. Load the page at a low speed and look for the files that contain the required information.
3. Find 'user-agent' and 'Referer' in the message header, and "params" and "encSecKey" in the form data.
4. Use requests.post() to crawl the file.
5. Extract the specific information in the file .

中文
1. 查看网页的源码中是否有所需信息，如果有，直接跳到3。
2. 低网速加载网页，寻找包含所需信息的文件。
3. 找到消息头中的'user-agent'和'Referer'，和表单数据中的"params"，"encSecKey"。
4. 使用requests.post()爬取文件。
5. 将文件中的特定信息提取出来。
