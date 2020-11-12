max_chars=256
def findSmallestWindow(string):
    n=len(string)
    dist_count=len(list(set([i for i in string])))
    start,start_index,min_len,count=0,-1,n,0
    curr_count=[0 for i in range(max_chars)]
    for j in range(n):
        curr_count[ord(string[j])]+=1
        if curr_count[ord(string[j])]==1:
            count+=1
        if count==dist_count:
            while curr_count[ord(string[start])]>1:
                if curr_count[ord(string[start])]>1:
                    curr_count[ord(string[start])]-=1
                start+=1
            len_window=j-start+1
            if min_len>len_window:
                min_len=len_window
                start_index=start
    return min_len
if __name__=='__main__':
    print("smallest window size containing all characters is:",findSmallestWindow("aaab"))