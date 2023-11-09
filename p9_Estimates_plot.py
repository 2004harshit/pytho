from statistics import mean
import matplotlib.pyplot as plt
import statistics
Estimates=[1000,1010,1786,2000,1500,100,120,150,150,150,170,175,100,197,200,200,400,500,600,788,142,169,256,300,789,958,589,654,456,489,258,741,369,478,874]
y=[]
Estimates.sort()
tv=int(0.1*len(Estimates))
Estimates=Estimates[tv:]
Estimates=Estimates[:len(Estimates)-tv]
for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates,y,'r--')
plt.plot([statistics.mean(Estimates)],[5],'ro')
plt.plot([statistics.median(Estimates)],[5],'bs')
plt.plot([375],[5],'g^')
plt.show()