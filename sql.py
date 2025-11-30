import sqlite3

connection = sqlite3.connect("rdm_exposure_detailed_fct.db")

cursor =connection.cursor()

table_info=""" create table rdm_exposure_detailed_fct(fic_mis_date  date,v_cust_id varchar(25),
v_cust_name varchar(25),f_fb_nfb_nslr_deriv varchar(20), n_outstanding_amount int, n_total_exposure int);

"""

table_info1=""" create table customer_info(v_cust_id  VARCHAR2(100),v_cust_industry varchar(25),
v_cust_name varchar(25), v_cust_nationality varchar(20), passport varchar2(100),DOB DATE);

"""


cursor.execute(table_info)
cursor.execute(table_info1)

cursor.execute(''' insert into rdm_exposure_detailed_fct values ('24-11-25','841111229','AAbb','FB',5224542564,12345678) ''')
cursor.execute(''' insert into rdm_exposure_detailed_fct values ('24-11-25','841111298','AAcc','NFB',5224554,65485278) ''')
cursor.execute(''' insert into rdm_exposure_detailed_fct values ('24-11-25','841111777','AAss','FB',5224569254,25896478) ''')
cursor.execute(''' insert into rdm_exposure_detailed_fct values ('24-11-25','841111666','AAqq','NFB',5222254,456789452) ''')
cursor.execute(''' insert into rdm_exposure_detailed_fct values ('24-11-25','841111555','AAtt','FB',5542254,456789452) ''')
cursor.execute(''' insert into rdm_exposure_detailed_fct values ('24-11-25','841111444','AAhh','NFB',54542254,456789452) ''')
cursor.execute(''' insert into rdm_exposure_detailed_fct values ('24-11-25','841111333','AAii','FB',5222254,456789452) ''')
cursor.execute(''' insert into rdm_exposure_detailed_fct values ('24-11-25','841111221','AAoo','FB',54542254,456789452) ''')
cursor.execute(''' insert into rdm_exposure_detailed_fct values ('24-11-25','841111759','AAyy','NFB',5222254,456789452) ''')

cursor.execute(''' insert into customer_info values ('841111229','IRON AND STEEL','AAbb','INDIA','A12345','22-09-93') ''')
cursor.execute(''' insert into customer_info values ('841111298','TEXTILE','AAcc','USA','B12345','22-08-93') ''')
cursor.execute(''' insert into customer_info values ('841111777','FOOD PROCESSING','AAss','CANADA','C12345','22-07-93') ''')
cursor.execute(''' insert into customer_info values ('841111666','IRON AND STEEL','AAqq','INDIA','D12345','22-06-93') ''')
cursor.execute(''' insert into customer_info values ('841111555','IRON AND STEEL','AAtt','INDIA','E12345','22-05-93') ''')





print ("the inserted records are")

data = cursor.execute('''select * from rdm_exposure_detailed_fct ''')
for row in data:
    print (row)

connection.commit()
connection.close()
