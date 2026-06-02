#library management system
book = {
    "name": "test",
    "author": "somebody"
}

def add_book():
    name = input("enter book title: \t").lower()
    author = input("enter book author: \t").lower()
    book["name"] = name
    book["author"] = author
    with open("library.txt", "a") as file:
        try:
            file.write(f"{book["name"]} \t {book["author"]} \n")
        except Exception as e:
            print(e)
    with open("available.txt", "a") as n_file:
                n_file.write(f"{book["name"]} \t {book["author"]} \n")
                #reminder replicate remove when borrowed
                #adding all the books edge case

def view_books():
    with open("library.txt","r") as file:
        try:
            file = file.readlines()
            print("book \t | author")
            for line in file:
                print(line)
        except Exception as e:
            print(e)

def borrow_book():
    name_of_book = input("book name: \t")
    name_of_lender = input("your name: \t")
    temp = []
    with open("available.txt", "r+") as file:
        lines = file.readlines()
        
        for line in lines:
            line = line.split("\t") #" \t "
            book = line[0]
            temp.append(book)
            print(book, temp)

            if name_of_book.strip() == book.strip():
                # print("hit")
                # # print("here")
                with open("borrowed.txt", "a+") as b_file:
                    try:
                        b_file.write(f"{name_of_lender} \t {name_of_book} \t{line[-1]} ")
                        print(f"{name_of_lender} succesfuly borrowed {name_of_book} by {line[-1]}")
                    except Exception as e:
                        print(e)
        

      
        index = 0
        for line in lines:
            line = line.split("\t")
            name_of_book = name_of_book.strip()
            target = line[0].strip()
            if name_of_book == target:
                lines.pop(index)
            index += 1
    with open("available.txt", "w") as file:
        file.writelines(lines)
        # print(lines)
    # print("end line")
    # print(temp)
    name_of_book = name_of_book + " "
    if not name_of_book in temp:
        print("not available")
        view_books()
        borrow_book()
    
    
def return_book():
    book_return = input("what book are you returning")
    with open("borrowed.txt", "r+") as file:
        upload = file.readlines()
        line_count = 0
        print(upload)
        for line in upload:
            if line == " ":
                continue
            else:
                line = line.split(" \t ")
                book = line[1]
                lender = line[0]
                line_count += 1

            #add to available
            if book_return == book:
                with open("available.txt", "a+") as a_file:
                    a_file.write(f"{line[1]} \t {line[2]} \n")
                    target_line = line_count - 1
                    print(f"{line[0]} returned {line[1]} succesfully")
            print(lender)
        # update borrowed list
        line_count = 0

        for line in upload:
            if line == " ":
                continue
            else:
                line_T = line.split(" \t ")
                print(line_T, "pre error", upload)
                if line_T == " ":
                    print("empty")
                    continue
                elif line_T[1] == book_return:
                    print(f"line{line_count}")
                    upload.pop(line_count)
                line_count += 1
    with open("borrowed.txt", "w") as filer:
        filer.writelines(upload)
        print(upload, "end")
        # for line in upload:
        #     print(line, line_count, target_line)
        #     if line_count == target_line:
        #         continue
        #     else:
        #         file.write(line)

def search_library():
    print("God Abeg!!!")
    search = input("\t enter title of book")
    with open("available.txt", "r") as file:
        entries = file.readlines()
        for entry in entries:
            present = entry
            # print ("start", present)
            if entry == " ":
                continue
            else:
                entry = entry.split(" \t ")
                if entry[0] == search:
                    print(entry, "found")
                    #to be completed

def display_availabilty(area):
    available = []
    borrowed = []
    if area == "available":

        with open("available.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                available.append(line)
            print(f"available books are \n")
            for i in available:
                print(i)
    elif area == "borrowed":
        with open("borrowed.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                borrowed.append(line)
            print(f"borrowed books are \n")
            for i in borrowed:
                print(i)
        






# add_book()
# view_books()
# borrow_book()
# return_book()
# search_library()
display_availabilty("borrowed")
# print(book)