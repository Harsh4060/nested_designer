from tkinter import *
import pyodbc
from tkinter import ttk
from PIL import ImageTk, Image
from functools import lru_cache
import smtplib
from email.message import EmailMessage
from tkinter import messagebox
import random
import pyautogui
import datetime
import os
import time


@lru_cache(maxsize=1000)
def screenshot(invoice, name):
    #region (left_side, top_side, right_side, bottom_side)
    bill_left_side = screen_width - 713
    bill_right_side = screen_width - 661
    bill_top_side = screen_height - 625
    bill_bottom_side = screen_height - 143
    take_screenshot = pyautogui.screenshot(region=(bill_left_side, bill_top_side,
                                                   bill_right_side, bill_bottom_side))
    file = os.path.abspath('bill' + '/' + str(invoice + 1) + '_' + name + '.pdf')
    take_screenshot.save(file)
    return 1


def check_str(string):
    string_list = string.split(' ')
    capital_string_list = []
    for n in range(len(string_list)):
        if string_list[n].isalpha():
            capital_string_list.append(string_list[n].capitalize())
        else:
            pass
    if len(string_list) == len(capital_string_list):
        return capital_string_list
    else:
        return 'discontinue'


def bill_view(frame):
    global lbl_new_product_series_no, \
        lbl_new_product_list, \
        lbl_new_customer_contactno, \
        lbl_new_product_amount_summary, \
        lbl_customer_received_amount, \
        lbl_new_product_quantity_summary, \
        lbl_customer_total_amount, \
        lbl_new_customer_name, \
        lbl_customer_due_amount, \
        lbl_purchasing_date, \
        lbl_customer_invoice_tag

    contact_add_detail = ''' select contact1,contact2,address from user'''
    cursor.execute(contact_add_detail)
    contact_add_data = cursor.fetchall()

    logo_billframe = Frame(frame, bg='white')
    logo_billframe.pack(fill=BOTH, side=TOP, pady=3, padx=3)
    detail_billframe = Frame(frame, bg='black')
    detail_billframe.pack(fill=BOTH, pady=2, padx=3)

    logo_billframe.pack(fill=BOTH, side=TOP, pady=3, padx=3)
    detail_billframe.pack(fill=BOTH, pady=2, padx=3)
    upper_frame = Frame(logo_billframe, bg='white')
    upper_frame.pack(fill=BOTH)
    ganeshji_frame = Frame(upper_frame, bg='white')
    ganeshji_frame.pack(side=LEFT, fill=BOTH)
    contact_frame = Frame(upper_frame, bg='white')
    contact_frame.pack(side=RIGHT, fill=BOTH)

    shop_details = Frame(logo_billframe, bg='WHITE')
    shop_details.pack()

    lbl_contact = Label(ganeshji_frame, text='''श्री गणेशाय नमः''',
                        font=('century', 12, 'bold'),
                        fg='black',
                        bg='white', width=35, anchor=SE)
    lbl_contact.pack(fill=BOTH, ipady=10)
    lbl_contact = Label(contact_frame,
                        text='Contact - ' + str(contact_add_data[0][0]) + '\n' + '                 '
                             + str(contact_add_data[0][1]),
                        font=('century', 12, 'bold'),
                        fg='black',
                        bg='white')
    lbl_contact.pack(fill=X)

    lbl_bill_shop_slogan = Label(shop_details, image=image_buy_, bg='white')
    lbl_bill_shop_slogan.pack(side=LEFT, fill=BOTH, anchor=N)

    lbl_bill_shop_name = Label(shop_details, text='          NESTED DESIGNER',
                               font=('century', 16, 'bold'),
                               fg='black',
                               bg='white', anchor=W)
    lbl_bill_shop_name.pack(fill=BOTH)
    lbl_bill_shop_slogan = Label(shop_details, text='      You Think We Make It Possible', bg='white',
                                 fg='BLACK',
                                 font=('century', 14, 'bold'), anchor=W)
    lbl_bill_shop_slogan.pack(fill=BOTH)

    lbl_address = Label(shop_details, text=str(contact_add_data[0][2]),
                        font=('century', 10, 'bold'),
                        fg='black',
                        bg='white', justify=CENTER)
    lbl_address.pack(fill=BOTH)

    customer_details = Frame(logo_billframe, bg='WHITE')
    customer_details.pack(fill=X)
    address_frame = Frame(customer_details, bg='white')
    address_frame.pack(fill=X)
    top_frame_frame1 = Frame(customer_details, bg='white')
    top_frame_frame1.pack(fill=X)
    top_frame_frame2 = Frame(customer_details, bg='white')
    top_frame_frame2.pack(fill=X)

    lbl_customer_invoice_tag = Label(top_frame_frame1, text='Invoice no. : ' + str(invoice_number), bg='white',
                                     width=15,
                                     font=('century', 12, 'bold'), anchor=W)
    lbl_customer_invoice_tag.pack(side=LEFT)
    lbl_purchasing_date = Label(top_frame_frame1, text='Date : ' + format_date, bg='white',
                                font=('century', 12, 'bold'))
    lbl_purchasing_date.pack(side=RIGHT)

    lbl_new_customer_name = Label(top_frame_frame2, text='Customer Name : XXXXXXXX', bg='white',
                                  font=('century', 12, 'bold'))
    lbl_new_customer_name.pack(side=LEFT)
    lbl_new_customer_contactno = Label(top_frame_frame2, text='Contact no. : XXXXXXXX85', bg='white', width=20,
                                       font=('century', 12, 'bold'))
    lbl_new_customer_contactno.pack(side=RIGHT)

    lbl_series_tag = Label(detail_billframe, text='Sr No.', bg='white', width=5,
                           font=('century', 12, 'bold'))
    lbl_series_tag.grid(row=0, column=0, pady=1)
    lbl_description_tag = Label(detail_billframe, text='DESCRIPTION', bg='white', width=29,
                                font=('century', 12, 'bold'))
    lbl_description_tag.grid(row=0, column=1, pady=1, ipadx=4)
    lbl_quantity_tag = Label(detail_billframe, text='Quantity', bg='white', width=14, font=('century', 12, 'bold'))
    lbl_quantity_tag.grid(row=0, column=2, pady=1)
    lbl_amount_tag = Label(detail_billframe, text='Amount', bg='white', width=11, font=('century', 12, 'bold'))
    lbl_amount_tag.grid(row=0, column=3, pady=1)

    lbl_new_product_series_no = Label(detail_billframe, text='1.', bg='white', width=5,
                                      font=('century', 12, 'bold'), anchor='n')
    lbl_new_product_series_no.grid(row=1, column=0, pady=1)
    lbl_new_product_list = Label(detail_billframe, text='Products List', bg='white', width=29,
                                 font=('century', 12, 'bold'), anchor='n')
    lbl_new_product_list.grid(row=1, column=1, pady=1, ipadx=4)

    lbl_new_product_quantity_summary = Label(detail_billframe, text='X', bg='white', width=14,
                                             font=('century', 12, 'bold'))
    lbl_new_product_quantity_summary.grid(row=1, column=2, pady=1)

    lbl_new_product_amount_summary = Label(detail_billframe, text='Amount', bg='white', width=11,
                                           font=('century', 12, 'bold'))
    lbl_new_product_amount_summary.grid(row=1, column=3, pady=1)

    lbl_note_tag = Label(detail_billframe, text='Note :', bg='white', width=35,
                         font=('century', 12, 'bold'), height=3, anchor=NW)
    lbl_note_tag.grid(rowspan=3, columnspan=2, pady=1, ipadx=2, ipady=8, padx=1)

    lbl_customer_total_amount_tag = Label(detail_billframe, text='Total Amount :', bg='white', width=14,
                                          font=('century', 12, 'bold'), anchor=E)
    lbl_customer_total_amount_tag.grid(row=2, column=2, padx=1, pady=1)
    lbl_customer_total_amount = Label(detail_billframe, text='Rs xxxx', bg='white', width=11,
                                      font=('century', 12, 'bold'))
    lbl_customer_total_amount.grid(row=2, column=3, padx=1, pady=1)
    lbl_customer_received_amount_tag = Label(detail_billframe, text='Recieved Amount :', bg='white', width=14,
                                             font=('century', 12, 'bold'), anchor=E)
    lbl_customer_received_amount_tag.grid(row=3, column=2, padx=1, pady=1)
    lbl_customer_received_amount = Label(detail_billframe, text='Rs xxxx', bg='white', width=11,
                                         font=('century', 12, 'bold'))
    lbl_customer_received_amount.grid(row=3, column=3, padx=1, pady=1)
    lbl_customer_due_amount_tag = Label(detail_billframe, text='Due Amount :', bg='white', width=14,
                                        font=('century', 12, 'bold'), anchor=E)
    lbl_customer_due_amount_tag.grid(row=4, column=2, padx=1, pady=1)
    lbl_customer_due_amount = Label(detail_billframe, text='Rs xxxx', bg='white', width=11,
                                    font=('century', 12, 'bold'))
    lbl_customer_due_amount.grid(row=4, column=3, padx=1, pady=1)


def email():
    def send_email():
        sender_email = sender_mail.get()
        sender_email_pass = sender_password.get()
        receiver_email = receiver_mail.get()
        subject_email = subject.get()
        message = text_entry.get("1.0", END)
        check_sender_email = sender_email.split("@")
        check_receiver_email = receiver_email.split("@")

        if len(check_sender_email) == 2:
            if len(check_receiver_email) == 2:
                sender_email = sender_email
                password = sender_email_pass
                reciever_email = receiver_email

                newmessage = EmailMessage()
                newmessage['Subject'] = subject_email
                newmessage['From'] = sender_email
                newmessage['To'] = reciever_email
                newmessage.set_content(message)

                files = [os.path.abspath('bill' + '/' + str(invoice_num + 1) + '_' + customer_name.get() + '.pdf')]

                for file in files:
                    with open(file, 'rb') as f:
                        file_data = f.read()
                        file_name = f.name
                        get_name = file_name.split("\\")
                    newmessage.add_attachment(file_data, maintype='application', subtype='octet-strea',
                                              filename=get_name[-1])
                try:
                    server = smtplib.SMTP('smtp.gmail.com: 587')
                    server.starttls()
                    try:
                        server.login(sender_email, password)
                        try:
                            server.send_message(newmessage)
                            messagebox.showinfo("success", "your Email sent successfully")
                        except:
                            messagebox.showerror("error", "error to send the message")
                    except:
                        messagebox.showerror("error", "check ypu email id or password")
                except:
                    messagebox.showerror("error", "check your internet")
            else:
                messagebox.showerror("ERROR", "Receiver E-Mail id is not correct ")
        else:
            messagebox.showerror("ERROR", "Sender E-Mail id is not correct ")

    mail_window = Toplevel(root)

    sender_mail = StringVar()
    sender_password = StringVar()
    receiver_mail = StringVar()
    subject = StringVar()

    sender_mail_label = Label(mail_window, text=" Your E-Mail", font=('century', 16))
    sender_mail_label.grid(row=0, column=0, padx=10, pady=10)
    sender_mail_entry = Entry(mail_window, font=('century', 16), textvariable=sender_mail, relief="solid")
    sender_mail_entry.grid(row=0, column=1, padx=10, pady=10)
    sender_password_label = Label(mail_window, text=" Password", font=('century', 16))
    sender_password_label.grid(row=1, column=0, padx=10, pady=10)
    sender_password_entry = Entry(mail_window, font=('century', 16), show="*", textvariable=sender_password,
                                  relief="solid")
    sender_password_entry.grid(row=1, column=1, padx=10, pady=10)
    receiver_mail_label = Label(mail_window, text="Receiver E-Mail", font=('century', 16))
    receiver_mail_label.grid(row=2, column=0, padx=10, pady=10)
    # flat, groove, raised, ridge, solid, or sunken
    receiver_mail_entry = Entry(mail_window, font=('century', 16), textvariable=receiver_mail, relief="solid")
    receiver_mail_entry.grid(row=2, column=1, padx=10, pady=10)
    label_subject = Label(mail_window, text="Subject", font=('century', 16))
    label_subject.grid(row=3, column=0, padx=10, pady=10)
    subject_entry = Entry(mail_window, font=('century', 16), textvariable=subject, relief="solid")
    subject_entry.grid(row=3, column=1, padx=10, pady=10)
    text_label = Label(mail_window, font=('century', 16), text="Text")
    text_label.grid(row=4, column=0, padx=10, pady=10, sticky="N")
    text_entry = Text(mail_window, font=('century', 16), height=7, width=20, relief="solid")
    text_entry.grid(row=4, column=1, padx=10, pady=10)
    send_btn = Button(mail_window, font=('century', 12), relief="groove", bg="black", fg="white", text="SEND",
                      command=send_email)
    send_btn.grid(row=5, columnspan=2, pady=10)


def main_program():
    root.withdraw()

    def available_product():
        try:
            stock_frame.pack_forget()
            buyproduct_frame.pack_forget()
            addproduct_frame.pack_forget()
            delete_color_frame.pack_forget()
            viewdetails_frame.pack_forget()
        finally:
            stock_frame.pack(fill=BOTH)

            def check_stock():
                product_name = selected_product.get()
                if len(product_name) != 0:
                    stock = pieces[products.index(product_name)]
                    lbl_total_stock.config(text='Available Quantity ' + str(stock) + ' Pieces')
                else:
                    messagebox.showerror('ERROR', 'Select an Product')

            selected_product = StringVar()
            lbl_product_tag = Label(stock_avaibility_frame, text='Product', fg='black', bg='white', width=30,
                                    font=('century', 16, 'bold'), anchor=E)
            lbl_product_tag.grid(row=0, column=0, padx=20, pady=40)

            combobox_product_list = ttk.Combobox(stock_avaibility_frame, value=products, textvariable=selected_product,
                                                 state='readonly', width=20,
                                                 font=('century', 16, 'bold'))
            combobox_product_list.grid(row=0, column=1, padx=20, pady=40)

            btn_search = Button(stock_avaibility_frame, text='Search', fg='white', bg='black',
                                font=('century', 12, 'bold'), command=check_stock)
            btn_search.grid(row=0, column=2, pady=40)
            lbl_total_stock = Label(stock_avaibility_frame, text='', fg='black', bg='white',
                                    font=('century', 16, 'bold'), width=45, anchor=E)
            lbl_total_stock.grid(row=1, columnspan=3, pady=50, padx=50)

            white_frame = Frame(stock_frame, bg='white', height=500)
            white_frame.pack(fill=BOTH)

    def buy_products():
        try:
            stock_frame.pack_forget()
            buyproduct_frame.pack_forget()
            addproduct_frame.pack_forget()
            delete_color_frame.pack_forget()
            viewdetails_frame.pack_forget()
        finally:
            buy_scrollbar.pack(side=RIGHT, fill=Y)
            buy_canvas.pack(fill=X)
            buyproduct_frame.pack(fill=BOTH)

            def create_bill_pic(row, *args):
                ans = messagebox.askyesno('CONFIRM', 'Confirm The Bill')
                if ans:
                    # database_entry_list = [" ".join(name_join), contact_number, bill_database_list.rstrip(','),
                    #                        str(total_amount),
                    #                        str(total_received_amount), str(due_amount)]
                    re_check_invoice_no = ''' SELECT MAX(invoice_no) from customer'''
                    cursor.execute(re_check_invoice_no)
                    re_check_bill_no = cursor.fetchall()
                    re_check_invoice_num = re_check_bill_no[0][0]
                    if re_check_invoice_num is None:
                        re_check_invoice_num = 0
                    else:
                        pass
                    if int(re_check_invoice_num) != int(invoice_number):
                        time.sleep(1)

                        screenshot(invoice_num, customer_name.get())

                        insert_record = f''' insert into customer
                                             values({invoice_number},'{args[0]}','{args[1]}','{format_date}',
                                                    '{args[2]}',
                                                    '{args[3]}','{args[4]}','{args[5]}') '''
                        cursor.execute(insert_record)

                        product_seperate = args[2].split(',')
                        for j in range(len(product_seperate)):
                            product_quantity_seperate = product_seperate[j].split('-')
                            product_pieces_index_no = products.index(product_quantity_seperate[0])
                            old_quantity = pieces[product_pieces_index_no]
                            new_quantity = old_quantity - int(product_quantity_seperate[1])
                            update_quantity = f'''update stock
                                                set no_of_piece = '{new_quantity}'
                                                where model = '{product_quantity_seperate[0]}' '''
                            cursor.execute(update_quantity)
                            pieces.pop(product_pieces_index_no)
                            pieces.insert(product_pieces_index_no, new_quantity)

                            conn.commit()
                        create_email_btn = Button(buy_detail_frame, text='Share via E-mail', relief='groove',
                                                  bg='black',
                                                  fg='white',
                                                  font=('century', 11, 'bold'),
                                                  command=email)
                        create_email_btn.grid(row=row + 6, column=1, pady=15, sticky="E")
                        messagebox.showinfo('SUCCESSFULL', 'your bill generate successfully')
                    else:
                        messagebox.showerror('ERROR', 'Bill Already Exist')
                else:
                    pass

            def values():
                purchased_product = product_name[-1].get()
                if len(purchased_product) != 0:
                    product_selling_price = f"select sell_price from stock where model = '{purchased_product}'"
                    cursor.execute(product_selling_price)
                    sp_of_product = cursor.fetchall()
                    if sp_of_product[0][0] != 0:
                        selling_price[-1].set(sp_of_product[0][0])
                    else:
                        messagebox.showerror('ERROR', 'Product Price Not Be 0')

            def final_submit(series_no, row, bill_price_list, total_amount, received_amount):
                create_bill = check_condition()
                if create_bill == 'continue':
                    if received_amount.get().isnumeric():
                        contact_number = contact_no.get()
                        total_received_amount = received_amount.get()
                        due_amount = total_amount - int(total_received_amount)
                        bill_item_list = ''
                        bill_unit_list = ''
                        series_list = ''
                        prod_list = []
                        unit_list = []
                        bill_database_list = ''
                        _name_ = customer_name.get().split(' ')
                        name_join = []
                        permission_list = []
                        temprorary_peices_list = []
                        temprorary_peices_list.extend(pieces)

                        for k in range(len(product_name)):
                            prod_list.append(product_name[k].get())
                            bill_item_list = bill_item_list + product_name[i].get() + '\n'
                        for unit in range(len(total_pieces)):
                            unit_list.append(total_pieces[unit].get())
                            bill_unit_list = bill_unit_list + total_pieces[unit].get() + '\n'
                        for name in _name_:
                            name_join.append((name.capitalize()))
                        for sr_no in range(len(series_no)):
                            series_list = series_list + series_no[sr_no] + '.' + '\n'
                        for database in range(len(unit_list)):
                            product_index = products.index(prod_list[database])
                            pieces_quantity = temprorary_peices_list[product_index]
                            remain_quantity = int(pieces_quantity) - int(unit_list[database])
                            if remain_quantity >= 0:
                                temprorary_peices_list.pop(product_index)
                                temprorary_peices_list.insert(product_index, remain_quantity)
                                permission_list.append('continue')
                                bill_database_list = bill_database_list + prod_list[database] + '-' + unit_list[
                                    database] + ','
                            else:
                                messagebox.showerror('ERROR',
                                                     f"Only {pieces_quantity} Pieces "
                                                     f"of {prod_list[database]} Are Available")
                        if len(permission_list) == len(prod_list):
                            lbl_new_customer_contactno.config(text='Contact no. : ' + contact_number)
                            lbl_customer_due_amount.config(text='Rs ' + str(due_amount))
                            lbl_customer_received_amount.config(text='Rs ' + str(total_received_amount))
                            lbl_new_product_series_no.config(text=series_list.rstrip('\n'))
                            lbl_new_product_list.config(text=bill_item_list.rstrip('\n'))
                            lbl_new_product_amount_summary.config(text=bill_price_list.rstrip('\n'))
                            lbl_new_product_quantity_summary.config(text=bill_unit_list.rstrip('\n'))
                            lbl_customer_total_amount.config(text='Rs ' + str(total_amount))
                            lbl_new_customer_name.config(text='Customer Name : ' + " ".join(name_join))

                            database_entry_list = [" ".join(name_join), contact_number, bill_database_list.rstrip(','),
                                                   str(total_amount),
                                                   str(total_received_amount), str(due_amount)]
                            global create_print_btn
                            create_print_btn = Button(buy_detail_frame, text='Save Bill', relief='groove', bg='black',
                                                      fg='white',
                                                      font=('century', 11, 'bold'),
                                                      command=lambda: create_bill_pic(row, *database_entry_list))
                            create_print_btn.grid(row=row + 6, columnspan=2, pady=15)
                            global create_email_btn
                            create_email_btn = Button(buy_detail_frame, text='Share via E-mail', relief='groove',
                                                      bg='black',
                                                      fg='white',
                                                      font=('century', 11, 'bold'),
                                                      state="disable", command=email)
                            create_email_btn.grid(row=row + 6, column=1, pady=15, sticky="E")
                        else:
                            pass
                    else:
                        messagebox.showerror('ERROR', 'Enter Correct Amount Value')
                else:
                    pass

            def amount_submission(series_no, row):
                create_bill = check_condition()
                if create_bill == 'continue':
                    final_amount = StringVar()
                    received_amount = StringVar()
                    bill_total_list = ''
                    amount = []
                    total_amount = 0

                    for k in range(len(selling_price)):
                        price = int(selling_price[k].get()) * int(total_pieces[k].get())
                        amount.append(price)
                        bill_total_list = bill_total_list + str(price) + '\n'
                    for j in range(len(amount)):
                        total_amount = total_amount + amount[j]

                    final_amount.set('Rs ' + str(total_amount))
                    global lbl_disable_total_amount, entry_disable_total_amount, lbl_received_amount, \
                        entry_received_amount, create_bill_btn
                    lbl_disable_total_amount = Label(buy_detail_frame, text='Total Amount : ', width=14,
                                                     font=('century', 12, 'bold'), bg='lightskyblue3')
                    lbl_disable_total_amount.grid(row=row + 4, column=0, pady=8)
                    entry_disable_total_amount = Entry(buy_detail_frame, width=20, state='disable',
                                                       textvariable=final_amount,
                                                       font=('century', 12))
                    entry_disable_total_amount.grid(row=row + 4, column=1)
                    lbl_received_amount = Label(buy_detail_frame, text='  Received Amount : ', width=14,
                                                font=('century', 12, 'bold'), bg='lightskyblue3')
                    lbl_received_amount.grid(row=row + 5, column=0)
                    entry_received_amount = Entry(buy_detail_frame, width=20, textvariable=received_amount,
                                                  font=('century', 12))
                    entry_received_amount.grid(row=row + 5, column=1)

                    create_bill_btn = Button(buy_detail_frame, text='Create Bill', relief='groove', bg='black',
                                             fg='white',
                                             font=('century', 11, 'bold'),
                                             command=lambda: final_submit(series_no, row,
                                                                          bill_total_list,
                                                                          total_amount,
                                                                          received_amount))
                    create_bill_btn.grid(row=row + 6, column=0, pady=15)
                else:
                    pass

            def check_condition():
                if len(product_name) == 0 and len(total_pieces) == 0 and len(selling_price) == 0:
                    return 'continue'
                else:
                    convert_str = check_str(customer_name.get())
                    if type(convert_str) == list:
                        name = customer_name.get().split(' ')
                        if len(name) >= 1:
                            if contact_no.get().isnumeric() and len(contact_no.get()) == 10:
                                if len(product_name[-1].get()) != 0:
                                    if str(total_pieces[-1].get()).isnumeric():
                                        if len(selling_price[-1].get()) != 0:
                                            return 'continue'
                                        else:
                                            messagebox.showerror('ERROR', 'Price is Empty\nClick on Product Name ')
                                    else:
                                        messagebox.showerror('ERROR', 'Enter correct Number of pieces value')
                                else:
                                    messagebox.showerror('ERROR', 'Select Your Product')
                            else:
                                messagebox.showerror('ERROR', 'Enter Valid Number')
                        else:
                            messagebox.showerror('ERROR', 'Enter full name')
                    else:
                        messagebox.showerror('ERROR', 'Customer Name is required Or Enter Correct Name ')

            def add_items(row, series_no, index_value, forget_submit_btn, forget_add_items_btn):
                program_continue = check_condition()
                if program_continue == 'continue':
                    if series_no <= 14:
                        try:
                            if row == 2:
                                pass
                            else:
                                forget_submit_btn.grid_forget()
                                forget_add_items_btn.grid_forget()
                                lbl_disable_total_amount.grid_forget()
                                entry_disable_total_amount.grid_forget()
                                lbl_received_amount.grid_forget()
                                entry_received_amount.grid_forget()
                                create_print_btn.grid_forget()
                                create_email_btn.grid_forget()
                                create_bill_btn.grid_forget()
                        finally:
                            product_var = chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + chr(
                                random.randint(65, 90))
                            piece_var = chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + chr(
                                random.randint(65, 90))
                            sp_var = chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + chr(
                                random.randint(65, 90))
                            if index_value != 0:
                                prod_position = prod_help.index(product_name[index_value - 1].get().lower())
                                total_prod_piece = piece_update[prod_position]
                                updated_pieces = total_prod_piece - int(total_pieces[index_value - 1].get())
                                piece_update.pop(prod_position)
                                piece_update.insert(prod_position, updated_pieces)
                                if updated_pieces > 0:
                                    product_name.append(product_var)
                                    total_pieces.append(piece_var)
                                    selling_price.append(sp_var)

                                    product_name[index_value] = StringVar()
                                    total_pieces[index_value] = StringVar()
                                    selling_price[index_value] = StringVar()

                                    product_lbl = Label(buy_detail_frame, text='Product ' + str(series_no) + ' : ',
                                                        width=14, bg='lightskyblue3',
                                                        font=('century', 12, 'bold'))
                                    product_lbl.grid(row=row, column=0, pady=20)

                                    product_selection = ttk.Combobox(buy_detail_frame, value=products,
                                                                     textvariable=product_name[index_value],
                                                                     state='readonly',
                                                                     height=5,
                                                                     width=20,
                                                                     font=('century', 12), postcommand=values)
                                    product_selection.grid(row=row, column=1)
                                    no_of_pieces_lbl = Label(buy_detail_frame, text='No. Of  Pieces : ', width=14,
                                                             font=('century', 12, 'bold'), bg='lightskyblue3')
                                    no_of_pieces_lbl.grid(row=row + 1, column=0)
                                    no_of_pieces_entry = Entry(buy_detail_frame, width=20,
                                                               textvariable=total_pieces[index_value],
                                                               font=('century', 12, 'bold'))
                                    no_of_pieces_entry.grid(row=row + 1, column=1, pady=20)
                                    no_of_pieces_lbl = Label(buy_detail_frame, text='Product Price : ', width=14,
                                                             font=('century', 12, 'bold'), bg='lightskyblue3')
                                    no_of_pieces_lbl.grid(row=row + 2, column=0)
                                    no_of_pieces_entry = Entry(buy_detail_frame, width=20,
                                                               textvariable=selling_price[index_value],
                                                               state='disable',
                                                               font=('century', 12, 'bold'))
                                    no_of_pieces_entry.grid(row=row + 2, column=1, pady=20)

                                    updated_row = row + 3
                                    series_num = series_no + 1
                                    updated_index = index_value + 1
                                    lbl_series_no.append(str(series_no))

                                    add_items_btn = Button(buy_detail_frame, text='Add Item', relief='groove',
                                                           bg='black',
                                                           fg='white',
                                                           font=('century', 11, 'bold'),
                                                           command=lambda: add_items(updated_row, series_num,
                                                                                     updated_index,
                                                                                     submit_btn,
                                                                                     add_items_btn))
                                    add_items_btn.grid(row=row + 3, column=1, sticky=E)
                                else:
                                    if updated_pieces <= 0:
                                        updated_pieces = total_prod_piece
                                    messagebox.showerror('ERROR',
                                                         f"Only {updated_pieces} Pieces "
                                                         f"of {prod_help[prod_position]} Are Available")
                            else:

                                product_name.append(product_var)
                                total_pieces.append(piece_var)
                                selling_price.append(sp_var)

                                product_name[index_value] = StringVar()
                                total_pieces[index_value] = StringVar()
                                selling_price[index_value] = StringVar()

                                product_lbl = Label(buy_detail_frame, text='Product ' + str(series_no) + ' : ',
                                                    width=14, bg='lightskyblue3',
                                                    font=('century', 12, 'bold'))
                                product_lbl.grid(row=row, column=0, pady=20)

                                product_selection = ttk.Combobox(buy_detail_frame, value=products,
                                                                 textvariable=product_name[index_value],
                                                                 state='readonly',
                                                                 height=5,
                                                                 width=20,
                                                                 font=('century', 12), postcommand=values)
                                product_selection.grid(row=row, column=1)
                                no_of_pieces_lbl = Label(buy_detail_frame, text='No. Of  Pieces : ', width=14,
                                                         font=('century', 12, 'bold'), bg='lightskyblue3')
                                no_of_pieces_lbl.grid(row=row + 1, column=0)
                                no_of_pieces_entry = Entry(buy_detail_frame, width=20,
                                                           textvariable=total_pieces[index_value],
                                                           font=('century', 12, 'bold'))
                                no_of_pieces_entry.grid(row=row + 1, column=1, pady=20)
                                no_of_pieces_lbl = Label(buy_detail_frame, text='Product Price : ', width=14,
                                                         font=('century', 12, 'bold'), bg='lightskyblue3')
                                no_of_pieces_lbl.grid(row=row + 2, column=0)
                                no_of_pieces_entry = Entry(buy_detail_frame, width=20,
                                                           textvariable=selling_price[index_value],
                                                           state='disable',
                                                           font=('century', 12, 'bold'))
                                no_of_pieces_entry.grid(row=row + 2, column=1, pady=20)

                                updated_row = row + 3
                                series_num = series_no + 1
                                updated_index = index_value + 1
                                lbl_series_no.append(str(series_no))
                                add_items_btn = Button(buy_detail_frame, text='Add Item', relief='groove', bg='black',
                                                       fg='white',
                                                       font=('century', 11, 'bold'),
                                                       command=lambda: add_items(updated_row, series_num, updated_index,
                                                                                 submit_btn,
                                                                                 add_items_btn))
                                add_items_btn.grid(row=row + 3, column=1, sticky=E)

                            submit_btn = Button(buy_detail_frame, text='Submit', relief='groove', bg='black',
                                                fg='white',
                                                font=('century', 11, 'bold'),
                                                command=lambda: amount_submission(lbl_series_no, row))
                            submit_btn.grid(row=row + 3, column=0)

                    else:
                        messagebox.showwarning('WARNING', 'BIlL Contain only upto 14 product')
                else:
                    pass

            product_name = []
            total_pieces = []
            selling_price = []
            lbl_series_no = []

            product_series_no = 1
            row_value = 2
            var_index = 0
            submit_button = None
            add_items_button = None

            global customer_name
            customer_name = StringVar()
            contact_no = StringVar()

            global custumer_billframe
            custumer_billframe = Frame(buyproduct_frame, bg='black')
            custumer_billframe.pack(fill=X, side=RIGHT, padx=20)

            customer_name_lbl = Label(buy_detail_frame, text='Customer Name : ', bg='lightskyblue3', width=14,
                                      font=('century', 12, 'bold'))
            customer_name_lbl.grid(row=0, column=0, pady=20)
            customer_name_entry = Entry(buy_detail_frame, width=30, textvariable=customer_name,
                                        font=('century', 12))
            customer_name_entry.grid(row=0, column=1)
            customer_name_lbl = Label(buy_detail_frame, text='Contact no. : ', bg='lightskyblue3', width=14,
                                      font=('century', 12, 'bold'))
            customer_name_lbl.grid(row=1, column=0, pady=20)
            customer_name_entry = Entry(buy_detail_frame, width=30, textvariable=contact_no,
                                        font=('century', 12))
            customer_name_entry.grid(row=1, column=1)
            add_items(row_value, product_series_no, var_index, submit_button, add_items_button)
            bill_view(custumer_billframe)

    def adding_product():
        try:
            stock_frame.pack_forget()
            buyproduct_frame.pack_forget()
            addproduct_frame.pack_forget()
            delete_color_frame.pack_forget()
            viewdetails_frame.pack_forget()
        finally:
            addproduct_frame.pack(fill=BOTH, ipady=700)
            addproduct_frame.config(bg='white')

            def add_product_in_database():
                new_product_name = product_name.get()
                product_quantity = quantity.get()
                if str(product_quantity).isnumeric():
                    if len(new_product_name) != 0:
                        continue_program = check_str(new_product_name)
                        if continue_program != 'discontinue':
                            if len(products) == 0:
                                products.append(0)
                            for o in range(len(products)):
                                if products[o] != " ".join(continue_program):
                                    insert_product = f'''insert into stock(model,no_of_piece)
                                                         values('{' '.join(continue_program)}',
                                                         '{int(product_quantity)}')'''
                                    cursor.execute(insert_product)
                                    conn.commit()
                                    messagebox.showinfo('Successfully', 'Your New Product Added Successfully')
                                    break
                                else:
                                    product_index = products.index(new_product_name)
                                    old_quantity = pieces[product_index]
                                    update_quantity = f'''update stock
                                                          set no_of_piece='{int(old_quantity) + int(product_quantity)}' 
                                                          where model='{' '.join(continue_program)}' '''
                                    cursor.execute(update_quantity)
                                    messagebox.showinfo('Successfully', 'Your Existed Product Updated Successfully')
                                    conn.commit()
                                    break
                        else:
                            messagebox.showerror('ERROR', 'Enter Correct Product Name')
                    else:
                        messagebox.showerror('ERROR', 'All Column Are Required')
                else:
                    messagebox.showerror('ERROR', 'Quantity Must be Integer')

            frame_add_product = Frame(addproduct_frame, bg='lightskyblue3')
            frame_add_product.grid(padx=320, pady=80, row=0, column=0, ipadx=10)

            product_name = StringVar()
            quantity = StringVar()

            existing_product_lbl = Label(frame_add_product, text='Product Name', bg='white',
                                         font=('century', 14, 'bold'),
                                         width=15)
            existing_product_lbl.grid(row=0, column=0, padx=30, pady=20)
            combobox_existing_product = ttk.Combobox(frame_add_product, value=products, textvariable=product_name,
                                                     font=('century', 14, 'bold'), width=19)
            combobox_existing_product.grid(row=0, column=1)

            item_name_lbl = Label(frame_add_product, text='Quantity', bg='white', font=('century', 14, 'bold'),
                                  width=15)
            item_name_lbl.grid(row=1, column=0, padx=30, pady=40)
            spinbox_quantiy = ttk.Spinbox(frame_add_product, from_=0, to=100, font=('century', 14, 'bold'),
                                          textvariable=quantity, width=20)
            spinbox_quantiy.grid(row=1, column=1)

            add_items_button = Button(frame_add_product, text='ADD ITEM', bg='black', fg='white',
                                      font=('century', 12, 'bold'), command=add_product_in_database)
            add_items_button.grid(row=2, columnspan=2)

    def del_product():
        try:
            stock_frame.pack_forget()
            buyproduct_frame.pack_forget()
            addproduct_frame.pack_forget()
            delete_color_frame.pack_forget()
            viewdetails_frame.pack_forget()
        finally:
            delete_color_frame.pack(fill=BOTH)

            def remove_product():
                delete_item = del_item.get()
                if len(delete_item) != 0:
                    product_index = products.index(delete_item)
                    product_peices = pieces[product_index]
                    delete_product_from_database = f'''delete from stock
                                                       where model='{delete_item}' '''
                    cursor.execute(delete_product_from_database)
                    conn.commit()
                    products.remove(delete_item)
                    pieces.remove(product_peices)
                    del_item.set('')
                    messagebox.showinfo('SUCCESSFULL', 'Your Product Has Been Deleted Successfully')
                else:
                    messagebox.showerror('ERROR', 'Select a product')

            del_item = StringVar()
            item_name_lbl = Label(deleteproduct_frame, text='Item Name', font=('century', 14, 'bold'))
            item_name_lbl.grid(row=0, column=0, padx=30, pady=40)

            del_item_combobox = ttk.Combobox(deleteproduct_frame, values=products, textvariable=del_item, height=5,
                                             state='readonly',
                                             font=('century', 16, 'bold'))
            del_item_combobox.grid(row=0, column=1)

            del_button = Button(deleteproduct_frame, relief='groove', text='Remove Product', bg='black', fg='white',
                                font=('century', 12, 'bold'),
                                comman=remove_product)
            del_button.grid(row=0, column=2, padx=30)
            delete_white_frame = Frame(delete_color_frame, bg='white')
            delete_white_frame.pack(fill=BOTH, ipady=500)

    def view_customer_details():
        take_costumer_detailed_frame = Frame(viewdetails_frame, bg='white', width=20)
        take_costumer_detailed_frame.grid(row=0, column=0, sticky="N")
        detail_frame = chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + chr(random.randint(65, 90))
        if len(frames) == 0:
            frames.append('abc')
        if frames[0] == 'abc':
            frames.pop(0)
        else:
            frames.pop(0)
        frames.append(detail_frame)
        frames[0] = Frame(viewdetails_frame, bg='black')
        frames[0].grid(row=0, column=1, sticky="N")
        try:
            stock_frame.pack_forget()
            buyproduct_frame.pack_forget()
            addproduct_frame.pack_forget()
            delete_color_frame.pack_forget()
            take_costumer_detailed_frame.grid_forget()
            viewdetails_frame.pack_forget()
            frames[0].grid_forget()
        finally:
            viewdetails_frame.pack(fill=BOTH)
            take_costumer_detailed_frame.grid(row=0, column=0, sticky="N")
            frames[0].grid(row=0, column=1)

            def get_details():
                get_invoice_number = find_invoice_num.get()
                details = f''' select * from customer
                                      where invoice_no = {get_invoice_number} '''
                cursor.execute(details)
                customer_details = cursor.fetchall()
                if customer_details:

                    bill_amount_list = ''
                    bill_series_list = ''
                    bill_product_list = ''
                    bill_quantity_list = ''
                    bill_split_product_list = customer_details[0][4].split(',')

                    for m in range(len(bill_split_product_list)):
                        bill_series_list = bill_series_list + str(m + 1) + '.' + '\n'
                        split_product_unit = bill_split_product_list[m].split('-')
                        bill_product_list = bill_product_list + split_product_unit[0] + '\n'
                        bill_product_selling_price = f'''select sell_price from stock
                                                             where model = '{split_product_unit[0]}' '''
                        cursor.execute(bill_product_selling_price)
                        sp_of_product = cursor.fetchall()
                        bill_quantity_list = bill_quantity_list + split_product_unit[1] + '\n'
                        bill_amount_list = bill_amount_list + str(
                            int(sp_of_product[0][0]) * int(split_product_unit[1])) + '\n'
                    try:
                        frames[0].grid_forget()
                        take_costumer_detailed_frame.grid_forget()
                        viewdetails_frame.pack_forget()
                    finally:
                        frames[0].grid(row=0, column=1)
                        take_costumer_detailed_frame.grid(row=0, column=0, sticky="N")
                        viewdetails_frame.pack(fill=BOTH)

                        lbl_new_product_series_no.config(text=bill_series_list.rstrip('\n'))
                        lbl_new_product_list.config(text=bill_product_list.rstrip('\n'))
                        lbl_new_customer_contactno.config(text='Contact no. : ' + str(customer_details[0][2]))
                        lbl_purchasing_date.config(text='Date : ' + customer_details[0][3])
                        lbl_customer_invoice_tag.config(text='Invoice no. : ' + str(customer_details[0][0]))
                        lbl_new_product_amount_summary.config(text=bill_amount_list.rstrip('\n'))
                        lbl_customer_received_amount.config(text=customer_details[0][6])
                        lbl_new_product_quantity_summary.config(text=bill_quantity_list.rstrip('\n'))
                        lbl_customer_total_amount.config(text=customer_details[0][5])
                        lbl_new_customer_name.config(text='Customer Name : ' + customer_details[0][1])
                        lbl_customer_due_amount.config(text=customer_details[0][7])

                        def on_email_button():
                            ab = screenshot(int(customer_details[0][0]) - 1, customer_details[0][1])
                            save_btn = Button(take_costumer_detailed_frame, text='SAVE', font=('century', 12),
                                              state="disable")
                            save_btn.grid(row=1, columnspan=2)
                            emaill = Button(take_costumer_detailed_frame, text='Share via Email', font=('century', 12),
                                            command=email)
                            emaill.grid(row=1, column=1)

                        save_btn = Button(take_costumer_detailed_frame, text='SAVE', font=('century', 12),
                                          command=on_email_button)
                        save_btn.grid(row=1, columnspan=2)
                else:
                    messagebox.showerror('ERROR', 'Record Not Exist')

            find_invoice_num = StringVar()
            lbl_invoice_tag = Label(take_costumer_detailed_frame, text='Enter Invoice no.', width=20,
                                    font=('century', 12, 'bold'))
            lbl_invoice_tag.grid(row=0, column=0, pady=20)
            entry_invoice_no = Entry(take_costumer_detailed_frame, font=('century', 12), textvariable=find_invoice_num,
                                     width=23)
            entry_invoice_no.grid(row=0, column=1, padx=12)

            sub_btn = Button(take_costumer_detailed_frame, text='Submit', font=('century', 12),
                             command=get_details)
            sub_btn.grid(row=1, column=0)
            save_btn = Button(take_costumer_detailed_frame, text='SAVE', font=('century', 12), state="disable")
            save_btn.grid(row=1, columnspan=2)
            emaill = Button(take_costumer_detailed_frame, text='Share via Email', font=('century', 12), state="disable",
                            command=get_details)
            emaill.grid(row=1, column=1)

            bill_view(frames[0])

            lbl_customer_invoice_tag.config(text='Invoice no. : XX')

    if security_check == 1:
        main_toplevel.withdraw()
    root.deiconify()
    button_frame = Frame(root, bg='lightskyblue3', width=20)
    button_frame.pack(fill=BOTH, side=LEFT)
    logo_frame = Frame(root, bg='white')
    logo_frame.pack(fill=BOTH)

    top_logo_slogan_frame(logo_frame)
    info_frame = Frame(button_frame, bg='lightskyblue3', height=120)
    info_frame.pack(fill=BOTH)
    contain_frame = Frame(root, bg='white', height=20)
    contain_frame.pack(fill=BOTH)

    btn2frame = Frame(button_frame, bg='lightskyblue3')
    btn2frame.pack(fill=BOTH, pady=10)

    #                       #######     MENU  FRAME     ##########

    #                       #######     STOCK AVAIBILITY FRAME     ##########
    stock_frame = Frame(contain_frame, bg='white')
    stock_frame.pack(fill=BOTH)
    stock_avaibility_frame = Frame(stock_frame, bg='white')
    stock_avaibility_frame.pack(fill=BOTH)
    #                       #######     BUY PRODUCT FRAME     ##########
    buyproduct_frame = Frame(contain_frame, bg='white')
    buyproduct_frame.pack(fill=BOTH)

    buyproduct_detailed_frame = Frame(buyproduct_frame, bg='white')
    buyproduct_detailed_frame.pack(fill=BOTH, side=LEFT)

    def myfunction(event):
        buy_canvas.configure(scrollregion=buy_canvas.bbox("all"), height=615, width=440)

    buy_canvas = Canvas(buyproduct_detailed_frame, bg='lightskyblue3')
    buy_detail_frame = Frame(buy_canvas, bg='lightskyblue3')
    buy_scrollbar = Scrollbar(buyproduct_detailed_frame, orient="vertical", command=buy_canvas.yview)
    buy_canvas.configure(yscrollcommand=buy_scrollbar.set)

    buy_scrollbar.pack(side=RIGHT, fill=Y)
    buy_canvas.pack(fill=X)
    buy_canvas.create_window((0, 0), window=buy_detail_frame)
    buy_detail_frame.bind("<Configure>", myfunction)

    buy_scrollbar.pack_forget()
    buy_canvas.pack_forget()

    #                       #######     ADD PRODUCT FRAME     ##########
    addproduct_frame = Frame(contain_frame)
    addproduct_frame.pack(fill=BOTH)
    #                       #######     DELETE PRODUCT FRAME     ##########

    delete_color_frame = Frame(contain_frame, bg='lightskyblue3')
    delete_color_frame.pack(fill=BOTH)
    deleteproduct_frame = Frame(delete_color_frame, bg='lightskyblue3', width=50)
    deleteproduct_frame.pack(fill=BOTH, padx=265, ipadx=50)

    #                       #######     VIEW DETAILS FRAME     ##########
    viewdetails_frame = Frame(contain_frame, bg='white')
    viewdetails_frame.pack(fill=BOTH)

    available_stock_image_location = os.path.abspath('images/available_stock.png')
    available_stock_opened_image = Image.open(available_stock_image_location)
    esize_image = available_stock_opened_image.resize((30, 30))
    global available_stock
    available_stock = ImageTk.PhotoImage(esize_image)
    btn = Button(btn2frame, image=available_stock, text='  AVAILABLE STOCK', compound=LEFT, relief='raised',
                 font=('century', 10), width=165, command=available_product)
    btn.grid(row=0, column=0, padx=10, pady=20)

    buy_product_image_location = os.path.abspath('images/buy_product.jpg')
    buy_product_opened_image = Image.open(buy_product_image_location)
    esize_image = buy_product_opened_image.resize((30, 30))
    global buy_product
    buy_product = ImageTk.PhotoImage(esize_image)
    btn = Button(btn2frame, image=buy_product, text='     BUY PRODUCT     ', compound=LEFT, relief='raised',
                 font=('century', 10), width=165, command=buy_products)
    btn.grid(row=1, column=0, padx=10, pady=20)

    add_product_image_location = os.path.abspath('images/add_product.jpg')
    add_product_opened_image = Image.open(add_product_image_location)
    esize_image = add_product_opened_image.resize((30, 30))
    global add_product
    add_product = ImageTk.PhotoImage(esize_image)
    btn = Button(btn2frame, image=add_product, text='     ADD PRODUCT     ', compound=LEFT, relief='raised',
                 font=('century', 10), width=165, command=adding_product)
    btn.grid(row=2, column=0, padx=10, pady=20)

    delete_image_location = os.path.abspath('images/delete.png')
    delete_opened_image = Image.open(delete_image_location)
    esize_image = delete_opened_image.resize((25, 30))
    global delete_product_image
    delete_product_image = ImageTk.PhotoImage(esize_image)
    # flat, groove, raised, ridge, solid, or sunken
    btn = Button(btn2frame, image=delete_product_image, text='  DELETE PRODUCT', compound=LEFT, relief='raised',
                 font=('century', 10), width=165, command=del_product)
    btn.grid(row=3, column=0, padx=10, pady=20)

    view_details_image_location = os.path.abspath('images/view_details.jpg')
    view_details_opened_image = Image.open(view_details_image_location)
    esize_image = view_details_opened_image.resize((30, 30))
    global view_details
    view_details = ImageTk.PhotoImage(esize_image)
    btn = Button(btn2frame, image=view_details, text='     VIEW DETAILS     ', compound=LEFT, relief='raised',
                 font=('century', 10), width=165, command=view_customer_details)
    btn.grid(row=4, column=0, padx=10, pady=20)

    refresh_button_image_location = os.path.abspath('images/refresh_button.jpg')
    refresh_button_opened_image = Image.open(refresh_button_image_location)
    esize_image = refresh_button_opened_image.resize((30, 30))
    global refresh_image
    refresh_image = ImageTk.PhotoImage(esize_image)
    refreshtbtn = Button(btn2frame, image=refresh_image, text='       REFRESH          ', compound=LEFT,
                         relief='raised',
                         font=('century', 10), width=165, command=lambda: exit_program(1))
    refreshtbtn.grid(row=5, column=0, padx=10, pady=20)

    exit_button_image_location = os.path.abspath('images/exit_button.jpg')
    exit_button_opened_image = Image.open(exit_button_image_location)
    esize_image = exit_button_opened_image.resize((30, 30))
    global exit_image
    exit_image = ImageTk.PhotoImage(esize_image)
    exitbtn = Button(btn2frame, image=exit_image, text='          EXIT               ', compound=LEFT, relief='raised',
                     font=('century', 10), width=165, command=lambda: exit_program(0))
    exitbtn.grid(row=6, column=0, padx=10, pady=20)


def security_system():
    def login():
        username_and_password = '''select username,password from user'''
        cursor.execute(username_and_password)
        user_login = cursor.fetchall()
        print(user_login)
        if user_login:
            if user_login[0][0] is not None:
                if user_login[0][0] == username.get() and user_login[0][1] == password.get():
                    main_program()
                else:
                    messagebox.showerror('ERROR', 'Your username or password is wrong')
            else:
                messagebox.showerror('ERROR', 'Register Username And Password')
        else:
            messagebox.showerror('ERROR', 'Register Username And Password')

    def sign_up():
        check_user = ''' select username from user '''
        cursor.execute(check_user)
        if not cursor.fetchall():

            def approve():
                username_get = username_input.get()
                contact1_get = contact1_input.get()
                contact2_get = contact2_input.get()
                address_get = address_input.get()
                password_get = password_input.get()
                re_password_get = re_password_input.get()

                if password_get.isalnum():
                    if contact1_get.isnumeric() and len(contact1_get) == 10:
                        if contact2_get.isnumeric() and len(contact2_get) == 10:
                            if password_get == re_password_get:
                                print(username_get, password_get,contact1_get,contact2_get, address_get)
                                insert_user_data = f''' insert into user 
                                                       values('{username_get}','{password_get}','{contact1_get}',
                                                               '{contact2_get}', '{address_get}' ) '''
                                cursor.execute(insert_user_data)
                                conn.commit()
                                messagebox.showinfo('SUCCESS', 'Your Sign Up Is Successfull')
                                sign_up_frame.place_forget()
                                security_frame.place(x=500, y=350)
                            else:
                                messagebox.showerror('error', 'password not same')
                        else:
                            messagebox.showerror('error', 'contact 2')
                    else:
                        messagebox.showerror('error', 'contact 1')
                else:
                    messagebox.showerror('error', 'password')

            username_input = StringVar()
            contact1_input = StringVar()
            contact2_input = StringVar()
            address_input = StringVar()
            password_input = StringVar()
            re_password_input = StringVar()

            security_frame.place_forget()

            sign_up_frame = Frame(security_requirement, bg='white', padx=20, pady=20)
            sign_up_frame.place(x=450, y=150)

            username_tag = Label(sign_up_frame, text='Username', bg='white', font=('century', 12))
            username_tag.grid(row=0, column=0, padx=30, pady=5)
            username_entry = Entry(sign_up_frame, font=('century', 12), textvariable=username_input)
            username_entry.grid(row=0, column=1, padx=30, pady=5)

            contact1_tag = Label(sign_up_frame, text='Contact no. 1 ', bg='white', font=('century', 12))
            contact1_tag.grid(row=1, column=0, padx=30, pady=5)
            contact1_entry = Entry(sign_up_frame, font=('century', 12), textvariable=contact1_input)
            contact1_entry.grid(row=1, column=1, padx=30, pady=5)

            contact2_tag = Label(sign_up_frame, text='Contact no. 2 ', bg='white', font=('century', 12))
            contact2_tag.grid(row=2, column=0, padx=30, pady=5)
            contact2_entry = Entry(sign_up_frame, font=('century', 12), textvariable=contact2_input)
            contact2_entry.grid(row=2, column=1, padx=30, pady=5)

            address_tag = Label(sign_up_frame, text='Address', bg='white', font=('century', 12))
            address_tag.grid(row=3, column=0, padx=30, pady=5)
            address_entry = Entry(sign_up_frame, font=('century', 12), textvariable=address_input)
            address_entry.grid(row=3, column=1, padx=30, pady=5)

            password_tag = Label(sign_up_frame, text='Password', bg='white', font=('century', 12))
            password_tag.grid(row=4, column=0, padx=30, pady=5)
            password_entry = Entry(sign_up_frame, show='*', font=('century', 12), textvariable=password_input)
            password_entry.grid(row=4, column=1, padx=30, pady=5)

            repassword_tag = Label(sign_up_frame, text='Re-enter password', bg='white', font=('century', 12))
            repassword_tag.grid(row=5, column=0, padx=30, pady=5)
            repassword_entry = Entry(sign_up_frame, show='*', font=('century', 12), textvariable=re_password_input)
            repassword_entry.grid(row=5, column=1, padx=30, pady=5)

            sign_up_image_location = os.path.abspath('images/sign up.png')
            sign_up_opened_image = Image.open(sign_up_image_location)
            resize_image = sign_up_opened_image.resize((110, 35))
            global sign_up_image
            sign_up_image = ImageTk.PhotoImage(resize_image)
            sign_up_btn = Button(sign_up_frame, image=sign_up_image, bg='white', relief='flat', command=approve)
            sign_up_btn.grid(row=6, column=1, padx=30)
        else:
            messagebox.showerror('ERROR', 'User Already Exist  ')

    top_logo_slogan_frame(shop_lbl_main_frame)

    username = StringVar()
    password = StringVar()

    security_requirement = Frame(main_toplevel, bg='white', width=60, height=620)
    security_requirement.pack(fill=BOTH)
    security_frame = Frame(main_toplevel, bg='white', padx=20)
    security_frame.place(x=500, y=350)

    top_logo_image_location = os.path.abspath('images/web-1012467_1920.jpg')
    top_logo_opened_image = Image.open(top_logo_image_location)
    esize_image = top_logo_opened_image.resize((1360, 750))
    global bg_image
    bg_image = ImageTk.PhotoImage(esize_image)
    Label(security_requirement, image=bg_image).place(x=-4, y=0, relwidth=1, relheight=1)

    username_image_location = os.path.abspath('images/username.png')
    username_opened_image = Image.open(username_image_location)
    resize_image = username_opened_image.resize((20, 20))
    global userame_image
    userame_image = ImageTk.PhotoImage(resize_image)
    lbl_username_tag = Label(security_frame, image=userame_image, text='   Username', compound=LEFT, bg='white'
                             , font=('century', 12))
    lbl_username_tag.grid(row=0, column=0, padx=5, pady=10)
    entry_username_tag = Entry(security_frame, textvariable=username, font=('century', 12), relief='groove')
    entry_username_tag.grid(row=0, column=1)

    password_protection_image_location = os.path.abspath('images/password protection.png')
    password_protection_opened_image = Image.open(password_protection_image_location)
    resize_image = password_protection_opened_image.resize((20, 20))
    global password_image
    password_image = ImageTk.PhotoImage(resize_image)
    lbl_password_tag = Label(security_frame, image=password_image, text='   Password ', compound=LEFT, bg='white',
                             font=('century', 12))
    lbl_password_tag.grid(row=1, column=0, padx=5, pady=5)
    entry_password_tag = Entry(security_frame, show='*', textvariable=password, font=('century', 12),
                               relief='groove')
    entry_password_tag.grid(row=1, column=1)

    register_btn_image_location = os.path.abspath('images/register_btn.jpg')
    register_btn_opened_image = Image.open(register_btn_image_location)
    esize_image = register_btn_opened_image.resize((125, 35))
    global sign_up_image
    sign_up_image = ImageTk.PhotoImage(esize_image)
    sign_up_button = Button(security_frame, bg='white', image=sign_up_image, relief='flat',
                            command=sign_up)
    sign_up_button.grid(row=2, column=0, pady=10)

    login_btn_image_location = os.path.abspath('images/login_Btn.jpg')
    login_btn_opened_image = Image.open(login_btn_image_location)
    esize_image = login_btn_opened_image.resize((120, 35))
    global login_image
    login_image = ImageTk.PhotoImage(esize_image)
    log_in_button = Button(security_frame, bg='white', image=login_image, relief='flat', command=login)
    log_in_button.grid(row=2, column=1, pady=10, padx=5)


def top_logo_slogan_frame(frame):
    shop_lbl_frame = Frame(frame)
    shop_lbl_frame.pack(fill=X, padx=5, pady=5)

    image_shop_name = Frame(shop_lbl_frame)
    image_shop_name.pack(fill=BOTH)
    shop_slogan = Frame(shop_lbl_frame)
    shop_slogan.pack(fill=BOTH)

    top_logo_image_location = os.path.abspath('images/nested_designer_logo.jpg')
    top_logo_opened_image = Image.open(top_logo_image_location)
    esize_image = top_logo_opened_image.resize((70, 70))
    global shop_logo
    shop_logo = ImageTk.PhotoImage(esize_image)
    lbl_shop_name = Label(image_shop_name, image=shop_logo, text='  NESTED DESIGNER', compound=LEFT,
                          font=('century', 28, 'bold'),
                          fg='black',
                          bg='white')
    lbl_shop_name.pack(fill=X)
    lbl_shop_name = Label(shop_slogan, text='                 You Think We Make It Possible',
                          font=('century', 18, 'bold'), fg='black',
                          bg='white')
    lbl_shop_name.pack(fill=X, side='bottom')


def exit_program(permission):
    global permit
    root.destroy()
    if permission == 1:
        permit = 'yes'
    else:
        permit = '0'


if __name__ == '__main__':
    security_check = 1
    permit = 'yes'
    while permit == 'yes':
        db_file_location = os.path.abspath("nestedd_designer.accdb")
        try:
            conn = pyodbc.connect(
                r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s' % (db_file_location,))
            cursor = conn.cursor()

            root = Tk()
            root.config(bg="white")
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            root.geometry(f'{screen_width}x{screen_height}')
            root.title('Nested Designer')
            root.iconbitmap(os.path.abspath('images/nested_designer_icon.ico'))

            #       #########################          RETRIEVE DATA FROM DATABASE         ######################

            products = []
            pieces = []
            frames = ['abc']
            piece_update = []
            prod_help = []

            product = ''' select model from stock '''
            cursor.execute(product)
            product_list = cursor.fetchall()
            peice = ''' select no_of_piece from stock '''
            cursor.execute(peice)
            no_of_pieces = cursor.fetchall()
            invoice_no = ''' SELECT MAX(invoice_no) from customer'''
            cursor.execute(invoice_no)
            bill_no = cursor.fetchall()
            if bill_no[0][0] is None:
                invoice_num = 0
            else:
                invoice_num = bill_no[0][0]
            if len(str(invoice_num)) == 1 and int(invoice_num) <= 8:
                invoice_number = '0' + str(invoice_num + 1)
            else:
                invoice_number = str(invoice_num + 1)
            for prods in product_list:
                for prod in prods:
                    products.append(prod)
            for peics in no_of_pieces:
                for peic in peics:
                    pieces.append(peic)
            for i in range(len(products)):
                prod_help.append(products[i].lower())
                piece_update.append(pieces[i])

            date = datetime.datetime.now()
            format_date = f"{date: %d/%b/%y, %a}"

            office_detail = ''' select * from user'''
            cursor.execute(office_detail)
            shop_data = cursor.fetchall()

            #                       #######     ROOT FRAME     ##########
            if security_check == 1:
                root.withdraw()
                main_toplevel = Toplevel()
                main_toplevel.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
                main_toplevel.title('Nested Designer')
                main_toplevel.iconbitmap(os.path.abspath('images/nested_designer_icon.ico'))

                #                       #######     SHOP LOGO AND SLOGAN FRAME    ##########
                shop_lbl_main_frame = Frame(main_toplevel, bg='black')
                shop_lbl_main_frame.pack(fill=X)
                #                       #######     SECURITY FRAME     ##########

                security_system()
            else:
                main_program()

            image_location = os.path.abspath('images/nested_designer_logo.jpg')
            opened_image = Image.open(image_location)
            logo_resize_image = opened_image.resize((60, 60))
            image_buy_ = ImageTk.PhotoImage(logo_resize_image)

            # ################## GLOBAL DECLARE ################
            custumer_billframe = Frame(root, bg='black')
            create_print_btn = Button(root, text='Print', relief='groove', bg='black',
                                      fg='white',
                                      font=('century', 11, 'bold'))
            lbl_disable_total_amount = Label(root, text='Total Amount : ', width=14,
                                             font=('century', 12, 'bold'))
            entry_disable_total_amount = Entry(root, width=20, state='disable',
                                               font=('century', 12))
            lbl_received_amount = Label(root, text='Received Amount : ', width=14,
                                        font=('century', 12, 'bold'))
            entry_received_amount = Entry(root, width=20,
                                          font=('century', 12))
            create_bill_btn = Button(root, text='Create Bill', relief='groove', bg='black',
                                     fg='white',
                                     font=('century', 11, 'bold'))
            root.mainloop()

            security_check += 1
        except:
            messagebox.showerror("ERROR", "unable to connect with database")
            permit = "no"
