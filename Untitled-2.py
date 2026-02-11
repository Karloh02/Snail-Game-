def snail(map):
    trail = []
    width = 0
    height = 0
    iteracao = 0

    while len(trail) < len(map)**2:

        while width < (len(map) - iteracao):
            trail.append(map[height][width])
            width += 1
           
        
        height += 1
        width -= 1

        while height < (len(map) - iteracao):
            trail.append(map[height][width])
            height += 1
         
   
        width -= 1
        height -= 1

        while iteracao <= width:
            trail.append(map[height][width])
            width -= 1
            

        iteracao += 1
        height -= 1
        width += 1


        while iteracao <= height:
            trail.append(map[height][width])
            height -= 1
            print(width, height)
        
        width += 1
        height += 1
        


    return(trail)

array = [[1,2,3,4,5,6],
         [20,21,22,23,24,7],
         [19,32,33,34,25,8],
         [18,31,36,35,26,9],
         [17,30,29,28,27,10],
         [16,15,14,13,12,11]]

print(snail(array))