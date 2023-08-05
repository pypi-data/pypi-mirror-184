# com2fun - Transform document into function.

This liabrary leverages [OpenAI API](https://github.com/openai/openai-python) to predict the output of a function based on its documentation.

## Install

```
pip install --upgrade com2fun
```

## Usage

```
@com2fun.com2fun
def top(category: str, n) -> list[str]:
    """Return a list of top-n items in a category."""

In  [1]: top("fish", 5)
Out [1]: ['salmon', 'tuna', 'cod', 'halibut', 'mackerel']
In  [2]: top("Pen Brand", 3)
Out [2]: ['Pilot', 'Uni-ball', 'Zebra']
```

## Add Example

```
In [3]: top.add_example('continents', 3)(['Asia', 'Africa', 'North America'])
```

## Different Prompt Format

### Python Interpreter

```
In  [3]: pirnt(top.invoke_prompt("Pen Brand", 3))
>>> 1
1
>>> def top(category: str, n) -> list[str]:
>>>     """Return a list of top-n items in a category."""
>>>     _top(*locals())
>>>
>>> top('continents', 3)
['Asia', 'Africa', 'North America']
>>> top('Pen Brand', 3)

```

### Flat

```
@functools.partial(com2fun.com2fun, SF=com2fun.FlatSF)
def text2tex(text: str) -> str:
    pass

In  [1]: text2tex.add_example("x divided by y")(r"\frac{x}{y}")
In  [2]: print(text2tex.invoke_prompt("integrate f(x) from negative infinity to infinity"))
def text2tex(text: str) -> str:
    pass
###
'x divided by y'
---
\frac{x}{y}
###
'integrate f(x) from negative infinity to infinity'
---

```

### Template
This format is inspired by [lambdaprompt](https://github.com/approximatelabs/lambdaprompt).

```
In  [1]: text2tex = com2fun.prompt("{} into latex: ")
In  [2]: text2tex.add_example("x divided by y")(r"\frac{x}{y}")
In  [3]: print(text2tex.invoke_prompt("integrate f(x) from negative infinity to infinity"))
x divided by y into latex: \frac{x}{y}
integrate f(x) from negative infinity to infinity into latex: 
```
