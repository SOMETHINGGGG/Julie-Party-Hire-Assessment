from tkinter import *

def quit():
    main_window.destroy()

def print_hire_details():
    name_count = 0
    print("Row\tname\tReceipt number\t\tItem Hired\tNumber Hired")
    while name_count < counters['total_entries']:
        print(name_count, "\t", customer_details[name_count][0], "\t\t", customer_details[name_count][1], "\t\t", customer_details[name_count][2], "\t", customer_details[name_count][3])
        name_count += 1
        counters['name_count'] = name_count

def append_name():
    customer_details.append([entry_customer_name.get(), entry_receipt_number.get(), entry_hire_item.get(), entry_number_hired.get()])
    current_customer_name = entry_customer_name.get()
    entry_customer_name.delete(0,'end')
    entry_receipt_number.delete(0,'end')
    entry_hire_item.delete(0,'end')
    entry_number_hired.delete(0,'end')

def delete_row ():
    del customer_details[int(delete_item.get())]
    counters['total_entries'] -= 1
    delete_item.delete(0,'end')

def main():
    total_entries = 0
    Label(main_window, text="Customer Name") .grid(column=0,row=0)
    Label(main_window, text="Receipt Number") .grid(column=0,row=1)
    Label(main_window, text="Item Hired") .grid(column=0,row=2)
    Label(main_window, text="Number Hired") .grid(column=0,row=3)
    Label(main_window, text="Row #") .grid(column=3,row=2=)

    Button(main_window, text="Quit",command=quit,width= 10) .grid(column=5, row=0)
    Button(main_window, text="Append Details",command=append_name) .grid(column=3, row=0)
    Button(main_window, text="Print Details",command=print_hire_details,width= 10) .grid(column=4, row=0)
    Button(main_window, text="Delete Row",command=delete_row,width= 10) .grid(column=5, row=2)
    main_window.mainloop()

main_window =Tk()
main_window.configure(background="#00ff00")
customer_details = []
entry_details = []
counters = {'total_entries':0,'name_count':0}
entry_customer_name = Entry(main_window)
entry_customer_name.grid(column=1,row=0)
entry_receipt_number = Entry(main_window)
entry_receipt_number.grid(column=1,row=1)
entry_hire_item = Entry(main_window)
entry_hire_item.grid(column=1,row=2)
entry_number_hired = Entry(main_window)
entry_number_hired.grid(column=1,row=3)
delete_item = Entry(main_window)
delete_item .grid(column=4,row=2)



main()



