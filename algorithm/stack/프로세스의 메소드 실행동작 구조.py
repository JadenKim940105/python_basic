def recursive(data):
    if data < 0:
        print("end")
    else:
        print(data)
        recursive(data - 1)
        print("return data ", data)

