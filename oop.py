class Solution:
    def tree(self, row, symbol):
        x = 00
        for i in range(row):
            x += 1
            print(' '*(row-x), (symbol*x)*2)

users = Solution()
height = int(input('Введите высоту ёлки'))
symbol = input('Введите символ :')

users.tree(height, symbol)
