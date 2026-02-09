def palindrome(tup):
    end=len(tup)-1
    start=0
    while(start<end):
        if(tup[start]!=tup[end]):
            return False
        start=start+1
        end=end-1
    return True 
t=(1,2,3,2,1)
if (palindrome(t)):
    print("palindrome")
else:
    print("not palindrome")