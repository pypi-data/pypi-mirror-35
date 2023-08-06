from store.postgres.dictionary import DictionaryStore



def user_store(table, db='user', usr='dameng', pwd='hello'):
    return DictionaryStore({'user': usr, 'password': pwd, 'name': db, 'table': table})
