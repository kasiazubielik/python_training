

class AddressHelper:

    def __init__(self, app):
        self.app = app

    def open_address_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, address):
        wd = self.app.wd
        # init address creation
        wd.find_element_by_link_text("add new").click()
        self.fill_address_form(address)
        # submit address creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_address_form(self, address):
        wd = self.app.wd
        self.change_field_value("firstname", address.firstname)
        self.change_field_value("middlename", address.middlename)
        self.change_field_value("lastname", address.lastname)
        self.change_field_value("nickname", address.nickname)
        self.change_field_value("title", address.title)
        self.change_field_value("company", address.company)
        self.change_field_value("address", address.address)
        self.change_field_value("home", address.home_phone)
        self.change_field_value("mobile", address.mobile_phone)
        self.change_field_value("work", address.work_phone)
        self.change_field_value("fax", address.fax)
        self.change_field_value("email", address.email)
        self.change_field_value("email2", address.email2)
        self.change_field_value("email3", address.email3)
        self.change_field_value("homepage", address.homepage)
        self.change_field_value("email", address.email)
        self.change_field_value("email2", address.email2)
        self.change_field_value("homepage", address.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[8]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[8]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[10]").click()
        self.change_field_value("byear", address.birth_date)
        self.change_field_value("address2", address.address2)
        self.change_field_value("phone2", address.phone2)
        self.change_field_value("notes", address.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_address(self):
        wd = self.app.wd
        self.open_address_page()
        self.select_first_address()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm deletion
        wd.switch_to_alert().accept()

    def select_first_address(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_address(self, new_adress_data):
        wd = self.app.wd
        self.open_address_page()
        self.select_first_address()
        # edit address form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_address_form(new_adress_data)
        # submit address edition
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def count(self):
        wd = self.app.wd
        self.open_address_page()
        return len(wd.find_elements_by_name("selected[]"))
