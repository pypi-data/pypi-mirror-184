=====================
document-template
=====================

Python解析文档模版
=====================
     
.. image:: https://img.shields.io/pypi/v/document-template.svg
    :target: https://pypi.org/project/document-template/
.. image:: https://img.shields.io/pypi/pyversions/document-template.svg
    :target: https://pypi.org/project/document-template/
.. image:: https://img.shields.io/pypi/l/document-template.svg
    :target: https://github.com/liying2008/document-template
.. image:: https://img.shields.io/pypi/wheel/document-template.svg
    :target: https://pypi.org/project/document-template/#files


安装方法
---------
使用 **pip** 安装
::

    pip install document-template

使用方法
---------
参考 test.py_  和 test.html_ :

.. _test.py: https://github.com/liying2008/document-template/blob/master/test.py
.. _test.html: https://github.com/liying2008/document-template/blob/master/test.html

:test.html:

.. code-block:: html

    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>#{title}</title>
    </head>
    <body>
    <h1>#{head}</h1>
    <a href="#{url}">#{url}</a>
    <br>
    <h1>网站标题</h1>
    <hr>
    <span style="font-size: larger;font-weight: bold">#{large_font}</span>
    <br>
    show_span 为真时显示:
    #{bool:show_span}<span>show_span is True</span>#{bool:show_span}
    show_span 为假时显示:
    #{bool:!show_span}<span>show_span is False</span>#{bool:!show_span}
    <br>
    #{copy:start}渲染多行文本，并替换局部内容：#{contents} 和 #{another_contents}<br>
    #{copy:end}
    </body>
    </html>

:test.py:

.. code-block:: python

    import sys

    from document_template import DocumentTemplate

    __author__ = 'liying'

    if sys.version_info < (3, 0):
        reload(sys)
        sys.setdefaultencoding('utf-8')

    if __name__ == '__main__':
        id_dict = {"title": "标题", "head": "正文标题", "url": "https://github.com/liying2008", "large_font": "大号字体"}
        id_dict['show_span'] = True

        # Multi-line copy supports string, list and tuple
        # id_dict['contents'] = 'ABCDEFG'
        # id_dict['another_contents'] = '1234567'
        id_dict['contents'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
        id_dict['another_contents'] = ['1', '2', '3', '4', '5', '6', '7']
        dt = DocumentTemplate()
        dt.load("test.html", encoding='utf-8')
        dt.set_identifier_dict(id_dict)
        dt.save_document("new_test.html")


指令说明
---------
- **普通变量**：#{var} 定义普通模板变量；
- **bool指令**：#{bool:var}text#{bool:var} 通过变量 var 是否为 True 控制 text 是否显示，或者 #{bool:!var}text#{bool:!var} 通过变量 var 是否为 False 控制 text 是否显示；
- **copy指令**：#{copy:start}text#{collection_var}#{copy:end} 循环遍历 collection_var ，将其值填充到内容中。


注意事项
---------
- 不支持 **copy 指令** 内使用 **copy 指令** 或 **bool 指令** 。


LICENSE
---------
`MIT License <https://github.com/liying2008/document-template/blob/master/LICENSE>`_

