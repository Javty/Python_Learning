if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

def list (x,y,z,n):
    final_list = []
    for value_1 in range(x+1):
        for value_2 in range(y+1):
            for value_3 in range(z+1):
                temp_list = [value_1,value_2,value_3]
                if sum(temp_list) != n:
                    final_list.append(temp_list)
    return final_list

print(list(x,y,z,n))
