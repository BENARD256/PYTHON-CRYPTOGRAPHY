#Eucledean's Algorithm Bacis


#gcd(1, 0) _>
#gcd(10, 10
import math
from math import ceil
from math import floor
from tabulate import tabulate


def euclidean(a, b, *kwarg) -> int:

    t_1=s_2 = 0
    t_2=s_1 = 1

    #Checking for rule 1 GCD(a, 0) --> a
    if b == 0:

        data = [
            ["GCD(%d, %d) is" % (a, b), a]
        ]

        tabulated = tabulate(data,  tablefmt="grid")
        print(tabulated)
        #gcd(10, 0)



    #Swapping if B is Greater than A
    if b > a:
        c = a
        a = b
        b = c

    #preserve the original values of a, b so that they can be referenced later

    a_val = a
    b_val = b

    #print("Divisor:", a, "Devident:", b, "\n\n")


    while b != 0:

        answer = a / b
        r = (a - (floor(answer)*b)) #Calculating the Reminder

        q = floor(answer) #getting the Quotient using the floor devision

        t = t_1 - q*(t_2)

        s = s_1 - q*(s_2)


        header = ["Quotient","Divisor", "Devident","Reminder", "S_1=1", "S_2=0", "S", "T_1=0", "T_2=1", "S"]
        data = [

            [q, a, b, r, s_1, s_2, s, t_1, t_2, t]
        ]

        tab = tabulate(data, tablefmt="grid", headers=header)
        print(tab)
        #swapping the Values of just as applied in the tabled Euclid Algorithm
        t_1 = t_2
        t_2 = t

        s_1 = s_2
        s_2 = s

        a = b
        b = r

        #Checking if the Value of b turn to 0 other wise rule no 1 GCD(a, b=0) gcd is a
        if b == 0:
            #print("\nDivisor:", a, "Devident:", b, "S_1:", s_1, "S_2:", s_2, "S:", s,"T_1:", t_1, "T_2:", t_2,'\n')

             # gcd(10, 0)
            data = [

                [a, b,s_1, s_2, s, t_1, t_2]
            ]

            header = [
                "Divisor", "Devident", "S_1","S_2", "S", "T_1", "T_2"
            ]
            tab = tabulate(data, tablefmt="grid", headers=header)
            print("\n\n\n",tab)

            print("GCD(%d, %d) is %d" % (a_val, b_val, a))


def main(a, b) -> int:
    return euclidean(a, b)


if __name__ == "__main__":


    while True:
        try:

            prompt_1 = int(input("\n\nFirt Number: "))
            prompt_2 = int(input("Second number: "))

            main(prompt_1, prompt_2)

        except ValueError:
            print("Numbers Expected")

        except Exception as e:
            print(e, "Error Occured")


