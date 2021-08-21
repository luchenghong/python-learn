# chats

# 读取档案
def read_file(filename):
    chats = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            chats.append(line.strip())
    return chats
# 转换格式 [名字:语句]的格式
def convert(chats):
    new = []
    person = None
    for c in chats:
        if c == 'Allen':
            person = 'Allen'
            continue
        elif c =='Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ':' + c)
    return new

#写入档案
def write_file(filename, chats):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for c in chats:
            f.write(c + '\n')

def main():
    input_file_name = 'input.txt'
    output_file_name = 'output.txt'
    chats = read_file(input_file_name)
    chats = convert(chats)
    write_file(output_file_name, chats)

if __name__ == '__main__':
    main()
