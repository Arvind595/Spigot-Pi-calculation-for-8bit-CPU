import sys

def pi_spigot():
    # Constants from the Pascal code
    n = 100
    length = (10 * n) // 3  # 'div' in Pascal is integer division '//' in Python

    # Initialize array 'a' with 2s. 
    # Pascal arrays are 1-based (1..len). Python is 0-based.
    # We create a list of size (length + 1) and ignore index 0 to match the math logic 
    # (specifically the usage of 'i' in the calculation "2*i - 1").
    a = [2] * (length + 1)

    nines = 0
    predigit = 0

    # Main loop: for j := 1 to n do
    for j in range(1, n + 1):
        q = 0

        # Inner loop: for i := len downto 1 do
        # range(start, stop, step): stop is exclusive, so 0 ensures we reach 1
        for i in range(length, 0, -1):
            x = 10 * a[i] + q * i
            a[i] = x % (2 * i - 1)
            q = x // (2 * i - 1)

        a[1] = q % 10
        q = q // 10

        if q == 9:
            nines += 1
        elif q == 10:
            # write(predigit + 1)
            sys.stdout.write(str(predigit + 1))
            
            # for k := 1 to nines do write(0)
            for k in range(nines):
                sys.stdout.write('0')
            
            predigit = 0
            nines = 0
        else:
            # write(predigit)
            sys.stdout.write(str(predigit))
            predigit = q
            
            if nines != 0:
                # for k := 1 to nines do write(9)
                for k in range(nines):
                    sys.stdout.write('9')
                nines = 0

    # writeln(predigit)
    print(predigit)

if __name__ == "__main__":
    pi_spigot()
