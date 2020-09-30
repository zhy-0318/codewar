#-*-coding:utf-8-*-
def longest(s1, s2):
    s3=""
    for i in s1:
        for j in s2:
            if i>='a'and i<='z'and j>='a' and j<='z':
                if i not in s3:
                    s3+=i
                if j not in s3:
                    s3+=j
            else:
                return "请重新输入只包含字母的字符串！"
    return ''.join(sorted(s3))


def longest1(s1,s2):
    return ''.join(sorted(set(s1+s2)))


if __name__ == '__main__':
    s1 = raw_input("请输入第一个字符串:")
    s2 = raw_input("请输入第二个字符串:")
    s3 = longest(s1,s2)
    s4 = longest1(s1,s2)
    print s3
    print s4