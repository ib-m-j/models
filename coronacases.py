import numpy.fft as fastf

f = open('corona_daily_cases.txt','r')

res = []
for l in f.readlines():
    print(l)
    res.append( [int(x) for x in l.split(';')])
    

data = [x[-1] for x in res][12:19]
print(data)
transform1 = fastf.rfft(data)
print(transform1)
print('inverse')
print(fastf.irfft(transform1))
print('testing')
testres = fastf.rfft([0,1,0,7])
print(testres)
print(fastf.irfft(testres))
