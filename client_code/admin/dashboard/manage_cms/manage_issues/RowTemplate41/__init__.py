from ._anvil_designer import RowTemplate41Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from collections import Counter



class RowTemplate41(RowTemplate41Template):
  def __init__(self, **properties):
    self.init_components(**properties)
   

   
  def button_1_click_click(self, **event_args):
    selected_row = self.item
    # customer_details = app_tables.fin_reported_problems.search()
    
    # Count occurrences of each customer_id
    # customer_ids = [row['customer_id'] for row in customer_details]
    # customer_id_counts = Counter(customer_ids)
    
    # # Check for duplicate customer_ids
    # duplicate_ids = [customer_id for customer_id, count in customer_id_counts.items() if count > 1]
    
    # if duplicate_ids:
    #   alert('Duplicate customer IDs found: ' + ', '.join(map(str, duplicate_ids)))
    # else:
    open_form('admin.dashboard.manage_cms.manage_issues.field_engineer', selected_row=selected_row)
