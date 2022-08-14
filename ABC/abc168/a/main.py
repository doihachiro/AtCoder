N = input()

h = ["2", "4", "5", "7", "9"]
p = ["0", "1", "6", "8"]
b = ["3"]

if N[-1] in h:
    print("hon")
elif N[-1] in p:
    print("pon")
elif N[-1] in b:
    print("bon")