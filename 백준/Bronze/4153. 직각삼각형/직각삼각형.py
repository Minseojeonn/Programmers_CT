while True:
    inputs = list(map(int, input().split()))
    if all(i==0 for i in inputs):
        break
    else:
        s_inputs = sorted(inputs)
        if s_inputs[-1]**2 == s_inputs[0]**2 + s_inputs[1]**2:
            print("right")
        else:
            print("wrong")


