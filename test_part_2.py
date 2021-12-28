import win32clipboard
from selenium.webdriver.support import expected_conditions as expect_conds_
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import generate_alias
from generate_alias import generate_hash
# from shorten_link_test import testing_preparations


def test_part_two(_default_wbd_, _links_list_doubles_):
    wbd_ = _default_wbd_
    print(
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'  # Upper border
        'Second part of the test.\n\n'
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')  # Lower border

    # import shorten_link_test
    # from shorten_link_test import default_wbd_, links_list_, links_list_doubles_
    # from shorten_link_test import links_list_

    # Waiting till website is loaded
    WebDriverWait(wbd_, 100).until(expect_conds_.visibility_of_element_located((By.TAG_NAME, 'body')))
    # Accepts cookies by clicking the button Got it
    cookies_butt_ = wbd_.find_element(By.XPATH, '//button[normalize-space()="Got it"]')
    wbd_.implicitly_wait(20)
    cookies_butt_.click()
    # Repeatedly shorten links from the list
    for idx_ in range(0, _links_list_doubles_.__len__()):  # Repeats the operation for each link
        # run generate_alias
        generate_hash()  # a foo generating random hash for an alias
        wbd_.implicitly_wait(20)
        # Prints link into Input field
        inp_field_ = wbd_.find_element(By.TAG_NAME, 'input').send_keys(
            # shorten_link_test.links_list_doubles_[idx_])
            _links_list_doubles_[idx_])
        wbd_.implicitly_wait(20)
        # Creates an alias
        als_field_ = wbd_.find_element(By.XPATH, '//input[@placeholder="alias"]')
        wbd_.implicitly_wait(20)
        als_field_.clear()
        wbd_.implicitly_wait(20)
        als_field_.send_keys(generate_alias.gener_hash_)
        # als_field_.send_keys('SerAutomatoQATest-' + str(idx_) + '-' + str(repeat_))
        wbd_.implicitly_wait(20)
        # Press button to shorten link
        make_butt_ = wbd_.find_element(By.XPATH, '//button[normalize-space()="Make TinyURL!"]').click()
        wbd_.implicitly_wait(20)
        # Copying the resulting link + alias to clipboard
        copy_butt_ = wbd_.find_element(By.XPATH, '//button[normalize-space()="Copy"]').click()
        wbd_.implicitly_wait(20)
        # Prints to console the value copied on clipboard
        win32clipboard.OpenClipboard()
        data_on_clipboard = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        print(
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
            'Now on clipboard: \n' + str(data_on_clipboard) +
            '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        )  # eof print

        wbd_.implicitly_wait(20)
        # Returns back to shorten another link
        short_another_butt_ = wbd_.find_element(By.XPATH, '//button[normalize-space()="Shorten another"]')
        wbd_.implicitly_wait(20)
        short_another_butt_.click()


# if __name__ == '__main__':
#     test_part_two()
