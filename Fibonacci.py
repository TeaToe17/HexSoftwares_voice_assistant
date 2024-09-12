def Fibonnaci():
    n = int(input("How many terms of the fibonnaci sequnce do you want to generate? "))
    sequence = []
    sequence.append(0)
    sequence.append(1)

    for i in range(n-2):  #Since we have the first two terms already
        Fn1 = sequence[(len(sequence))-1]
        Fn2 = sequence[(len(sequence))-2]

        sequence.append(Fn1+Fn2)

    n = 0
    sum = 0

    for i in sequence:
        sum += sequence[n]
        n += 1

    print(f"number of terms: {len(sequence)}")
    print(f"sequence: {sequence}")
    print(f"The Sum of the first Fifty terms of the Fibonacci Sequence is {sum}")

if __name__ == "__main__":
    Fibonnaci()