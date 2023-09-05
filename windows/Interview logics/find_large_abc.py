import string

class FindLargeABC:
    def __init__(self):
        

    def compare(flag,ans): 
        for i in userdata:
            if flag:
                pointer = ref.index(i)
            if ref[pointer] == i:
                ans += i
                pointer += 1
                flag  = False
            else:
                update_dict(ans)
                ans = ''
                flag  = True

    def update_dict(ans):
        if len(ans) in ans_dict:
            ans_list.append(ans)
            ans_dict[len(ans)] = ans_list
        else: 
            ans_list.append(ans)
            ans_dict.update({len(ans):ans})


    def large(ans_dict):
        high = 0
        for i in ans_dict:
            if i > high:
                high = i
        print(f'largest len is {high} and its value is {ans_dict[high]}')
    


if __name__ == '__main__':
    userdata = input('input: ')
    ref = string.ascii_lowercase
    ans_dict = {}
    ans = ''
    ans_list = []
    flag = True

    compare(flag,ans)
    if len(ans)>0:
        update_dict(ans)
    large(ans_dict)


