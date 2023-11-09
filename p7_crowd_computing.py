from statistics import mean
from scipy import stats
Estimates=[1000,1010,1786,2000,1500,100,120,150,150,150,170,175,100,197,200,200,400,500,600,788,142,169,256,300,789,958,589,654,456,489,258,741,369,478,874]
Estimates.sort()
# sum=0
# for i in range (len(Estimates)):
#    print(Estimates[i])
    # sum=sum+Estimates[i]
# print(sum)
# print(len(Estimates))     
# calculation by manually
tv=int(0.1*len(Estimates))
Estimates=Estimates[tv:]
Estimates=Estimates[:len(Estimates)-tv]
print(mean(Estimates))


# using stats.trim_mean() function
m=stats.trim_mean(Estimates,0.1)
print(m)