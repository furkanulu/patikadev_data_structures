def merge_sort(arr_list):
    if len(arr_list) > 1:
  
         # Listenin orta noktası
        mid = len(arr_list)//2
  
        # Listenin sol kısmı
        L = arr_list[:mid]
  
        # Listenin sağ kısmı
        R = arr_list[mid:]
  
        # Sol kısmı sıralamak için fonksiyonu tekrar çağır
        merge_sort(L)
  
        # Sağ kısmı sıralamak için fonksiyonu tekrar çağır
        merge_sort(R)
  
        i = j = k = 0
  
        # Veriyi L[] ve R[] geçici listelerine kopyala 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr_list[k] = L[i]
                i += 1
            else:
                arr_list[k] = R[j]
                j += 1
            k += 1
  
        # Eleman kalıp kalmadığını kontrol et
        while i < len(L):
            arr_list[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr_list[k] = R[j]
            j += 1
            k += 1


def merge_sort_function(num_list):
    sorted_list=num_list.copy()
    merge_sort(sorted_list)
    return sorted_list

def main():
    num_list = [16,21,11,8,12,22,1] 
    x=merge_sort_function(num_list)
    print(x)

if __name__ == "__main__":
    main()