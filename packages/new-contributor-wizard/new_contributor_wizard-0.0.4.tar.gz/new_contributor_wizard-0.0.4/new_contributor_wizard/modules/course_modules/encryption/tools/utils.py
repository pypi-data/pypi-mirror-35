'''
Utility functions for encryption.tools module
'''


def clean_email(user_email):
    '''
    clean_email removes unnecessary spaces from Full Name
    '''
    return user_email.strip('\t\n\r ')


def clean_name(name):
    '''
    clean_name removes unnecessary spaces from Full Name
    '''
    name = ' '.join(name.split())
    return name.strip('\t\n\r ')


def extract_key_uid_info(uid):
    '''
    extract_key_uid_info returns Name, Email and Comment from the key uid
    uid format would be 'Shashank Kumar (This is a comment) <name@domain.com>'
    '''
    name = uid.split('(')[0].strip(' ')
    name = clean_name(name)

    email = uid.split('<')[1].split('>')[0]
    email = clean_email(email)

    comment = uid.split('(')[1].split(')')[0]

    return {
        'name': name,
        'email': email,
        'comment': comment,
    }
