
class LoginPage(tk.Frame):
    
    def __init__(self, root, commands):
        super().__init__(root)

        self.pack()
        ItemList(self).pack(side=tk.LEFT, padx=10, pady=10)
        ItemForm(self).pack(padx=10, pady=10)
        SalaryForm(self).pack(pady=10)
        self.next_button = Button(self, button_text='Next >')
        self.next_button.pack(side=tk.BOTTOM, pady=5)
        # self.item_listbox.bind_double_click(control.select_item)  
        self.item_form.bind_update(commands['login-update'])
        self.item_form.bind_delete(commands['login-delete'])
        self.item_form.bind_save(commands['login-save'])
        self.next_button.bind(commands['login-next'])

    def append_item(self, item):
        self.item_listbox.insert_item(item)

    def update_item(self, item, index):
        self.item_listbox.update_item(item, index)

    def remove_items(self):
        self.item_form.clear_entries()
        self.item_listbox.clear_items()

    def get_item_details(self):
        return self.item_form.get_item_details()

    def display_item_details(self, item):
        self.item_form.display_item_details(item)

    def get_salary(self):
        return self.salary_form.get_salary()