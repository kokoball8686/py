citys = ['seoul', 'daejeon', 'kimpo', 'suncheon', 'pusan']


#
# for i in citys:
#     #print(len(i))
#
#
#
#     print(list(len(i)))
#



longest_city = max(citys, key=len)
shortest_city = min(citys, key=len)
print('Long Name City : ', longest_city)
print('Short Name City : ', shortest_city)

