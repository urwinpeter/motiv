import locale
import tkinter as tk
import tkinter.messagebox as mb
from motivate.item import Item
from motivate.views.buttonwidgets import Button

locale.setlocale(locale.LC_ALL, "")
csymb = locale.localeconv()["currency_symbol"]


class Form(tk.LabelFrame):
    """Configures the login page widgets"""

    def __init__(self, form_fields, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._create_form(form_fields)

    def _create_form(self, fields):
        labels = [tk.Label(self, text=f) for f in fields]
        self.entries = [tk.Entry(self) for _ in fields]
        self.form_widgets = list(zip(labels, self.entries))
        for i, (label, entry) in enumerate(self.form_widgets):
            label.grid(row=i, column=0, padx=10, sticky=tk.W)
            entry.grid(row=i, column=1, padx=10, pady=5)


class EarningsForm(Form):
    form_fields = ("Earnings",)

    def __init__(self, item_price, master_widget):
        super().__init__(self.form_fields, master_widget)
        item_price_text = tk.Message(
            master=self, text=f"/{locale.currency(item_price)}", width=100
        ).grid(row=len(self.form_widgets) - 1, column=2)
        button_row = len(self.form_widgets) + 1
        self.start_button = Button(
            master_widget=self, 
            button_text="Start"
        )
        self.pause_button = Button(master_widget=self, button_text="Pause")
        self.reset_button = Button(master_widget=self, button_text="Reset")
        self.start_button.grid(row=button_row, column=0, padx=1)
        self.pause_button.grid(row=button_row, column=1, padx=1)
        self.reset_button.grid(row=button_row, column=2, padx=1)

    def update_earnings(self, money):
        self.entries[0].delete(0, "end")  # tk.END?
        self.entries[0].insert("end", str(locale.currency(money)))

    def bind_start(self, callback):
        self.start_button.bind(callback)

    def bind_pause(self, callback):
        def _callback():
            self.start_button.config(state=tk.ACTIVE)
            self.pause_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.ACTIVE)
            callback()

        self.pause_button.bind(_callback)

    def bind_reset(self, callback):
        def _callback():
            self.start_button.config(state=tk.ACTIVE)
            self.pause_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.DISABLED)
            callback()

        self.reset_button.bind(_callback)


class ItemForm(Form):
    form_fields = "Category", "Name", f"Price, {csymb}"

    def __init__(self, master):
        super().__init__(
            self.form_fields, master, text="Modify An Item or Create Your Own"
        )
        self._create_buttons()

    def _create_buttons(self):
        button_row = len(self.form_widgets) + 1
        self.update_button = Button(master_widget=self, button_text="Update")
        self.delete_button = Button(master_widget=self, button_text="Delete")
        self.save_button = Button(master_widget=self, button_text="Save as New")
        self.update_button.grid(row=button_row, column=0, padx=1)
        self.delete_button.grid(row=button_row, column=1, padx=1)
        self.save_button.grid(row=button_row, column=2, padx=1)

    def get_item_details(self):
        details = [entry.get() for entry in self.entries]
        try:
            return Item(*details)
        except ValueError as e:
            mb.showerror("Validation error", str(e), parent=self)

    def display_item_details(self, item):
        values = (
            item.category,
            item.name,
            locale.currency(float(item.price))[1:],
        )  # change to string. remove
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)  # or call clear_entries?
            entry.insert(0, value)

    def clear_entries(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

    def bind_update(self, callback):
        self.update_button.bind(callback)

    def bind_delete(self, callback):
        self.delete_button.bind(callback)

    def bind_save(self, callback):
        self.save_button.bind(callback)


class SalaryForm(Form):
    form_fields = (f"Annual Salary, {csymb}",)

    def __init__(self, master):
        super().__init__(self.form_fields, master, text="Set Your Salary")

    def get_salary(self):
        # TODO: Check user entry is of appropriate form
        return float(self.entries[0].get())

