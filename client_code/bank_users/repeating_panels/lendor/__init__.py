from ._anvil_designer import lendorTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class lendor(lendorTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_id = self.user_id
    user_data=app_tables.fin_user_profile.get(customer_id=user_id)
    if user_data:
      self.image_1.source= user_data['user_photo']

    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    selcted_row=self.item
    open_form('lendor_registration_form.dashboard.lender_view_loans.view_details_1',selected_row=selcted_row)

