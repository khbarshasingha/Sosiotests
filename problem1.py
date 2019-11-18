n= int(input())

emails=[]
for _ in range(0,n):
    email=input()
    emails.append(email)

for em in emails:
    if '@' in em and '.com' in em:
        print(em)
