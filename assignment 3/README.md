 Variable operations exercises
 1. subnr_str because you can contanate string with a string but not an integer
 2. 
    
        print(sub_code + " "  + subnr_str ) 
        print(sub_code + " "  +(subnr_str*3))
        print((sub_code + subnr_str)*3)
        print((sub_code*3)+(subnr_str*3))

List operations exercises

 1. 
        
        numlist = [1,2,3]
        print(numlist *2)

 2. The numbers in the array are doubled instead of the actual array unlike the list which is multiplied 3 times
       
        numarr = np.array([1,2,3])
        print(numarr*2)

 3. 
        
        print([strlist[0]*2,strlist[1]*2,strlist[2]*2,strlist[3]*2])

        print(strlist*2)

        print([strlist[0],strlist[0],
              strlist[1],strlist[1],
              strlist[2],strlist[2],
              strlist[3],strlist[3]])
       
        print([[strlist[0],strlist[0]],
              [strlist[1],strlist[1]],
              [strlist[2],strlist[2]],
              [strlist[3],strlist[3]]])

Zipping exercises

    import numpy as np

    first_list = []
    second_list= []

    imgs_house = ['house1.png'] * 5 + ['house2.png'] * 5 + ['house3.png'] * 5 + ['house4.png'] * 5 + ['house5.png'] * 5
    
    imgs_face = ['face1.png'] * 5 + ['face2.png'] * 5 + ['face3.png'] * 5 + ['face4.png'] * 5 + ['face5.png'] * 5
    
    Cues = ['Cue1'] * 50 + ['Cue2'] * 50

    first_list.extend(imgs_face)
    first_list.extend(imgs_house)
    first_list.extend(imgs_face)
    first_list.extend(imgs_house)
    img_fs = ['face1.png', 'face2.png', 'face3.png', 'face4.png', 'face5.png'] * 5
    img_hs = ['house1.png', 'house2.png', 'house3.png', 'house4.png', 'house5.png'] * 5

    second_list.extend(img_hs)
    second_list.extend(img_fs)
    second_list.extend(img_hs)
    second_list.extend(img_fs)
    catimgs = list(zip(first_list, second_list, Cues))
    np.random.shuffle(catimgs)
    print(catimgs)


indexing exercises

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    print(colors[4])
    print(colors[4][2])
    print(colors[4][3])
    colors.remove('purple')
    colors.append('indigo')
    colors.append('violet')
    print(colors)

Slicing exercises

    list1 = list(range(0,101))
    print(list1)
    print(list1[:10])
    print(list1[1:101:2][::-1])
    print(list1[97:101][::-1])

    list2 = [39,40,41,42,43]
    print(list2 == list1[39:44] ) 
yes they are the same because the 40th number would be at the 39th index and the 44th number would be at the 43rd index

