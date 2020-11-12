
SELECT_ALL = '''select * from shoes'''

# DEPARTMENT_INSERT = '''
#     insert into department(department_name,created_dt,modified_dt,
#     created_by,modified_by,is_active) values (%s,now(),now(),%s,%s,True)
#     '''
# DEPARTMENT_SELECT_ALL = '''select * from estabs_tbl'''
#
# DEPARTMENT_SELECT='''select department_id,department_name from department where is_active=True  and department_id=%s'''
#
# DEPARTMENT_UPDATE = '''
#     update department set department_name=%s,modified_by=%s, modified_dt=now() where department_id=%s
#     '''
# DEPARTMENT_DELETE='''
# delete from department where department_id=%s
# '''
#
#
# DB_CREATE='''
# CREATE TABLE department (
#     department_id SERIAL PRIMARY KEY,
#     department_name character varying(40),
#     created_dt date,
#     modified_dt date,
#     created_by character varying(40),
#     modified_by character varying(40),
#     is_active boolean
# )
# '''
#
#
# DROP_TABLE='''
# drop table department
# '''
