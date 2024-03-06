def cas(studentscores):
    return {name:sum(scores)/len(scores) for name,scores in studentscores}
ssl=[("Amudhan",[90,90,90]),("Mohan",[80,80,80])]
result=cas(ssl)
print(result)