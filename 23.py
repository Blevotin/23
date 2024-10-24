def custom_write(file_name, *strings):
    list(strings)
    with open(file_name, 'w', encoding="utf-8") as file:
        print(file.tell())
        a = 0
        for i in strings:
            a += 1
            file.write(f"{i}\n")
            kr = (a, file.tell())
            print({kr:i})



custom_write("2", "gf", "gf", "gf", "gf")
