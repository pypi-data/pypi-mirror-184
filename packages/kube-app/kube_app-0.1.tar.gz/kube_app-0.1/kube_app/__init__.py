"""
General functions for kube.
"""
"""
table = <sales,sales_order,ar,hierarchy,customer,product,target>
"""
import requests
import pandas as pd
from sqlalchemy import create_engine

__all__ = ['Client','pushData', 'getSchema','getData']

class Client:
    def __init__(self,api_key,secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        if (self.secret_key=='abc') & (self.api_key=='abc'):
            self.output = {"Flag":True,"pgsql_url":"4.224.250.105","pgsql_user":"kube_app","pgsql_pwd":"kubeapp","pgsql_port":"5432","pgsql_db":"asdf1234qwer"}
        else:
            self.output = {"Flag":False}

    def getSchema(self,table=None):
        if self.output['Flag']==True:
            return 'Schema'
        else:
            return 'Wrong api_key or secret_key'
        
    def getData():
        return True
    
    def pushData(client,source_data,table,overwrite=True):
        error_message = ''
        if client==True:
            if source_data==None:
                error_message = 'source_data as compulsory argument is not provided'
                return error_message
            if table==None:
                error_message = 'table name as a compulsory argument is not provided'
                return error_message
            else:
                return True
        else:
            return False

    def write_data(df,table,pgsql_url,pgsql_db,pgsql_user,pgsql_pwd,pgsql_port):
        engine = create_engine("postgresql://"+pgsql_user+":"+pgsql_pwd+"@"+pgsql_url+":"+pgsql_port+"/"+pgsql_db+"")
        df.to_sql(table, engine)
