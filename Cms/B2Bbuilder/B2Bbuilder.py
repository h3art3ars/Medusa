#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.B2Bbuilder import B2BbuilderBackgroundCommandExecutionVulnerability
from Cms.B2Bbuilder import B2BbuilderContainsVulnerabilitiesLocally
from Cms.B2Bbuilder import B2BbuilderHeadSQLInjectionVulnerability
from Cms.B2Bbuilder import B2BbuilderSQLInjectionVulnerability
from Cms.B2Bbuilder import B2BbuilderSQLInjectionVulnerability2
from Cms.B2Bbuilder import B2BbuilderSQLInjectionVulnerability3
from Cms.B2Bbuilder import B2BbuilderSQLInjectionVulnerability4
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(B2BbuilderBackgroundCommandExecutionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(B2BbuilderContainsVulnerabilitiesLocally.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(B2BbuilderHeadSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(B2BbuilderSQLInjectionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(B2BbuilderSQLInjectionVulnerability2.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(B2BbuilderSQLInjectionVulnerability3.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(B2BbuilderSQLInjectionVulnerability4.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] B2Bbuilder component payload successfully loaded\033[0m")
    time.sleep(0.5)