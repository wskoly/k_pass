# k_pass
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/wskoly/k-pass)
### Python package to generate random strong password and OTP.

- [Description](#Description)
- [Installation](#Installation)
- [Examples](#examples)
- [License](#license)
- [Developer](#developer)

## Description
- The package has a function named `GenPass()` which can generate random passwords and OTP which contains random UpperCase, LowerCase, Special and Numeric Characters.
- By default the generated password will be a mixtures of random UpperCase letters, LowerCase letters, Special and Numeric Characters and the length will be also a random number between 16-32.
- User can customize the password generation by passing various argument to the generation function.
- User can customize the password length by passing a numeric value to the `length` parameter.
- There 4 others boolean parameters to control the generated password's characters.
  - boolean `upper` parameter for UpperCase Letters.
  - boolean `lower` parameter for LowerCase Letters.
  - boolean `special` parameter for Special Characters.
  - boolean `number` parameter for Numbers.
- By default all the boolean parameters wll be false. This will generate a random password of mixed charset.
- To enforce custom charset, one should pass True value to the parameters regarding those charset.
## Installation
To install write the following command in your terminal.
```py
pip install k_pass
```
## Examples
Import the function to your code.
```py
from k_pass import GenPass
```
- Generate a random password using default parameters.
```py
password = GenPass()
```
- Generate a random password of a fixed length(mixed characters).
```py
password = GenPass(8)
```
- Generate a random password of a fixed length and consist of only UpperCase letters.
```py
password = GenPass(8, upper=True)
```
- Generate a random password of a random length and consist of only LowerCase letters.
```py
password = GenPass(lower=True)
```
- Generate a random password of a fixed length and consist of Numbers(i.e OTP).
```py
password = GenPass(6, number=True)
```
- Generate a random password of a random length and consist of only Special Characters.
```py
password = GenPass(special=True)
```
- Generate a random password of a fixed length and consist of only Special Characters and UpperCase letters.
```py
password = GenPass(8, upper=True, special=True)
```
## License
MIT

## Developer
#### Wahid Sadique Koly
[Github](https://github.com/wskoly/) [Portfolio](https://wskoly.ml)
