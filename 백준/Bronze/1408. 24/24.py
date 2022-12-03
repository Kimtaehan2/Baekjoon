H, M, S = map(int, input().split(':'))
h, m, s = map(int, input().split(':'))
t = h*3600+m*60+s - (H*3600+M*60+S)
if t < 0:
    t += 60*60*24
rh = t//3600 
rm = (t%3600)//60 
rs = t%60
print("%02d:%02d:%02d" % (rh,rm,rs))