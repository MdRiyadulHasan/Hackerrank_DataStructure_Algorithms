def count_substring(string, sub_string):
    length_s=len(string)
    length_sub=len(sub_string)
    c=0
    for i in range(length_s):
        if string[i:i+length_sub]==sub_string:
            c=c+1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)