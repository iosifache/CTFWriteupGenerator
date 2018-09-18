# Tokyo Westerns CTF 4th 2018: simpleauth

![date](https://img.shields.io/badge/date-01.01.1970-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)  
![web category](https://img.shields.io/badge/category-web-lightgrey.svg)
![score](https://img.shields.io/badge/score-55-blue.svg)
![solves](https://img.shields.io/badge/solves-343-brightgreen.svg)

## Description
http://simpleauth.chal.ctf.westerns.tokyo

## Summary
Exploit **CVE-2007-3205** vulnerability in *PHP*, that consist in arbitrary variable overwrite with function `parse_str()`

## Flag
```
TWCTF{d0_n0t_use_parse_str_without_result_param}
```

## Detailed solution
Visiting the given URL, we can view the [source code](index.php) of the application, from which we learn how looks a basic auth request(`action=auth&user=USER&pass=PASS`) and how the app works. We observe a *`parse_str()`* function call, that is vulnerable, according to [CVE-2007-3205](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-3205).  
> The parse_str() function, when called without a second parameter, might allow remote attackers to overwrite arbitrary variables by specifying variable names and values in the string to be parsed.

So, to get the value of `$flag` variable, we need to figured out a method to bypass `$hashed_password` verification. The `$action` need to be "*auth*", likewise the `$res = parse_str($query)`.  
According to the founded vulnerability, we need to overwrite the `$hashed_password` with a URL variable and to keep its value unchanged before the verification(`$user` and `$pass` must be `NULL`).  
The final exploit is *`action=auth&hashed_password=c019f6e5cd8aa0bbbcc6e994a54c757e`, appended to the base URL.  