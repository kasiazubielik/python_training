
import re

def test_phones_on_home_page(app):
    address_from_home_page = app.address.get_address_list()[0]
    address_from_edit_page = app.address.get_address_info_from_edit_page(0)
    assert address_from_home_page.home_phone == clear(address_from_edit_page.home_phone)
    assert address_from_home_page.mobile_phone == clear(address_from_edit_page.mobile_phone)
    assert address_from_home_page.work_phone == clear(address_from_edit_page.work_phone)
    assert address_from_home_page.phone2 == clear(address_from_edit_page.phone2)

def test_phones_on_contact_view_paga(app):
    address_from_view_page = app.address.get_address_from_view_page(0)
    address_from_edit_page = app.address.get_address_info_from_edit_page(0)
    assert address_from_view_page.home_phone == address_from_edit_page.home_phone
    assert address_from_view_page.mobile_phone == address_from_edit_page.mobile_phone
    assert address_from_view_page.work_phone == address_from_edit_page.work_phone
    assert address_from_view_page.phone2 == address_from_edit_page.phone2

def clear(s):
    return re.sub("[() +-]", "", s)
