# MarkdownParser

Markdown 语法解析器

## 安装

```bash
pip install MarkdownParser
```

## 快速使用

```python
import MarkdownParser

html = MarkdownParser.parse("# Hello World!")
print(html)
```

## 更多用法 & 实现思路

https://luzhixing12345.github.io/MarkdownParser/

## 不支持

- 四个空格变为代码段
- [^1]的引用方式
- Latex数学公式
- Setext 形式的标题
- 上标 / 下标 / 下划线
- SpecialTextBlock中叠加使用有可能会有bug

## 相关参考

- [Github Markdown CSS](https://cdn.jsdelivr.net/npm/github-markdown-css@4.0.0/github-markdown.css)