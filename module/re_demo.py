# coding=utf-8

import re

content = "ab+cd&e"
content = re.sub(r'\+|=|,|&|%|#|@|!', '', content)

print content

