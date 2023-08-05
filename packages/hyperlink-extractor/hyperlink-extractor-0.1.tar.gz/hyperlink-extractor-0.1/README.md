# hyperlink-extractor

Extracts and returns html links as `hyperlink.URL`.

### Simple Usage

```
In [1]: text = '''    <html>
   ...:         <body>
   ...:             <a id="a_1" href="link1.html"></a>
   ...:             <a id="a_2"></a>
   ...:             <a id="a_3" href="link3.html"></a>
   ...:             <div id="div_1">
   ...:                 <a href="link4.html"></a>
   ...:                 <a href="link5.html"></a>
   ...:             </div>
   ...:         </body>
   ...:     </html> 
   ...:     '''

In [2]: from hyperlink_extractor import extract

In [3]: extract(text)
Out[3]: 
[URL.from_text('link1.html'),
 URL.from_text('link3.html'),
 URL.from_text('link4.html'),
 URL.from_text('link5.html')]

In [4]: extract(text, restrict_xpaths=['//*[@id="div_1"]'], base_url='https://www.test.com')
Out[4]: 
[URL.from_text('https://www.test.com/link4.html'),
 URL.from_text('https://www.test.com/link5.html')]
 ```
