a=int(input())
for a in range(a):
    n=input("Enter a name: ")
    ID=input("Admission ID: ")
    cap=input("CAP Rank: ")
    print()
    print('Hi {},\n\nCongratulations...!\n{} You got selected for next round of recruitment process submit your academic credential including primary and secondary certificates. Your admission ID is {} and will be eligible for the next round of interview with a CAP rank of {} If you submit all the documents on time and process university might offer you a scholarship.'.format(n.capitalize(),n.capitalize(),ID,cap))