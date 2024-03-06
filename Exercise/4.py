def m(d1,d2):
    return{key:d1.get(key,0)+d2.get(key,0) for key in set(d1)|set(d2)}
da={"a":10,"b":0,"c":30}
db={"b":1,"c":15,"d":25}
print(m(da,db))