
# this is the HTML input
data = '<tag1 value = "HelloWorld"><tag2 name = "Name1"></tag2></tag1></tag>'

# making html string for a better string play
data = data.split("><")
data = [c.replace("<", "").replace(">", "") for c in data]

tags = []  # this would be used to store tags 
ans = {}  # this would be storing 
for _ in data:
    tagContent = _.split(" ")
    tag = tagContent[0]
    
    # if it gets closure of a tag, it start removing from last 
    if tag.startswith("/"):
        tags.pop()
    else:
        tags.append(tag)
        
    attrVal = {}  # it would be used to store attributes of the current tag
    if len(tagContent) > 0:
        for _ in range((len(tagContent)-1)//3):
            attrVal[tagContent[1 + (3 * _)]] = tagContent[3 + (3*_)].replace("\"", "")

    ansKey = ""
    ansKey = ".".join(tags)

    for k, v in attrVal.items():
        ans[ansKey+"~"+k] = v

q = "tag1~value"

fA = "Not found!!!" # this variable would print the exact answer we need
for k in ans.keys():
    if q in k:
        fA = ans.get(k)

print(fA)
