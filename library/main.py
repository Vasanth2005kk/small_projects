import oops as lib
import random

code=random.randrange(1000,10000)
    

print("{msg:^50}".format(msg="---------- wellcome to library -----------".upper()))

print("\n1. All BOOKS VIEW ")
print("2. available_books".upper())
print("3. outof stack".upper())
print("4. get book ".upper())
print("5. book name to author name check ".upper())
print("6. uplode book ".upper())
print(f"\n-------------\n| ADMIN KEY |  ==> {code} \n-------------")
print("\n{msg:^30}".format(msg="<<< EXIT >>>\n"))

def json_format():
    import re
    dic={}
    with open('//home//vasanth//All_Repositories//libray//books.txt',"r") as f:
        for i in f:
            output=re.split("[\n]|,",i)
            dic.update({output[0]:output[1]})
    return dic

def style(a,b):
    s="-"*int(len(a)+4+len(b)+3)
    print(f"{s}\n| {a} | {b} |\n{s}")

output=lib.library(json_format())

while True:

    keys=input("\nENTHR THE KEY :").lower()

    if keys == "1":
        for i in json_format().keys():
            print(i)

    elif keys == "2":
        for i in output.available_books():
            print(i)

    elif keys == "3":
        stack=output.outof_stack()
        for i in stack:
            print(i)
            
        if not(stack):
            print("--- NO OUTOF STACK ---")    

    elif keys == "4":
        book_name=input("\nENTER THE BOOK NAME :")
        output.get_books(book_name=book_name)

    elif keys == "5":
        book_name=input("ENTER THE BOOK NAME :")
        au=output.book_name_to_author_name(book_name=book_name)
        
        for a,b in json_format().items():
            if a == book_name:
                style(a,b)

    elif keys == "6":
        key=input("ENTER CODE :")
        if key == str(code):
            user_name=input("USER_NAME :")
            password=input("PASSWORD :")
            output.admin(user_name,password)

        else:
            print("--- NOT THIS CODE ! ---")

    elif keys == "exit":
        break

    else:
        print("{msg:^50}".format(msg="\n---------- NOT THIS KEY ! -----------\n".upper()))