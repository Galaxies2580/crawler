import re
test = r"10年增长10倍 如何看中国企业在美专利拥有量的快速增长?,./，。/!@#$"
print(test)
testStr = re.sub('\W','',test)
print(testStr)