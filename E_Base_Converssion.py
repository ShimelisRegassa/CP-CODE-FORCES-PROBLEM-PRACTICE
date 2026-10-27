for _ in range(int(input())):
    n=int(input())
    def recursion(n):
        if(n==0):
            return ""
        return str(n%2)+recursion(n//2)
    print(recursion(n)[::-1])
        