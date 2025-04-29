import pandas as pd
from sqlalchemy import create_engine
df=pd.DataFrame({'sno':[1,2],'sname':['张三','王麻子'],'score':[100,99]})
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/stu')
df.to_sql('student', engine, if_exists='replace', index=False)