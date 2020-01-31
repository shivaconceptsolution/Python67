basic =int(input("enter basic"))
ta = int(input("enter ta"))
da = int(input("enter da"))
comm = int(input("enter commision"))
pf = int(input("enter pf"))
lv = float(input("enter leave"))
tsal = basic+ta+da+comm
nsal= tsal-pf-(tsal/30)*lv
print("Net Salary Is",nsal)
