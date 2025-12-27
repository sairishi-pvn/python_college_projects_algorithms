s1 = "ATCGA"
s2 = "AACGT"
s3 = "TTGGT"
s4 = "CACCA"
con=[]
for i in range(len(s1)):
  li=[]
  li.append(s1[i])
  li.append(s2[i])
  li.append(s3[i])
  li.append(s4[i])

  if li.count('A')>len(li)//2:
    con.append('A')
  elif li.count('T')>len(li)//2:
    con.append('T')
  elif li.count('G')>len(li)//2:
    con.append('G')
  elif li.count('C')>len(li)//2:
    con.append('C')
  else:
    con.append('*')
print(con)
for j in range(len(con)):
  if con[j] != '*':
    print(con[j],j)