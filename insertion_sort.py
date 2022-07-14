def insertion_sort(num_list):
    for i in range(len(num_list)):
        min_num=num_list[i]
        u = num_list[i]
        u_i=i
        for j in range(i+1, len(num_list)):
            if min_num > num_list[j]:
                min_num=num_list[j]
                u_i=j

        num_list[i]  = min_num
        num_list[u_i] = u
    
    return num_list

def main():
    num_list = [22,27,16,2,18,6]
    x = insertion_sort(num_list)
    print(x)

if __name__ == "__main__":
    main()