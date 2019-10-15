#import modul NewtonA

import NewtonA

def main():
    #rumus newton 1
    f = 4

    newton1 = NewtonA.n1(f)

    print("newton1")
    print("gaya\t: ", f)
    print("newton1\t= ", newton1)

    #rumus newton2
    m = 80
    a = 9

    newton2 = NewtonA.n2(m, a)

    print("newton2")
    print("massa\t: ", m)
    print("percepatan\t= ", a)
    print("newton2\t= ", newton2)

    #rumus newton3
    m = 200
    g = 10

    newton3 = NewtonA.n3(m, g)
    
    print("\newton3")
    print("massa\t: ", m)
    print("gravitasi\t= ", g)
    print("newton3\t= ", newton3)
    
if __name__ == "__main__":
    main()


    
