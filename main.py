current_weight= float(input("请输入你当前的体重(kg):"))
annual_increase=0.5
years=10
print("{:<5}{:<15}{:<15}".format("年份","地球体重(kg)","月球体重(kg)"))
print("-"*35)
for year in range(1,years+1):
    earth_weight=current_weight+annual_increase*year
    moon_weight=earth_weight*0.165
    print("{:<5}{:<15.2f}{:<15.2f}".format(year,earth_weight,moon_weight))
