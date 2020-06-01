list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

chunks = [list[x:x+2] for x in range(0,len(list),2)]

print(chunks)
print(chunks[1])