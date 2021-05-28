def getStr(s):
  s=s[:0] + s[0] + s[0:]
  s=s[:0] + s[0] + s[0:]
  s=s[:3] + s[3] + s[3:]
  s=s[:3] + s[3] + s[3:]
  s=s[:6] + s[6] + s[6:]
  s=s[:6] + s[6] + s[6:]

  strlen = len(s)
  return [s, strlen]

print(getStr("abc"))
print(getStr("xyz"))

test = "test string"
print(test[:1] + test[0])
print(test[1:])