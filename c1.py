data = '<tag1 value = "HelloWorld"><tag2 name = "Name1"></tag2></tag1></tag>'

try:
    data = data.split("><")
except Exception as e:
    print(str(e))
data = [c.replace("<", "").replace(">","") for c in data]

# print(data)

# data = ["<tag1 att = 'val' attr1 = 'val3'>", "<tag2 attr = 'val2'>", "<tag3 att3 = 'val3'>", "</tag3>", "</tag2>", "</tag1>"]
quer = "tag1.tag2~name tag1~name tag1~value"
q = quer.split()





tags = []
ans = {}

for _ in data:
    tagContent = _.split(" ")


    tag = tagContent[0]

    if tag.startswith("/"):
        try:
            tags.pop()
        except Exception as e:

    else:
        tags.append(tag)
    attrVal = {}
    if len(tagContent) > 0:
        for _ in range((len(tagContent)-1)//3):
            attrVal[tagContent[1 + (3 * _)]] = tagContent[3 + (3*_)].replace("\"", "")

    ansKey = ""

    ansKey = ".".join(tags)

    for k, v in attrVal.items():
        ans[ansKey+"~"+k] = v

q = "tag1~value"

fA = "Not found!!!"
for k in ans.keys():
    if q in k:
        fA = ans.get(k)

print(fA)
