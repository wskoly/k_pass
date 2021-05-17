# k_pass
[![](https://img.shields.io/badge/Version-0.0.2-green)](https://github.com/wskoly/k-pass) [![](https://img.shields.io/badge/Author-Wahid%20Sadique%20Koly-red)](https://github.com/wskoly/)
### Python package to generate random strong password and OTP.

- [Description](#Description)
- [Installation](#Installation)
- [Examples](#examples)
- [Author](#author)
- [License](#license)

## Description
- The package has a function named `GenPass()` which can generate random passwords and OTP which contains random UpperCase letters, LowerCase letters, Special and Numeric Characters.
- By default the generated password will be a mixture of random UpperCase letters, LowerCase letters, Special and Numeric Characters, and the length will be also a random number between 16-32.
- User can customize the password generation by passing some arguments to the generation function.
- User can customize the password length by passing a numeric value to the `length` parameter.
- There are other 4 boolean parameters to control the generated password's characters.
  - boolean `upper` parameter for UpperCase Letters.
  - boolean `lower` parameter for LowerCase Letters.
  - boolean `special` parameter for Special Characters.
  - boolean `number` parameter for Numbers.
- By default, all the boolean parameters will be false. This will generate a random password consist of mixed characters.
- To enforce custom charset, one should pass True value to the parameters regarding those charsets.

## Installation
To install, write the following command in your terminal.
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
- Generate a random password of a fixed length and consist of only Numbers(i.e OTP).
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
## Author
**Wahid Sadique Koly**
- [Github](https://github.com/wskoly/) 
- [Portfolio](https://wskoly.ml)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
