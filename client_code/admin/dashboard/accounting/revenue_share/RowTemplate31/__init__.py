# from ._anvil_designer import RowTemplate31Template
# from anvil import *
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables


# class RowTemplate31(RowTemplate31Template):
#   def __init__(self, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)

#     # Any code you write here will run before the form opens.

#   def link_1_click(self, **event_args):
#     # customer_id = self.link_1.text
#     # open_form('admin.dashboard.revenue_share.lender_revenue_share',customer_id)
#     open_form('admin.dashboard.revenue_share.lender_revenue_share', customer_id=self.item['customer_id





from ._anvil_designer import RowTemplate31Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate31(RowTemplate31Template):
  def __init__(self, **properties):
    self.init_components(**properties)

  def link_1_click(self, **event_args):
    customer_id = self.item['customer_id']
    open_form('admin.dashboard.accounting.revenue_share.lender_revenue_share', customer_id=customer_id)
