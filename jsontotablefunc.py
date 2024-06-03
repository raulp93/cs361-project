import time

def tablepipeline():

    print("\nWould you like to see the results in a table?")

    viewtable = input("\nEnter response here: ")

    if viewtable == "yes":
        with open("C:\\Users\\raulp\\Documents\\CS361\\projectfile\\jsontotable\\request.txt", "w") as outfile:
            outfile.write("send table")
        
        time.sleep(1.5)

        with open("C:\\Users\\raulp\\Documents\\CS361\\projectfile\\jsontotable\\table.txt", "r") as infile:
            print(infile.read())





