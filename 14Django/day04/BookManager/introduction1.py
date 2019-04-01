"""
    模板语言：
    {{ 变量 }}

    {% 代码段 %}

    {%  一个参数时：变量|过滤器, Book.id | add: 1 <= 2 当前id+1来和2比较
        两个参数时：变量|过滤器:参数 %}， 过滤器最多只能传2个参数，过滤器用来对传入的变量进行修改
        {% if book.name|length > 4 %} 管道|符号的左右不能有多余的空格，否则报错，其次并不是name.length而是通过管道来过滤
        {{ book.pub_date|date:'Y年m月j日' }} 日期的转换管道

"""