def starPatternInverse():
    for i in range(0, 8):
        for j in range(i, 8):
            print("* ", end="")
        for k in range(0, i):
            print("  ", end="")
        if(i>0):
            for m in range(0, i):
                print("  ", end="")
        for n in range(8, i, -1):
            print("* ", end="")
        print()

def starPatternDiamond():
    for i in range(0, 8):
        if (i<5):
            for j in range(i, 5):
                print("  ", end="")
            for k in range(0, i):
                print("* ", end="")
            if(i>0):
                for m in range(0, i-1):
                    print("* ", end="")
            print()
        else:
            for j in range(5, i+2):
                print("  ", end="")
            for k in range(i, 8):
                print("* ", end="")
            if(i>4):
                for m in range(8, i+1, -1):
                    print("* ", end="")
            print()

starPatternInverse()
starPatternDiamond()
        
