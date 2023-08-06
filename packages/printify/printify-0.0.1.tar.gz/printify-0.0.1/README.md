# Python pretty print

A small printer package to get some better looking print statements.

## Install

```bash
pip install printify
```

## Usage

```python
from printify import printify

printify('test', {'title': 'Test dictionary'}, ['test', 'list'])
```

`Output`

```bash
----------*----------
test
----------*----------
{
        'title': 'Test dictionary'
}
----------*----------
['test', 'list']
----------*----------
```

### `color`

```python
printify("test", color="red")
```

#### Color list

|  Color  |   Code   |
| :-----: | :------: |
| default | \033[0m  |
| warning | \033[93m |
|  error  | \033[91m |
|  blue   | \033[94m |
| success | \033[92m |
| header  | \033[95m |
|   red   | \033[91m |
|  green  | \033[92m |
|  cyan   | \033[96m |
|  white  | \033[97m |
| yellow  | \033[93m |
| magenta | \033[95m |
|  grey   | \033[90m |
|  black  | \033[90m |
