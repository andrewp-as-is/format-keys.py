#!/usr/bin/env python
import format_keys


string = "https://api.travis-ci.org/{fullname}.svg?branch={branch}"
keys = format_keys.keys(string)
print(keys)
