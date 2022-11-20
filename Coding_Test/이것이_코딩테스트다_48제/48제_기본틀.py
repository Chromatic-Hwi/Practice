import psutil



print()
p=psutil.Process()
rss=p.memory_info().rss/2**20
print(rss, "MB")


"""



"""
