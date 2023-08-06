# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['markdownparser']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'markdownparser',
    'version': '0.1.4',
    'description': '',
    'long_description': "# MarkdownParser\n\nMarkdownParser 是一个 Markdown 语法解析器,用于实现md到html标签的转换\n\n## 安装\n\n```bash\npip install markdownparser\n```\n\n## 快速使用\n\n```python\nimport MarkdownParser\n\nhtml = MarkdownParser.parse('# Hello World')\nprint(html)\n\n#<div class='markdown-body'><h1>Hello World!</h1></div>\n```\n\n## 不支持\n\n- 四个空格变为代码段\n- [^1]的引用方式\n- Latex数学公式\n- Setext 形式的标题\n- 上标 / 下标 / 下划线\n- SpecialTextBlock中叠加使用有可能会有bug\n\n## 相关参考\n\n- [Github Markdown CSS](https://cdn.jsdelivr.net/npm/github-markdown-css@4.0.0/github-markdown.css)",
    'author': 'luzhixing12345',
    'author_email': 'luzhixing12345@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/luzhixing12345/MarkdownParser',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
