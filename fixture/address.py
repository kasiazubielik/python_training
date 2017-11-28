

from model.address import Address
import re


class AddressHelper:

    def __init__(self, app):
        self.app = app

    def open_address_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, address):
        wd = self.app.wd
        # init address creation
        wd.find_element_by_link_text("add new").click()
        self.fill_address_form(address)
        # submit address creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.address_cache = None

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

    def delete_address_by_index(self, index):
        wd = self.app.wd
        self.open_address_page()
        self.select_address_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm deletion
        wd.switch_to_alert().accept()
        self.address_cache = None

    def delete_first_address(self):
        self.delete_address_by_index(0)

    def select_address_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_address_by_index(self, index, new_address_data):
        wd = self.app.wd
        self.open_address_page()
        self.choose_address_by_index(index)
        self.fill_address_form(new_address_data)
        # submit address edition
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.address_cache = None

    def modify_first_address(self):
        self.modify_address_by_index(0)

    def choose_address_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[8]/a/img")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_address_page()
        return len(wd.find_elements_by_name("selected[]"))

    address_cache = None

    def get_address_list(self):
        wd = self.app.wd
        if self.address_cache is None:
            self.open_address_page()
            self.address_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                all_phones = cells[5].text.splitlines()
                self.address_cache.append(Address(id=id, firstname=firstname, lastname=lastname,
                                                  home_phone=all_phones[0], mobile_phone=all_phones[1],
                                                  work_phone=all_phones[2], phone2=all_phones[3]))
        return self.address_cache

    def open_address_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_address_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_address_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_address_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Address(firstname=firstname, lastname=lastname, id=id,
                       home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, phone2=phone2)

    def open_address_view_by_index(self, index):
        wd = self.app.wd
        self.open_address_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_address_from_view_page(self, index):
        wd = self.app.wd
        self.open_address_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Address(home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, phone2=phone2)
