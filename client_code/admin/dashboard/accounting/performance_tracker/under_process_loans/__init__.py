from ._anvil_designer import under_process_loansTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class under_process_loans(under_process_loansTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # Fetch approved loans data from fin_loan_details table
    self.data = app_tables.fin_loan_details.search(loan_updated_status=q.like('under process'))
        
    # Initialize an empty list to store formatted loan details
    self.result = []
        
    # Iterate through fetched data to format loan details
    for loan in self.data:
        # Retrieve borrower profile information
        borrower_profile = app_tables.fin_user_profile.get(customer_id=loan['borrower_customer_id'])
        if borrower_profile is not None:
            self.result.append({
                    'loan_id': loan['loan_id'],
                    'borrower_email_id': loan['borrower_email_id'],
                    'borrower_customer_id': loan['borrower_customer_id'],
                    'borrower_full_name': loan['borrower_full_name'],
                    'loan_updated_status': loan['loan_updated_status'],
                    # 'interest_rate': loan['interest_rate'],
                    # 'tenure': loan['tenure'],
                    'loan_amount': loan['loan_amount'],
                    'mobile': borrower_profile['mobile'],
                    'product_name': loan['product_name'],
                    # 'product_description': loan['product_description'],
                    # 'loan_disbursed_timestamp': loan['loan_disbursed_timestamp'],
                    'user_photo': borrower_profile['user_photo'],
            })
        
    # Populate repeating panel with formatted loan details
    self.repeating_panel_1.items = self.result
        
    # Display alert if no approved loans found
    if not self.result:
        alert("No under process Loans Available!")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.accounting.performance_tracker')
