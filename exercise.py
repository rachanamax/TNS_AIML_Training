def check_marks(marks):
    for m in marks:
        if(m>90):
            print(f"A -> {m}")
        elif(75<m<89):
            print(f"B -> {m}")
        elif(60<m<74):
            print(f"C -> {m}")
        elif(40<m<59):
            print(f"D -> {m}")
        else:
            print(f"F -> {m}")

marks=[95,82,72,55,30]
check_marks(marks)