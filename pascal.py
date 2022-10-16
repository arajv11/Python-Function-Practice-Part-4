def pascal(n):
    if (n < 1):
        print("Not enough rows")
    elif (n == 1):
        print("1")
    elif (n == 2):
        print("1")
        print("1 1")
    else:
        print("1")
        print("1 1")

        row_list = [1, 1]
        row_number = 3
        def new_rows(row_list, row_number):
            while (row_number <= n):
                current_row = [1]
                output_string = "1"
                for i in range (1, len(row_list)):
                    current_row.append(row_list[i-1] + row_list[i])
                    output_string += f" { current_row[i] }"
                output_string = f"{output_string} 1"
                print(output_string)
                current_row.append(1)
                row_list = current_row
                row_number += 1
        new_rows(row_list, row_number)

print("Pascal 0")
pascal(0)
print("Pascal 1")
pascal(1)
print("Pascal 2")
pascal(2)
print("Pascal 3")
pascal(3)
print("Pascal 4")
pascal(4)
print("Pascal 5")
pascal(5)