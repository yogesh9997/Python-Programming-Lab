#Replace multiple spaces with single space in a text file.


def program():
    f1 = open("merge.txt","rt")
    f2 = open("merge1.txt","wt")
    for line in f1:
        f2.write(' '.join(line.split()))
    f1.close()
    f2.close()
program()
