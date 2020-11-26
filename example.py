
from ln2sql import Ln2sql

# d = ln2sql.database.Database()
# d.load('/code/ln2sql/pg.sql')
# d.print_me()

ln2sql = Ln2sql(
    database_path='/code/ln2sql/pg.sql',
    language_path='lang_store/english.csv',
    json_output_path='output.json',
    thesaurus_path=None,
    stopwords_path=None,
).get_query('What is the number of web_community with place_name greater than stbridge in this database?')

print(ln2sql)
