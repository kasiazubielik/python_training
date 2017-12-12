

from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("homepage", contact.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[8]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[8]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[10]").click()
        self.change_field_value("byear", contact.birth_date)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm deletion
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm deletion
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        checkbox = wd.find_element_by_css_selector("input[value='%s']" % id)
        checkbox.click()
        return checkbox

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        self.choose_contact_by_index(index)
        self.fill_contact_form(new_contact_data)
        # submit contact edition
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        checkbox = self.select_contact_by_id(id)
        row = checkbox.find_element_by_xpath("./../..")
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
        # self.choose_contact_by_id(id)
        self.fill_contact_form(new_contact_data)
        # submit contact edition
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def choose_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[8]/a/img")[index].click()

    def choose_contact_by_id(self, id):
        wd = self.app.wd
        # wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[8]/a/img")[index].click()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        wd = self.app.wd
        if self.contact_cache is None:
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                all_phones = cells[5].text
                address = cells[3].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname,
                                                  all_phones_from_home_page=all_phones, address=address, all_emails_from_home_page=all_emails))
        return self.contact_cache

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, phone2=phone2, address=address,
                       email=email, email2=email2, email3=email3)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, phone2=phone2)
