Title: Pandoc Markdown 文档
Tags: markdown,pandoc
lang: zh
Slug: pandoc-markdown
Summary: Pandoc Markdown 文档
Date: 2018-07-15
Modified: 2018-08-04


-----------------------------


# Philosophy 哲学

Markdown is designed to be easy to write,and,even more importantly,easy to read.

>A Markdown-formatted document should be publishable as-is,as plain text,without looking like it's been marked up with tags or formatting instructions. - [John Gruber](http://daringfireball.net/projects/markdown/syntax#philosophy)

# Paragraphs 段落

一个段落包含一行或多行文字，通过行后跟随一个或多个空白行，换行符（newlines）和空格（spaces）作用一样，如果需要硬换行（hard line break），在行后添加两个以上的空格。

Extension `escaped_line_breaks`

反斜杠（backslash）后跟随换行符也是一种硬换行

**Note** 在多行和表格中，这种方式是唯一的方式进行硬换行，因为表格中空格会被忽略。

# Headers 标题

## 标题风格

两种风格的标题 Setext 和 ATX

- Setext 风格

```markdown
A level-one header
==================

A level-two header
------------------
```

- ATX 风格

```markdown
# A level-one header

## A level-two header

### A level-three header ###
```

Extension `blank_before_header`

标准 Markdown 语法不需要在标题前空白行，Pandoc 需要 **空白行**（除了在文档开头）。原因是可能由于自动断行后产生歧义。

```markdown
I like several of their flavors of ice cream:
#22, for example, and #5.
```

Extension `space_in_atx_header`

大多数 Markdown 语法不需要在`#`与标题文字间添加 **空格**，但是Pandoc需要空格。

## Header identifiers 标题标识符

Extension `header_attributes`

可以标题文字后添加属性，`{#identifier .class .class key=value key=value}`。本语法兼容[PHP Markdown Extra](https://michelf.ca/projects/php-markdown/extra/)

添加的属性通常用于 **HTML** 或基于 **HTML** 的格式文件如 **EPUB**。

Extension `implicit_header_references`

Pandoc 默认为标题创建引用链接,并可直接使用,如果有多个相同标题，引用将指向第一个出现的标题。引用大小写不敏感。

```markdown
[Header identifiers in HTML]
or
[Header identifiers in HTML][]
or
[the section on header identifiers][header identifiers in
HTML]
or
[Header identifiers in HTML](#header-identifiers-in-html)
```

# Block quotations 块引用

Markdown 使用 email 传统引用文字，每行前面都有一个`>`字符和一个可选空格，`>`符号不需要从最左边开始，但是不应该缩进超过三个空格。

```markdown
> This is a block quote. This
> paragraph has two lines.
>
> 1. This is a list inside a block quote.
> 2. Second item.
```

lazy form,需要在块引用的第一行使用`>`符号即可。

```markdown
> This is a block quote. This
paragraph has two lines.

> 1. This is a list inside a block quote.
2. Second item.
```

nested quote,块引用可以多层嵌套

```markdown
> This is a block quote.
>
> > A block quote within a block quote.
```

**Note** 如果在`>`符号后跟随可选空格，这些空格将被解析为块引用的一部分而不是内容缩进，如果需要产生缩进你需要在`>`符号后输入 **五个空格**

Extension `blank_before_blockquote`

标准语法不需要在块引用前添加 **空白行**，Pandoc需要（除了文档开头），原因是自动断行造成歧义，除非指定`markdown_strict`标志，Pandoc不认为以下代码是引用嵌套。

```markdown
> This is a block quote.
>> Nested.
```

# Verbatim(code) blocks 代码块

## Indented code blocks 缩进代码块

文本缩进四个空格或一个tab键，将被视为代码块，保留空格、换行，特殊字符不会触发样式。初始缩进 **四个空格或tab** 将在输出中移除。

**Note** 代码块中空白行不需要四个空格缩进

## Fenced code blocks 围栏代码块

Extension `fenced_code_blocks`

除了标准缩进代码块，Pandoc支持围栏代码块，使用`~`符号，在代码块前后添加一行符号，后行长度至少和起始行一样。

```markdown
~~~~~
if (a > 3) {
  moveShip(5 * gravity, DOWN);
}
~~~~~
```

围栏代码块需要空白行分离周围普通文本，如果代码中包含`~`符号需要使用更长的波浪线行。

Extension `backtick_code_blocks`

同 `fenced_code_blocks` 使用 `` ` `` 代替 `~` 符号

Extension `fenced_code_attributes`

围栏代码块可附加属性

```markdown
~~~~ {#mycode .haskell .numberLines startFrom="100"}
qsort []     = []
qsort (x:xs) = qsort (filter (< x) xs) ++ [x] ++
               qsort (filter (>= x) xs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

`mycode` 是标识符，`haskell`和`numberLines`表示classes，`startForm`属性值为100。这些属性值可以用于语法高亮 [syntax highlight](http://pandoc.org/MANUAL.html#syntax-highlighting)

```html
<pre id="mycode" class="haskell numberLines" startFrom="100">
  <code>
  ...
  </code>
</pre>
```
`numberLines` 将显示代码行数，以下是快捷（shortcut）形式

~~~~~markdown
~~~{.haskell}
qsort [] = []
~~~
equal
~~~haskell
qsort [] = []
~~~
~~~~~

如果 `fenced_code_attributes` 拓展关闭，但是文本中包含属性值，这些属性将会被打印。

# Line blocks 行块

Extension `line_blocks`

行块是一系列以垂直符`|`开头后接空格的文本行，断行、空格将被保留。用于诗词和地址。借鉴与[reStructuredText](http://docutils.sourceforge.net/docs/ref/rst/introduction.html)

```markdown
| The limerick packs laughs anatomical
| In space that is quite economical.
|    But the good ones I've seen
|    So seldom are clean
| And the clean ones so seldom are comical

| 200 Main St.
| Berkeley, CA 94718
```

# Lists 列表

## Bullet lists 项目列表／无序列表

项目列表使用项目符（`*`,`+`,`-`）开头。

```markdown
* one
* two
* three
```

默认生成的项目列表紧凑，如果需要稀疏列表，可以在将列表项格式化为段落，在列表项之间添加空格

```markdown
* one

* two

* three
```

**Note** 列表不需要左边缘对齐，可以使用一到三个空格缩进，**项目列表符后必须有空格**

## Block content In list items 列表内的块

列表项可能包含多个段落或块级内容，然而后续段落必须以 **空白行开头并且缩进以列表标记之后的第一个非空格内容对齐**

```markdown
  * First paragraph.

    Continued.

  * Second paragraph. With a code block, which must be indented
    eight spaces:

        { code }
```

Exceptin 如果列表标记后跟随缩进代码块，必须在列表标记后添加 **五个空格**，后续段落必须在列表标记的最后一个字符后 **两个空格缩进**

```markdown
*     code

  continuation paragraph
```

列表包含其他列表，前置空白行可以省略，内嵌的列表缩进必须与前一个列表标记后的第一个非空字符对齐。

```markdown
* fruits
  + apples
    - macintosh
    - red delicious
  + pears
  + peaches
* vegetables
  + broccoli
  + chard
```

懒式（lazily）列表可以省略行前缩进，但如果列表项存在多个段落或其他块，**每段的第一行需要缩进**

```markdown
+ A lazy, lazy, list
item.

+ Another one; this looks
bad but is legal.

    Second paragraph of second
list item.
```

## Ordered lists 有序列表

标准 Markdown 语法，序号是十进制数字后加 **`.`和空格**，序号数字会被忽略。

```markdown
1.  one
2.  two
3.  three

5.  one
7.  two
1.  three
```

Extension `fancy_lists`

Pandoc 允许有序列表使用大小写字母、罗马数字、阿拉伯数字标注，列表标记可能被括号包围、单独一个右括号或者句号，他们必须与列表内容间隔一个空格，如果列表标记是大写字母后接句号则间隔至少两个空格。`#`同样可以作为符号标记

```markdown
#. one
#. two
```

Extension `startnum`

Pandoc 同样支持自定义起始数字，以下列表数字后接右括号，从9开始，并且子列表为小写罗马数字。

```markdown
9)  Ninth
10)  Tenth
11)  Eleventh
       i. subone
      ii. subtwo
     iii. subthree
```

Pandoc 将不同类型的列表标记重新开始列表，以下是建立三个列表

```markdown
(2) Two
(5) Three
1. Four
*  Five
```

## Definition lists 列表定义

Extension `definition_lists`

Pandoc 支持定义列表，使用[PHP Markdown Extra](https://michelf.ca/projects/php-markdown/extra/)

```markdown
Term 1

:   Definition 1

Term 2 with *inline markup*

:   Definition 2

        { some code, part of Definition 2 }

    Third paragraph of definition 2.
```

每行定义一个术语，后面可存在空白行，但必须存在一个或多个定义，定义始于冒号或波浪号，可能会存在缩进一两个空格。

TODO

## Numbered example lists 编号示例列表

Extension `example_lists`

特殊列表标记符`@`，列表会依次编号横跨整个文档，后续的新列表使用`@`标记符，会续接之前的编号

```markdown
(@)  My first example will be numbered (1).
(@)  My second example will be numbered (2).

Explanation of examples.

(@)  My third example will be numbered (3).
```

编号的示例可以打标签并且在文档中引用

```markdown
(@good)  This is a good example.

As (@good) illustrates, ...
```

标签可以使用任何字母数字下划线和连字符

**Note** 连续段落在示例列表中 **必须缩进四个空格**

## Compact and loose lists 紧凑／稀疏列表

Pandoc 与 `Markdown.pl` 在"边缘情况"(edge cases)表现不同

```markdown
+   First
+   Second:
    -   Fee
    -   Fie
    -   Foe

+   Third
```
Pandoc 解释为紧凑列表（`<p>` 不包围 **First**, **Second**, **Third** 而 Markdown 不包围 **First** ）因为 **Third** 的空格。Pandoc 遵循简单的规则：如果文本后跟随空格视为段落，**Second** 后没有空行后接列表视为非段落。事实上列表后接空白行是无关的。

## Ending a list 结束列表

```markdown
-   item one
-   item two

    { my code block }
```

Pandoc 将代码块视为第二个列表项的第二段而不是代码块

为了“切断”列表，可以插入不缩进的内容，如HTML注释

```markdown
-   item one
-   item two

<!-- end of list -->

    { my code block }
```

你可以使用同样的方法获得两个连续的列表而不是一个

```markdown
1.  one
2.  two
3.  three

<!-- -->

1.  uno
2.  dos
3.  tres
```

# Horzontal rules 水平分隔线

一行包含三个以上 `*`,`-`,`_` 字符，字符间可插入空格，视为水平分割线

```markdown
*  *  *  *

---------------
```

# Tables 表格

四种列表样式，前三种要求等宽（fixed-width）字体,最后一种可以使用等比例（proportionally spaced）字体

Extension `table_captions`

选择为所有4种表格提供题注。题注是以字符串Table:(或只是:)开头的段落，它将被剥离,它可能出现在表格之前或之后。

Extension `simple_tables`

```markdown
  Right     Left     Center     Default
-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123
      1     1          1             1

Table:  Demonstration of simple table syntax.
```

表头和表行必须各自填充一行。列对齐由表头文本相对于其下方虚线的位置确定

- 如果虚线与右侧的表头文本齐平但在左侧超出表头，则该列右对齐
- 如果虚线与左侧的表头文本齐平但在右侧超出表头，则该列左对齐
- 如果虚线超出两侧的表头文本，则该列居中对齐。
- 如果虚线与两侧的表头文本齐平，则使用默认对齐方式（大多数情况是左对齐）

**表格必须以空白行结束或空白行后接虚线行**

如果使用虚线来结束表格，则可以省略列表头

```makrdown
-------     ------ ----------   -------
     12     12        12             12
    123     123       123           123
      1     1          1              1
-------     ------ ----------   -------
```

省略标题时，根据表格主体的第一行内容确定列对齐。在上表中，列将分别为右，左，中和右对齐。

Extension `multiline_tables`

多行表格允许表头和表行跨越多行文本（但不支持跨越表的多个列或行的单元格）

```markdown
-------------------------------------------------------------
 Centered   Default           Right Left
  Header    Aligned         Aligned Aligned
----------- ------- --------------- -------------------------
   First    row                12.0 Example of a row that
                                    spans multiple lines.

  Second    row                 5.0 Here's another one. Note
                                    the blank line between
                                    rows.
-------------------------------------------------------------

Table: Here's the caption. It, too, may span
multiple lines.
```

同简单列表类似，但存在以下不同

- 它们必须以表头文本之前的一行虚线开头（除非省略表头）
- 它们必须以一行虚线结束，然后是空白行
- 行之间必须用空行分隔

多行表可能只有一行，但该行后面应该有一个空行（然后是结束表的虚线行）

Extension `grid_tables`

```markdown
: Sample grid table.

+---------------+---------------+--------------------+
| Fruit         | Price         | Advantages         |
+===============+===============+====================+
| Bananas       | $1.34         | - built-in wrapper |
|               |               | - bright color     |
+---------------+---------------+--------------------+
| Oranges       | $2.10         | - cures scurvy     |
|               |               | - tasty            |
+---------------+---------------+--------------------+
```

`=`行将表头与表体分开，对于无表头可以省略。网格表的单元格可以包含任意块元素（多个段落，代码块，列表等）,不支持跨多个列或行的单元格。

通过将冒号放在表头后面的分隔线边界处，类似与`pipe tables`

```markdown
+---------------+---------------+--------------------+
| Right         | Left          | Centered           |
+==============:+:==============+:==================:+
| Bananas       | $1.34         | built-in wrapper   |
+---------------+---------------+--------------------+
```

对于无表头，冒号位于顶行

```markdown
+--------------:+:--------------+:------------------:+
| Right         | Left          | Centered           |
+---------------+---------------+--------------------+
```

**Note** Pandoc不支持具有行跨度或列跨度的网格表。这意味着Pandoc既不支持跨行的可变列数，也不支持跨列的可变行数。所有网格表在每行中必须具有相同的列数，并且每列中的行数必须相同

Extension `pipe_tables`

```markdown
| Right | Left | Default | Center |
|------:|:-----|---------|:------:|
|   12  |  12  |    12   |    12  |
|  123  |  123 |   123   |   123  |
|    1  |    1 |     1   |     1  |

  : Demonstration of pipe table syntax.
```

前后垂直符可省略，表头不能省略。 要模拟无表头表，请包含带有空白单元格的表头。由于垂直线指示列边界，因此列不需要垂直对齐

```markdown
fruit| price
-----|-----:
apple|2.05
pear|1.37
orange|3.09
```

表的单元格不能包含段落和列表等块元素，也不能跨越多行。如果表包含可打印内容宽于列宽的行，则表将占用全文宽度，单元格内容将换行，相对单元格宽度由在表格表头与表格主体分隔的行中虚线数量确定。另一方面，如果没有行宽于列宽，则单元格内容将不会包裹，单元格将根据其内容确定大小

# Metadata blocks 元数据块

Extension `pandoc_title_block`

```markdown
% title
% author(s) (separated by semicolons)
% date
```

解析为书目信息，而不是常规文本,如果需要不同的信息，使用空白行分离

```markdown
%
% Author

% My title
%
% June 15, 2006
```

标题可能占用多行，但延续行必须以空格开头

```markdown
% My title
  on multiple lines
```

如果文档有多个作者，则作者可能被放在具有开头空格的单独行中，或者用分号或两者分隔

```markdown
% Author One
  Author Two

% Author One; Author Two

% Author One;
  Author Two
```

日期必须单独一行

所有三个元数据字段都可能包含标准内联格式（inline format）（斜体，链接，脚注等）


Extension `yaml_metadata_block`

顶部的三个连字符`---`和底部的三个连字符`---`或三个点`...`的行分隔。 **YAML**元数据块可能出现在文档中的任何位置，但如果它不在文档开头，则必须以前方存在空白行

元数据可以包含列表和 **YAML** 对象，Pandoc 将忽略名称以下划线结尾的字段，如果两个元数据块尝试设置相同的字段，则将采用第一个块中的值。

必须遵循 **YAML** 转义规则,标题包含冒号，则必须引用它。垂直符`|`在缩进行的行首，该行将按字面解释，无需转义。当文本中包含空行或块级样式时，必须遵守以上规则

```markdown
---
title:  'This is the title: it contains a colon'
author:
- Author One
- Author Two
tags: [nothing, nothingness]
abstract: |
  This is the abstract.

  It consists of two paragraphs.
...
```

TODO `Template variables`

# Backslash escapes 反斜杠转义

Extension `all_symbols_escapable`

除了代码块或内联代码之外，任何以反斜杠开头的标点符号或空格字符都将按字面处理，即使它表示格式。

```markdown
*\*hello\**

one will get

<em>*hello*</em>

instead of

<strong>hello</strong>
```

转义字符`` \`*_{}[]()>#+-.! ``，反斜杠转义空格被解析为不间断空格

反斜杠转义的换行符（即在行尾发生的反斜杠）被解析为硬换行。这是Markdown的“隐形”换行方式，和行后尾随两个空格作用相同

**Note** 反斜杠转义在代码块种不起作用

# Inline formatting 内联样式

## Emphasis 强调

单个`*`或`_`包围文本表示斜体

```markdwon
This text is _emphasized with underscores_, and this
is *emphasized with asterisks*.
```

两个`*`或`_`包围文本表示加重／加粗

```markdown
This is **strong emphasis** and __with underscores__.
```

`*`或`_`包围文本中 **存在空格或反斜杠转义** 不会产生斜体效果

```markdown
This is * not emphasized *, and \*neither is this\*.
```

Extension `intraword_underscores`

因为`_`有时在单词和标识符中使用，所以Pandoc不会将由字母、数字包围的名称`_`处理为斜体，使用`*`代替

```markdown
feas*ible*, not feas*able*.
```

## Strikeout 删除线

Extension `strikeout`

用 `~~` 开始和结束

```markdown
This ~~is deleted text.~~
```

## Superscripts and subscripts 上下标

Extension `superscript` `subscript`

通过`^`字符包围上标文本来表示上标; 可以通过`〜`字符围绕下标文本来表示下标

```markdown
H~2~O is a liquid.  2^10^ is 1024.
```

如果上标或下标文本包含空格，则必须使用反斜杠转义这些空格

## Verbatim

文本放在反引号`` ` ``中，默认保留所有格式

```markdown
What is the difference between `>>=` and `>>`?
```

如果文本中包含反引号`` ` ``,使用``` `` ```代替，包围的前后空格会被忽略

```markdown
Here is a literal backtick `` ` ``
```

**Note** 反斜杠转义在文本上下文不起作用

Extension `inline_code_attributes`

类似于围栏代码块

```markdown
`<$>`{.haskell}
```

# Math 数学公式

Extension `tex_math_dollars`

两个`$`字符之间的任何内容都将被视为TeX数学公式。开头`$`必须在其右边有一个非空格字符，而结束`$`必须在其左边有一个非空格字符，并且不能立即跟随一个数字。 如果由于某种原因你需要包含文本`$`字符中，则反斜杠`\`转义它们.

# Raw HTML

Extension `raw_html`

Markdown允许您在文档中的任何位置插入原始HTML（其中<，>和＆按字面解释）

Extension `markdown_in_html_blocks`

Extension `native_divs`

Extension `native_spans`

Extension `raw_tex`

**LaTeX** 文本

```markdown
\begin{tabular}{|l|l|}\hline
Age & Frequency \\ \hline
18--25  & 15 \\
26--35  & 33 \\
36--45  & 22 \\ \hline
\end{tabular}
```

# Generic raw attribute

Extension `raw_attribute`

具有特殊属性的内联 `spans` 和围栏代码块将被解析为具有指定格式的内容 **?**

~~~markdown
\```{=ms}
.MYMACRO
blah blah
\```
~~~

# LaTeX macros

Extension `latex_macros`

TODO

# Links 链接

## Automatic links 自动链接

将`URL`或`email` 放在尖括号中

```markdown
<http://google.com>
<sam@green.eggs.ham>
```

## Inline links 内联链接

内联链接由方括号中的链接文本组成，后跟圆括号的URL。（URL后面可以跟引号中的链接标题。）

```markdown
This is an [inline link](/url), and here's [one with
a title](http://fsf.org "click here for a good time!").
```

**方括号部分和圆括号部分之间不能有空格** 链接文本可以包含格式，但标题`tilte`不能。

内联链接中的电子邮件地址不会被自动检测，因此必须以`mailto`为前缀

```markdown
[Write me!](mailto:sam@green.eggs.ham)
```

## Reference links 参考链接

显式参考链接有两个部分，链接本身和链接定义

链接由方括号的链接文本，后跟方括号中的标签组成。 链接定义包括方括号标签，后跟 **冒号和空格**，后跟URL，以及可省略的引号或括号中的链接标签。**引用优先于链接标签**

```markdown
[my label 1]: /foo/bar.html  "My title, optional"
[my label 2]: /foo
[my label 3]: http://fsf.org (The free software foundation)
[my label 4]: /bar#special  'A title in single quotes'
[my label 5]: <http://foo.bar.baz>
[my label 6]: http://fsf.org
  "The free software foundation"
```

链接标签大小写不敏感

```markdown
Here is [my link][FOO]

[Foo]: /bar/baz
```

隐式参考链接的第二个方括号内容可以省略


```markdown
See [my website][].

[my website]: http://foo.bar.baz
```

**Note** 大多数 Markdown 实现不能将参考链接嵌入列表项和块引用中，Pandoc解除了这个限制。

```markdown
> My block [quote].
>
> [quote]: /foo
```

Extension `shortcut_reference_links`

短参考引用可以省略第二个方括号

```markdown
See [my website].

[my website]: http://foo.bar.baz
```

## Internal links 内部链接

内部链接支持链接到自动生成的标题识别符

```markdown
See the [Introduction](#introduction).

See the [Introduction].

[Introduction]: #introduction
```

# Images 图片

一个链接紧接着一个`!`将被视为插入图像，链接文本将用图像替代文字

```markdown
![la lune](lalune.jpg "Voyage to the moon")

![movie reel]

[movie reel]: movie.gif
```

Extension `implicit_figures`

图像存在非空的文字出现在段落中，将渲染成图像题注

```markdown
![This is the caption](/url/of/image.png)
```

Extension `link_attributes`

图片链接可以设置属性样式

```markdown
An inline ![image](foo.jpg){#id .class width=30 height=20px}
and a reference ![image][ref] with attributes.

[ref]: foo.jpg "optional title" {#id .class key=val key2="val 2"}
```

# Divs and Spans

Extension `fenced_divs`

Pandoc 支持围栏 `div` 语法,连续三个冒号，后面可跟随属性样式

```markdown
::::: {#special .sidebar}
Here is a paragraph.

And another.
:::::
```

围栏 `div` 可以嵌套使用

```markdown
::: Warning ::::::
This is a warning.

::: Danger
This is a warning within a warning.
:::
::::::::::::::::::
```

Extension `bracketed_spans`

行内方括号包围文字可以解释为链接，如果后面跟随属性样式将会解析为 `Span` 标签

```markdown
[This is *some text*]{.class key="val"}
```

# Footnotes 脚注

Extension `footnotes`

```markdown
Here is a footnote reference,[^1] and another.[^longnote]

[^1]: Here is the footnote.

[^longnote]: Here's one with multiple blocks.

    Subsequent paragraphs are indented to show that they
belong to the previous footnote.

        { some.code }

    The whole paragraph can be indented, or just the first
    line.  In this way, multi-paragraph footnotes work like
    multi-paragraph list items.

This paragraph won't be part of the note, because it
isn't indented.
```

脚注标志符可能不包含空格、tab、回车，输出时脚注会被依次编号。脚注不需要放在文档末位处，每个脚注需要使用空白行与其他内容分离

Extension `inline_notes`

行内脚注不能包含多段落内容

```markdown
Here is an inline note.^[Inlines notes are easier to write, since
you don't have to pick an identifier and move down to type the
note.]
```

# Citations 引用

Extension `citations`

Pandoc 使用以下命令可以自动生成引用和参考目录

```bash
pandoc --filter pandoc-citeproc myinput.txt
```

TODO

# Non-pandoc extensions

以下拓展可以默认未开启，如需使用需要在 `+EXTENSION` 后输入拓展名

Extension `old_dashes`

智能解析 `-` 和 `--` 符号，pandoc <= 1.8.2.1, `textile` 输出默认选中

Extension `angle_brackets_escapable`

允许 `<` 和 `>` 作为转义字符

Extension `lists_without_preceding_blankline`

允许列表在段落后出现，没有中间空格

Extension `four_space_rule`

列表项后续段落需要四个空格缩进

Extension `spaced_reference_links`

允许参考链接的两个括号之间存在空格

Extension `hard_line_breaks`

段落中的所有换行符被解释为硬换行符而不是空格

Extension `ignore_line_breaks`

导致段落中的换行符被忽略，而不是被视为空格或硬换行符。 此选项适用于东亚语言，其中单词之间不使用空格，但文本被分为行以便于阅读。

Extension `east_asian_line_breaks`

同上，对于包含东亚宽字符和其他字符混合的文本，这是一个比 `ignore_line_breaks` 更好的选择。

Extension `emoji`

Pandoc 解析 `:smile:` 为 Emoji 表情

Extension `tex_math_single_backslash`

`\( \)` 和 `\[ \]` 解析为数学公式，但是会忽略转义的 `\(` 和 `\[`

Extension `tex_math_double_backslash`

`\\( \\)` 和 `\\[ \\]` 解析为数学公式

Extension `markdown_attribute`

默认 Markdown 解析块级属性为文本内容,此拓展只解析 具有 `markdown=1` 标签的块属性

Extension `mmd_title_block`

支持 [MultiMarkdown](http://fletcherpenney.net/multimarkdown/) 风格的标题块,如果 `pandoc_title_block` 和 `yaml_metadata_block` 选项开启会优先于此拓展

```markdown
Title:   My title
Author:  John Doe
Date:    September 1, 2008
Comment: This is a sample mmd title block, with
         a field spanning multiple lines.
```

Extension `abbreviations`

解析 PHP Markdown Extra 缩写键值,Pandoc不支持缩写，缩写键值简单跳过

```markdown
*[HTML]: Hypertext Markup Language
```

Extension `autolink_bare_uris`

所有绝对路径成为链接，即使没有尖括号`<...>`包围

Extension `mmd_link_attributes`

```markdown
This is a reference ![image][ref] with multimarkdown attributes.

[ref]: http://path.to/image "Image title" width=20px height=30px
       id=myId class="myClass1 myClass2"
```

Extension `mmd_header_identifiers`

Extension `compact_definition_lists`

兼容性定义列表，pandoc <= 1.2*

# Markdown variants Markdwon 变种

## markdown_phpextra(PHP Markdown Extra)

>
footnotes, pipe_tables, raw_html, markdown_attribute, fenced_code_blocks, definition_lists, intraword_underscores, header_attributes, link_attributes, abbreviations, shortcut_reference_links, spaced_reference_links.

## markdown_mmd(MultiMarkdown)

>
pipe_tables, raw_html, markdown_attribute, mmd_link_attributes, tex_math_double_backslash, intraword_underscores, mmd_title_block, footnotes, definition_lists, all_symbols_escapable, implicit_header_references, auto_identifiers, mmd_header_identifiers, shortcut_reference_links, implicit_figures, superscript, subscript, backtick_code_blocks, spaced_reference_links, raw_attribute.

## markdown_strict(Markdown.pl)

>
raw_html, shortcut_reference_links, spaced_reference_links.

## gfm(GitHub-Flavored Markdown)

>
pipe_tables, raw_html, fenced_code_blocks, auto_identifiers, ascii_identifiers, backtick_code_blocks, autolink_bare_uris, intraword_underscores, strikeout, hard_line_breaks, emoji, shortcut_reference_links, angle_brackets_escapable.

# 常用语法高亮

常用语法高亮

```markdown
awk
bash
bibtex
c
cpp
cmake
css
changelog
coffee
diff
djangotemplate
dockerfile
doxygen
doxygenlua
email
erlang
gcc
go
html
haskell
ini
json
jsp
java
javascript
javadoc
kotlin
llvm
latex
lua
makefile
markdown
matlab
php
perl
postscript
powershell
python
ruby
sql
sqlmysql
scala
scheme
texinfo
mandoc
xml
yaml
zsh
dot
sed
xorg
```

# 引用
[Pandoc](http://pandoc.org/MANUAL.html#pandocs-markdown)