import pandas as pd

def gen_csv(promo_csv, contacts_csv):
    '''
    Assign promocode to contacts and convert promocode into html table
    '''
    promo = pd.read_csv(promo_csv)
    contacts = pd.read_csv(contacts_csv)
    contacts['promocode'] = [convert_promo(list(promo['Code'][i*15:(i+1)*15])) for i in range(len(contacts))]
    return contacts


def convert_promo(promocodes):
    html = '<table border="10" style="border-color:blue">'
    for i in range(15):
        if i % 5 == 0:
            html += '<tr>' + '<td>' + promocodes[i] + '</td>'
        elif i % 5 != 4:
            html += '<td>' + promocodes[i] + '</td>'
        else:
            html += '<td>' + promocodes[i] + '</td>' + '</tr>'
    html += '</table>'
    return html