# 使用切片功能翻转文本
# seq[a:b] 从位置a开始到位置b结束来对序列进行切片
# 第三个参数可用来确定切片的补偿(step)。默认不长为1
# 他会返回一份连续的文本，如果给定一个负数步长，如-1，将返回翻转过的文本
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    print(reverse(text))
    return text == reverse(text)

something = input('Enter text: ')
if is_palindrome(something):
    print('Yes, it is a palindrome ,')
else :
    print("No, it is not a palindrome")

