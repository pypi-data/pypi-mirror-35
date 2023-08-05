https://github.com/yoptgyo/get_input
Author: Prashant Sengar
Author email: prashantsengar5@hotmail.com

# get_input
Python module to take input of a defined data type from user


# How to use


```python

import get_input

return_value = get_input.input(prompt, data_type)
```




## Data types which can be used:

  -'int' for integer
  -'str' for string

  -'float' for float values
  
  


# Example code

`integer_value = get_input.input("Please enter a number: ", 'int')`



```python

>>> Please enter a number: hello

>>> Please enter an integer value.

>>> Please enter a number: 5.0

>>> Please enter an integer value.

>>> Please enter a number: 5

>>>

```



--It will ask the user to enter an integer value and will wait till an integer value is returned--

