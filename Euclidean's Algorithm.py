#Eucledean's Algorithm Bacis


#gcd(1, 0) _>
#gcd(10, 10
import math
from math import ceil
from math import floor


def euclidean(a, b, *kwarg) -> int:

    #Checking for rule 1 GCD(100, 0) --> 100
    if b == 0:
        print("GCD(%d, %d) is %d"%(a, b,a))
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
        print("Quotient: ", q, "Divisor:", a, "Devident:", b, "Reminder:", r, '\n')

        #swapping the Values of A and B
        a  =  b
        b = r

        # Checking if the Value of b turn to 0 other wise rule no 1 GCD(a, b=0) gcd is a

        if b == 0:
            print("GCD(%d, %d) is %d" % (a_val, b_val, a))
            # gcd(10, 0)








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

        except Exception:
            print("Error Occured")


