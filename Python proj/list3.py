num=[12,75,150,180,145]
for i in num:

  if i > 150:
    continue
  elif i > 500:
    break
  elif i % 5 == 0:
    print(i)
    