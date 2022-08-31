pg = int(input('give a number to check if it is prime'))

count = 0
if pg != 1:

    for pn in range (2, pg):
        if (pg % 2) == 0:
            print(pg, "isn't prime")
            print (pn, 'multiplied by', pg//pn, 'is', pg);

            break

        if (pg % 2 ) != 0 and count == 0:
            count += 1
            print(pg, 'is prime')

        elif count != 0:
            break
            
        