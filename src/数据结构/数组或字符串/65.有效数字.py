# 验证给定的字符串是否可以解释为十进制数字。
#
# 例如:
#
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false
#
# 说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：
#
# 数字 0-9
# 指数 - "e"
# 正/负号 - "+"/"-"
# 小数点 - "."
# 当然，在输入中，这些字符的上下文也很重要。

class Solution:
    def isNumber(self, s: str) -> bool:
        # 画出状态转移表，结构为states[n]存储n个状态
        # states = [
        #     {'b':0,'s':1,'d':2,'.':4},  # 0. start
        #     {'d':2,'.':4},              # 1. 正负号在指数前面
        #     {'d':2,'.':3,'e':5,'b':8},  # 2. 数字在小数点前面
        #     {'d':3,'e':5,'b':8},        # 3. 小数点和数字
        #     {'d':3},                    # 4. 小数点前没有数字
        #     {'s':6,'d':7},              # 5. 'e'
        #     {'d':7},                    # 6. 正负号在e之前
        #     {'d':7,'b':8},              # 7. 数字在e之前
        #     {'b':8}                     # 8. 结束
        # ]
        states = [
            {'b':0,'s':1,'d':6,'.':2},
            {'d':6,'.':2},
            {'d':3},
            {'b':8,'e':4,'d':3},
            {'s':7,'d':5},
            {'b':8,'d':5},
            {'b':8,'d':6,'.':3,'e':4},
            {'d':5},
            {'b':8}
        ]
        p = 0
        for c in s:
            if '0' <= c <= '9': typ = 'd'
            elif c == ' ':typ = 'b'
            elif c == '.':typ = '.'
            elif c == 'e':typ = 'e'
            elif c in "+-":typ = 's'
            else: typ = '?'
            if typ not in states[p]:return False
            p = states[p][typ]
        return p in [3,5,6,8]