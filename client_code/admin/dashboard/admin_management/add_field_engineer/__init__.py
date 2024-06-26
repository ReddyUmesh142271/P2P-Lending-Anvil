from ._anvil_designer import add_field_engineerTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import date, datetime
from ..... import admin
import re
from .....borrower.dashboard import main_form_module


class add_field_engineer(add_field_engineerTemplate):
  def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # self.user_id = main_form_module.userId
        self.user_id = main_form_module.userId
        self.date_lable.text = date.today().strftime('%d %b %Y')
        self.customer_id = anvil.server.call('generate_field_engineer_id')
        print(self.customer_id)
        # Any code you write here will run before the form opens.
        gender_options = [row['gender'] for row in app_tables.fin_gender.search()]
        # Set the dropdown options
        self.gender.items = gender_options

        self.role.text = 'field engineer'
        # role_options = [row['role'] for row in app_tables.fin_admin_role.search()]
        # # Set the dropdown options
        # self.role.items = role_options
        # user = anvil.users.get_user()
        # Check if a user is logged in
        # if user:
            # Fetch the user profile record based on the current user's email
        user_profile = app_tables.fin_user_profile.get(customer_id=self.user_id)
            # Check if the user profile record is found
        if user_profile:
                # Access the user ID from the user profile record
            self.user_mail = user_profile['email_user']
            self.user_name = user_profile['full_name']
            print(self.user_mail)
            print(self.user_name)

  def save_all_fields_click(self, **event_args):
        email = self.admin_email.text 
        name = self.admin_name.text
        mobile_no = self.mobile_number.text
        address = self.address_text_box.text
        dob = self.dob.date
        gender = self.gender.selected_value
        role = self.role.text
        password = self.create_password_text.text
        retype = self.re_enter_password.text
        created_date = date.today()
        status = True
        ref_admin_name = self.user_name
        ref_admin_email = self.user_mail
        customer_id = self.customer_id
        
        # Validation
        if not all([email, name, mobile_no, dob, gender, role, password ,address]):
            alert("Fill all the fields")
            return

        if password != retype:
            alert("Passwords do not match. Please re-enter.")
            return

        # Regular expression pattern to allow alphabetic characters and underscores
        pattern = r'^[a-zA-Z_ ]+$'
        
        # Check if the name matches the pattern
        if not re.match(pattern, name):
            alert("Name should contain only alphabetic characters and underscores.")
            return

        if not mobile_no.isdigit() or len(mobile_no) != 10:
            alert("Mobile number should contain 10 digits only.")
            return

        dob_str = dob.strftime('%Y-%m-%d')  # Convert date to string
        try:
            dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
        except ValueError:
            alert("Invalid Date of Birth")
            return
    
        age = (date.today() - dob).days // 365  # Calculate age
        if age < 18:
            alert("Age should be 18 years or more.")
            return

        hashed_password = anvil.server.call('hash_password', password)

        result = admin.add_engineers_details(email, name, mobile_no, dob, gender, role, hashed_password, created_date, status, ref_admin_name, ref_admin_email, customer_id,address)

        alert("data added succesfully!")
        open_form('admin.dashboard.admin_management')

  def clear_function_click(self, **event_args):
        # Clear all input fields
        self.admin_email.text = ""
        self.admin_name.text = ""
        self.mobile_number.text = ""
        self.dob.date = None
        self.gender.selected_value = None
        self.role.selected_value = None
        self.create_password_text.text = ""
        self.re_enter_password.text = ""
        self.address_text_box.text = ""

  def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('admin.dashboard.admin_management')
      
