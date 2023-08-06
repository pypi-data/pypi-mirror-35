# sapass

First version of password generator for python projects

Install easy

Use Easy

Use python version bigger than 2.7

## For generate new password: :-1:
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

## For convert password: :new: Added In version 2.0
> You must use **_convertor_** class

1. Hash password with **hash_password** and validate it **hash_password_validate** method:
```python
new_pwd = "testPWd"
hashed_password = convertor.hash_password(new_pwd)
print(hashed_password)
old_pass = new_pwd
if convertor.check_password(hashed_password, old_pass):
    print('You entered the right password')
else:
    print('I am sorry but the password does not match')

```
 
 2. To verify the strength of password using **password_strong_check**:
 ```python
print(convertor.password_strong_check("hello"))
```

