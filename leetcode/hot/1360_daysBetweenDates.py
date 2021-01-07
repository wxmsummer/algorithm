# 计算日期之间间隔
class Solution:
    
    # 判断是否是闰年：是否是400的整数倍 或 是4的倍数但不是100的整数倍
    def leap_year(self, year):
        return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

    # 将日期减去1971/1/1，得到日期天数
    def date_to_int(self, year, month, day):
        month_length = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ans = day - 1
        # 计算当年经过的天数
        while month != 0:
            month -= 1
            ans += month_length[month]
            if month == 2 and self.leap_year(year):
                ans += 1
        # 根据年份计算天数
        ans += 365 * (year - 1971)
        # 计算闰年的数量
        # 先加上模4为0的年份数量，此时多加了一些模100为0的非闰年
        ans += (year - 1) // 4 - 1971 // 4
        # 再减去模100为0的年份数量，此时多减了一些模400为0的闰年
        ans -= (year - 1) // 100 - 1971 // 100
        # 再加上模400为0的年份数量
        ans += (year - 1) // 400 - 1971 // 400
        return ans

    def daysBetweenDates(self, date1:str, date2:str) -> int:
        # 分割字符串并转换为数组
        date1 = [int(i) for i in date1.split('-')]
        date2 = [int(i) for i in date2.split('-')]
        return abs(self.date_to_int(*date1) - self.date_to_int(*date2))