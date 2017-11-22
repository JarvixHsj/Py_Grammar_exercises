# 定义可忽略的元祖
# 循环忽略元祖的内容，并将字符串内对应的字符替换为空
ignore = '#@'
def removeSpecial(text, specialStr):
    #循环字符串
    for i in text:
        # 判断字符串的每个字符是否 是特殊字符
        if i in specialStr:
            #如果是则替换为空（移除）
            text = text.replace(i,'')
    return text

def reverse(text):
    return text[::-1]


something = input('Enter Str :')
text = removeSpecial(something,ignore)
print(text)
if text == reverse(text):
    print('相等')
else:
    print('不相等')



# def filterAndreverse(text,list):
#     for i in list:
#         if i in text:
#             print(i,text)
#         else :
#             print('none')
#         text.find(i)
#
# list = ['@','#']
# something = input('Endter value :')
#
# filterAndreverse(something, list)

