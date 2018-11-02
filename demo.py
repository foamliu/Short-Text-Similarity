import difflib

# 其中的str1，str2并未分词，是两组字符串
str1 = '兆丰世贸大楼'
str2 = '兆疯世贸大厦'

diff_result = difflib.SequenceMatcher(None, str1, str2).ratio()
print(diff_result)
