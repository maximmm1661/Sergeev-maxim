# TODO Найдите количество книг, которое можно разместить на дискете
v=1.44
page=100
str=50
simv=25
sim1=4
kol=(simv*str*page*sim1)/1024/1024
book=int(v//kol)
print("Количество книг, помещающихся на дискету:", book)