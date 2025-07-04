x, y, w, h = map(int, input().split())

# (0, 0) 이나 (w, h) 중 1에 닿아야..

toleft_x = abs(0 - x)
toleft_y = abs(0 - y)

toright_x = abs(w - x)
toright_y = abs(h - y)

dis = [toleft_x, toleft_y, toright_x, toright_y]
dis.sort()

print(dis[0])