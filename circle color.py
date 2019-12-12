alex.color("green")    # alex has a color
alex.right(60)         # alex turns 60 degrees right
alex.left(60)          # alex turns 60 degrees left

color = ["green", "blue", "red"]
for i in range(0,3):
    alex.color(color[i])
    for counter in range(1,5):
       alex.circle(20*counter)
    alex.right(120)
    alex.left(0)
    
