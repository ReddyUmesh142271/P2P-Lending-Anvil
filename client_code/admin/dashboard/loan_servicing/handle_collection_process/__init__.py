from ._anvil_designer import handle_collection_processTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class handle_collection_process(handle_collection_processTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Fetch data and populate the repeating panel
    self.repeating_panel_1.items = self.fetch_collection_data()

  def fetch_collection_data(self):
    # Search for EMIs with NPA fees greater than 0
    emi_rows = app_tables.fin_emi_table.search(npa_fee=q.greater_than(0))
    data = []

    for emi_row in emi_rows:
      # Fetch the corresponding loan details
      loan_row = app_tables.fin_loan_details.get(loan_id=emi_row['loan_id'])
      if loan_row:
        # Fetch the corresponding user profile based on borrower_customer_id
        user_profile_row = app_tables.fin_user_profile.get(customer_id=loan_row['borrower_customer_id'])
        
        if user_profile_row:
          borrower_image = user_profile_row['user_photo']
          another_email = user_profile_row['another_email']
          # relative_relationship = user_profile_row['relative_relationship']
          street_adress_1 = user_profile_row['street_adress_1']
          street_adress_2 = user_profile_row['street_address_2']

        guarantor_row = app_tables.fin_guarantor_details.get(customer_id=loan_row['borrower_customer_id'])
        if guarantor_row:
          guarantor_name = guarantor_row['guarantor_name']
          guarantor_mobile_no = guarantor_row['guarantor_mobile_no']
          guarantor_address = guarantor_row['guarantor_address']
          another_person = guarantor_row['another_person']

        
        # Combine all the required data
        data.append({
          'status' : 'NPA',
          'loan_id': loan_row['loan_id'],
          'borrower_full_name': loan_row['borrower_full_name'],
          'borrower_customer_id': loan_row['borrower_customer_id'],
          'product_name': loan_row['product_name'],
          'borrower_email_id': loan_row['borrower_email_id'],
          'emi_number': emi_row['emi_number'],
          'total_remaining_amount': emi_row['total_remaining_amount'],
          'image': borrower_image,  # Include the image
          'guarantor_name': guarantor_name,
          'guarantor_mobile_no': guarantor_mobile_no,
          'another_email': another_email,
          'street_adress_1': street_adress_1,
          'guarantor_address': guarantor_address,
          'another_person' : another_person,
          'street_adress_2':street_adress_2,
          
        })
    return data

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_servicing')
