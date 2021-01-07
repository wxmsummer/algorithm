class Solution:

    def save_data(self, p_dic, a_dic, visit_dic, personID, areaID):
        
        if personID not in p_dic:
            p_dic[personID] = areaID
            visit_dic[personID] = [areaID]
        else:
            
            # 如果不是徘徊，才去更新a_dic
            if areaID not in visit_dic[personID]:
                visit_dic[personID].append(areaID)
                key = p_dic[personID] + areaID
                a_dic[key] += 1

            # 更新 p当前位置
            p_dic[personID] = areaID

        print(a_dic)
        # 使用 visit_dic(set)保存p走过的area
        # p1 - {a1 a2}
        # 若p已走过该area，则a_dic不增加

        # 更新areaDIC
        
        # 更新personDIC

    # 返回值是count，表示有多少个人从from_area 到了 to_area
    # from 和 to 紧邻 即1到2，不能到5
    def getStatistics(self, a_dic, from_area, to_area): 
        return a_dic[from_area + to_area]

if __name__ == '__main__':
    obj = Solution()
    p_dic = {}
    a_dic = {'a1a2':0,'a2a1':0,'a2a3':0}
    visit_dic = {}
    obj.save_data(p_dic, a_dic, visit_dic, 'p1', 'a2')
    obj.save_data(p_dic, a_dic, visit_dic, 'p1', 'a1')
    obj.save_data(p_dic, a_dic, visit_dic, 'p1', 'a2')
    obj.save_data(p_dic, a_dic, visit_dic, 'p1', 'a3')

    print(obj.getStatistics(a_dic, 'a1', 'a2'))
    print(obj.getStatistics(a_dic, 'a2', 'a3'))

# 客流数据化
# 摄像头 上报
# 两个接口 1. 接收数据
# 2. 查询