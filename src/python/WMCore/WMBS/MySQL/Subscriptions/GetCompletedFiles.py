#!/usr/bin/env python
"""
_AcquireFiles_

MySQL implementation of Subscription.GetCompletedFiles

Return a list of files that are available for processing
"""
__all__ = []
__revision__ = "$Id: GetCompletedFiles.py,v 1.2 2008/06/30 18:00:19 metson Exp $"
__version__ = "$Revision: 1.2 $"

from WMCore.WMBS.MySQL.Base import MySQLBase

class GetCompletedFiles(MySQLBase):
#    sql = """select lfn from wmbs_file_details
#                where id in (
#                     select file from wmbs_sub_files_complete where subscription=:subscription
#                )"""
    sql = "select file from wmbs_sub_files_complete where subscription=:subscription"
    
    def execute(self, subscription=None, conn = None, transaction = False):
        result = self.dbi.processData(self.sql, self.getBinds(subscription=subscription), 
                         conn = conn, transaction = transaction)
        return self.format(result)

