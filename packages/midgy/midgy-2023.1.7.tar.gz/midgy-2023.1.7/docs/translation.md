# translating markdown to python

translating markdown to python requires 2 units of work:

1. __[tokenization]__ uses a `parser` represent markdown `input` as `tokens`.
2. __rendering__ uses a `renderer` to represent tokens as python.


`midgy` defers the initial __[tokenization]__ work to [`markdown_it`]; the `parser` and `tokens` are dependent on the `markdown_it` types
the primary work of the `midgy` is __rendering__ parsed tokens as python. the __[tokenization]__ step reuses machinery from [`markdown_it`]. the primary types referred to in this work are from the `midgy` and `markdown_it` libraries.
    
```python
    input: str
    parser: "markdown_it.MarkdownIt"
    tokens: list["markdown_it.token.Token"]
    renderer: "midgy.python.Python"
```

## __rendering__ python


## code vs non-code block

## translation implementation with `markdown_it`

the __[tokenization]__ step reuses machinery from the [`markdown_it`] project. this library was chosen because amongst other markdown parsers (eg. [`mistune`], [`mistletoe`], [`python-markdown`]) it is the only one to return line numbers. 

[`markdown_it`] it is a port of the popular [markdown it javascript library]. it appears reliable for the `parser` and `tokens` because: 
* it is not innovating independently so we should expect a fairly stable api.
* the plugin interface makes it possible to extend the markdown parser in consistent ways as we do for the `code_lexer`, `doctest_lexer` and `front_matter` lexer.
* further, [`markdown_it`] has [strong adoption](https://pypistats.org/packages/markdown-it-py) specifically through documentation in `jupyter_book` and linting with `mdformat`. 


    

[tokenization]: https://en.wikipedia.org/wiki/Lexical_analysis#Tokenization
[`markdown_it`]: https://github.com/executablebooks/markdown-it-py
[markdown it javascript library]: https://github.com/markdown-it/markdown-it
[`mistune`]: https://pypi.org/project/mistune/
[`mistletoe`]: https://pypi.org/project/mistletoe/
[`python-markdown`]: https://pypi.org/project/markdown/
[`jupyter_book`]: https://pypi.org/project/jupyter-book/