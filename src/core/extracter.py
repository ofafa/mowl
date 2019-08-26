from pandas import DataFrame as df
import pandas as pd
import os
import copy
from seleniumrequests import Chrome
from tqdm import tqdm
from src.utils.vars import columns_to_merge
from collections import Counter

def load_historical_data(filename_prefix, filename_postfix, lower, upper, merge):

    '''
    Read csv file and merge to one dataframe
    '''
    d = df() if merge else dict()
    for r in range(lower, upper + 1):
        if merge:
            d = d.append(pd.read_csv(filename_prefix + str(r) + filename_postfix))
        else:
            d[r] = pd.read_csv(filename_prefix + str(r) + filename_postfix)
    return d

def merge_columns(data, columns_to_merge):
    '''
    Merge related columns based on columns_to_merge dict
    '''
    d = copy.deepcopy(data)
    for k in tqdm(columns_to_merge):
        d[k] = d[columns_to_merge[k]].apply(lambda x: ''.join(x.dropna().astype(str)), axis=1)
        for c in columns_to_merge[k]:
            del d[c]
    return d


def get_most_common(data, n):
    return Counter(data.apply(lambda x: x.lower())).most_common(n)

# selenium params
login_url = 'https://kktix.com/users/sign_in'
login_email = os.environ['USERNAME_OR_EMAIL']
login_pwd = os.environ['USER_PWD']


def load_recent_ticket_sales_data(event_id):
    '''
    use selenium to login into kktix and fetch event sales
    '''

    # step 1. setup webdriver
    webdriver = Chrome()
    
    # step 2. login with webdriver
    webdriver.get(login_url)
    email_id_el = webdriver.find_element_by_id("user_login")
    passwd_el = webdriver.find_element_by_id("user_password")
    email_id_el.send_keys(login_email)
    passwd_el.send_keys(login_pwd)
    login_button = webdriver.find_element_by_name('commit')
    login_button.click()
    # todo: check login status, if failure, return with warning

    # step 3. now we should be login successfully, 
    # using the cookies to fetch ticket sales data by performing post requersts
    webdriver.get('https://kktix.com/dashboard/events/' + event_id + '/orders')
    export_button = webdriver.find_element_by_link_text('CSV')
    export_button.click()

    # step 4. fetch data from the email sent to login_email
    # todo: using gmail API rather than poplib, which would be very difficult to find the KKTIX email

    # step 5. perform requests.get with the provided email and put the data into somewhere for future analysis