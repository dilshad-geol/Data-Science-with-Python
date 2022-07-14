# Markdown Language Cheat Sheet
***
# Content
[1- Headings](#1--heading)\
[2- Block of Words](#2--block-of-words)\
[3- Line Breaks](#3--line-breaks)\
[4- Combining two things](#4--combine-two-things)\
[5- Face of Text](#5--face-of-text)\
[6- Bullet Points and Lists](#6--bullet-points-lists)\
[7- Lines and Page breaks](#7--lines-and-page-break)\
[8- Links and Hyper links](#8--links-and-hyperlinks)\
[9- Images and Figures With links](#9--images-and-figures-with-links)\
[10- Adding code or Code Block](#10--adding-code-or-code-block)\
[11- Adding Tables](#11--adding-tables)\
[12- Extensions for Markdown](#12--extensions-for-markdown)\
[13- Changing colors](#13--changing-colors)\
[14- Adding equations](#14--adding-equations)
***
# 1- Heading
> How to give headings in markdown files?
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

# 2- Block of Words
This is normal text in markdown
> This is a block of special text.

> This is another block of special text.

# 3- Line breaks
This is a Dilshad Raza doing his assignment for Python ka Chilla 40-Days course.\
This is next line
# 4- Combine Two things
Block of words & Heading:
> ## Heading
# 5- Face of text
**Bold**\
***Italic Bold***\
*Italic*

or these symbols can be used:
_ (underscore)

__BOLD__\
_ITALIC_
# 6- Bullet points/ Lists
- First bullet point
- Second Bullet point
- Third Bullet point
    - Sub-bullet 1
      - another sub bullet
    - Sub-heading 2
      - Another Subbullet

Also can be formed by usiing * and + sign
* Bullet point with star sign
+ Bullet point with plus sign

> Numbering of lists
1. List 1
    1. Sub List 1
    2. Sub List 2
2. List 2
3. List 3
4. List 4
5. List 5
6. List 6
7. List 7
8. List 8
# 7- Lines and Page Break
This is page 1
___
---
***
This is page 2
# 8- Links and Hyperlinks
<https://www.youtube.com>

---
[The playlist of python ka chilla is here](https://youtube.com/playlist?list=PL9XvIvvVL50HVsu-Ao8NBr0UJSO8O6lBI)

[Youtube]:https://www.youtube.com

Click to open youtube [here][Youtube]


# 9- Images and Figures with Links

To add picture from local dir\
[image](image.extension)\
to show picture in preview, add exclamation mark(!)

To add Online picture\
[Image](url) 

# 10- Adding Code or Code Block
> To print Hello, World! use \
`print("Hello, World!")`

or to add block of code use
> writing code language would help understanding code type like Python Syntax below:
```python
#Code
x=2
y=3
z= x*y
print(z)
```
> writing code language would help understanding code type like R Syntax below:
```R
#Code
x=2
y=3
z= x*y
print(z)
```
# 11- Adding Tables

|First column|Second column| Third Column|
:---:| :-------:|:------:|
|Value 1| Value 2| Value 3|
|Value 1| Value 2| Value 3|
|Value 1| Value 2| Value 3|


# 12- Extensions for Markdown
- Markdown All-in-One
- Markdownlint
- Markdown PDF
- Markddown Shortcuts
  
  **Bold** ctrl+ B\
  **Italic** ctrl + I\
  ***Italic and Bold***
  
  Toggle image\
  Togle hyperlink\
  Toggle codeblock\
  Toggle inline code\
  ~~Strikethrough~~\
  Toggle Citations\
  Toggle citation
> Add table

Column A | Column B | Column C
---------|----------|---------
 A1 | B1 | C1
 A2 | B2 | C2
 A3 | B3 | C3
>Add table with header

Column A | Column B | Column C
---------|----------|---------
 A1 | B1 | C1
 A2 | B2 | C2
 A3 | B3 | C3

# 13- Changing Colors
This text color is normal.\
<span style = "color: red">
This text color is red.\
</span>
# 14- Adding Equations

> In line Maths

$this_{is}^{inline}$

> Math Block

$$
\int_0^\infinity\frac{x^3}{e^x-1}\, dx = \frac{\pi^4}{15}
$$

You can visit following link for more information: [Mathjax](https://jupyterbook.org/content/math.html)