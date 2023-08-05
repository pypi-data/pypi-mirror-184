# add my own installation to path. It is 2 levels up from this file.
import sys, os

sys.path.insert(0, (os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))))
# sys.path.insert(0, 'C:/Users/Mike/Sync/code/mypysurreal/')


import pysurrealdb as surreal

conn = surreal.connect(user='test', password='test', database='test', namespace='test')
# conn = surreal.connect(user='test', password='test', database='main', namespace='main')
# conn = surreal.connect(host='https://sparkling-cherry-9759.fly.dev', user='proth', password='passicus', database='test', namespace='test')



conn.drop('person')
conn.insert('test', {'id': 1 , 'name': 'test', 'age': 20.65, 'description': 'Test'})
# conn.query("insert into test {'id': 2 , 'name': 'test2', 'age': 20.65}")
# conn.insert('person', {'id': 2 , 'name': 'test', 'age': 2, 'description': '"This" is `a` test of strange encoding characters.'})
conn.insert('test', {'id': 3 , 'name': 'test', 'age': 12, 'description': '"This" is `a` test of strange encoding characters.'})
# conn.insert('person', {'id':69 ,'name': "'test'", 'age': 42, 'description': "'This' is `a` test of strange encoding characters."})

# print(conn.query('select total from profiler'))
# print(conn.get("profiler"))
# conn.drop('profiler')
# print(conn.query('select * from profiler'))
# print(conn._send_chunks("select * from person"))
# table = 'person'
# print(conn.create_large(table, {'id': 1 , 'name': 'test', 'age': 31, 'description': 'Test'}))

print(conn.table('test').where_not_in('age', [2, 12]).get())