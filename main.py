import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

root = ttkb.Window()

customer_label = ttkb.Label(root,text='Customer name:')
customer_label.config(font=('Helvetica',18))
customer_label.grid(row=1,column=0,padx=10,pady=5)

customer_entry = ttkb.Entry(root)
customer_entry.grid(row=1,column=1,padx=10,pady=5)

root.mainloop()