from ._anvil_designer import star_1_borrower_registration_form_5_bank_1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re

class star_1_borrower_registration_form_5_bank_1(star_1_borrower_registration_form_5_bank_1Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    user_data=app_tables.fin_user_profile.get(customer_id=user_id)
    if user_data:
      self.text_box_1.text=user_data['account_name']
      self.drop_down_1.selected_value=user_data['account_type']
      self.text_box_3.text=user_data['account_number']
      self.text_box_4.text=user_data['bank_name']
      self.bank_id.text=user_data['bank_id']
      self.branch_name.text=user_data['account_bank_branch']
      user_data.update()
      
    options = app_tables.fin_borrower_account_type.search()
    options_string = [str(option['borrower_account_type']) for option in options]
    self.drop_down_1.items = options_string
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.accepted_terms = False
    self.button_2.enabled = False

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    bank_id = self.bank_id.text
    bank_branch = self.branch_name.text
    account_name = self.text_box_1.text
    account_type = self.drop_down_1.selected_value
    account_number = self.text_box_3.text
    bank_name = self.text_box_4.text
    t_and_c = self.check_box_1_copy_2 
    user_id = self.userId
    if not account_name or not account_type or not account_number or not bank_name or not bank_id or not bank_branch or not t_and_c:
        Notification("Please fill all the required fields").show()
    elif not re.match(r'^[A-Za-z\s]+$', account_name):
        Notification("Account name should be valid").show()
    elif not account_number.isdigit():
        Notification("Account number should be valid").show()
    else:
        anvil.server.call('add_borrower_step6', bank_id, bank_branch, user_id)
        anvil.server.call('add_borrower_step5', account_name, account_type, account_number, bank_name, user_id)
        open_form('borrower.dashboard')

  def button_1_click(self, **event_args):
    open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_4_loan',user_id=self.userId)

  def button_3_click(self, **event_args):
    open_form("bank_users.user_form")

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert('Agreements, Privacy Policy and Applicant should accept following:Please note that any information concealed (as what we ask for), would be construed as illegitimate action on your part and an intentional attempt to hide material information which if found in future, would attract necessary action (s) at your sole cost. Hence, request to be truthful to your best knowledge while sharing your details)')

  def check_box_1_copy_2_change(self, **event_args):
        """This method is called when the check box is checked or unchecked"""
        self.accepted_terms = self.check_box_1_copy_2.checked
        self.button_2.enabled = self.accepted_terms