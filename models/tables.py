# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.




# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)


import datetime

def get_user_email():
    return None if auth.user is None else auth.user.email

def get_current_time():
    return datetime.datetime.utcnow()

def get_username():
    return None if auth.user is None else auth.user.username

db.define_table('post',
                Field('post_username', default=get_username()),
                Field('post_city'),
                Field('post_price'),
                Field('post_image','text', default=None),
                Field('post_category'),
                Field('post_author', default=get_user_email()),
                Field('post_title'),
                Field('post_description', 'text'),
                Field('post_time', 'datetime', default=get_current_time()),
                )

