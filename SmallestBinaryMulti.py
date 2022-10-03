#Given a number A, find the smallest number which has only 1s and 0s as its digits which are divisible by the number A.
#Solution 

def GetMiniumBinaryDigit (A):
   # QUEUE/LIST FOR BREATH FIRST SEARCH
    q = []

   #constructor for visited remainder list / string 1 to first to be pushed
    checkedRem = set([])
    t = '1'
    q.append(t)
   #to avoid evulating the same number, each number that has looked at has 1 or 0 added before appended
    while q:
        t = q.pop(0)
        rem = int(t) % A
        if rem == 0:
            return t
        if rem not in checkedRem:
            checkedRem.add(rem)
            q.append(t+'0')
            q.append(t+'1')


#Test code - type any value to verify 
n = input("Enter value: ")
n = int(n)
print(GetMiniumBinaryDigit(n))
