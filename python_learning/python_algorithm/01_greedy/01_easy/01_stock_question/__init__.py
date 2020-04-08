# encoding:utf-8


class Soultion:
    def maxProfit(self, prices):
        """
        :param prices: 列表
        :return: 输出最大的利润
        """
        max_posix = 0
        for i in range(1, len(prices)):
            temp = prices[i] - prices[i-1]
            if temp > 0:
                max_posix += temp
        return max_posix


if __name__ == '__main__':
    soultion = Soultion()
    print soultion.maxProfit([7, 1, 5, 3, 6, 4])
