def count_num_in_file(file_path, num):
    count = 0
    with open(file_path,"r") as f:
        for line in f.readlines():
            tokens = line.split(",")
            count += count_num_in_tokens(tokens, num)

    return count

def count_num_in_tokens(tokens, num):
    count = 0
    for token in tokens:
        if num == int(token):
            count+=1
    return count


def sum_numbers(file_path):
    output_lines = []
    with open(file_path,"r") as f:
        for line in f.readlines():
            tokens = line.split(",")
            total = sum_tokens(tokens)
            output_lines.append("sum: " + str(total) + " | " + line)
    with open(file_path,"w") as f:
        f.writelines(output_lines)

def sum_tokens(tokens):
    sum = 0
    for token in tokens:
        sum += int(token)
    return sum

sum_numbers("C:\\Code\\Py\\Basics\\input.txt")