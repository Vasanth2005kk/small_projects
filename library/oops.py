
class library():

    def __init__(self,booknames):
        
        self.booknames=booknames
        self.copy_booknames=booknames.copy()
        #print(self.copy_booknames)

    def all_books(self):
        
        return self.booknames
    
    def get_books(self,book_name="book3"):

        if book_name in self.copy_booknames :
            self.copy_booknames.pop(book_name)
            print("----- SUCCESSFULLY ! -----")
        
        else:
            print("----- THE BOOK NAME NOT IN LIBRARY ! -----")
        
        

    def available_books(self):
        list_1=[]
        for i in self.copy_booknames:
            list_1.append(i)
        if list_1:
            return list_1
        
        return list(["----- ALL BOOK IS NOT AVELABLE ! -----"])
    
    
    def outof_stack(self):
        for i in self.booknames:
            outof_s=[]
            if i not in self.copy_booknames:
                outof_s.append(i)
        return outof_s
    
    def admin(self,user_name , password ):
        if user_name == "vasanth" and password == "2005" :
            book_name=input("ENTER THE BOOK NAME :")
            book_author=input("ENTER THE AUTHOR NAME :")
            def add_book(x,y):
                with open("//home//vasanth//All_Repositories//libray//books.txt","a") as file_1:
                    file_1.write(f"{x},{y}\n")
                    print("----- SUCCESSFULLY ! -----")
            add_book(book_name,book_author)

    def book_name_to_author_name(self,book_name):
        return self.booknames.get(book_name,"--- THIS BOOK NOT AVAILABLE ---")
    

