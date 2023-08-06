# sapass

First version of password generator for python projects

Install easy

Use Easy

Use python version bigger than 2.7

```python
from sapass import sapass

print(sapass.generator.get_new_pass(15))
```

### you can use below parameters for class inputs
1. length
    Default length for password defined 8 character, by change this value you get new pass with another size.
2. passType
    ```python
    passType = {'mix', # alphabet + numbers + symbols
            'alphabet', # only alphabet
            'number', # only numbers
            }
    ```
3. includeSymbol
    Boolean parameter: if define 'True' generated password contains special characters such as {!@#$%^&*()}
4. includeUppercaseCharacters
    Boolean parameter: if define 'True' generated password contains uppercase characters such as {ABCDEFGHIJ...}
