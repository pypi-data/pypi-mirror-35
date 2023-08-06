from swimlane import Swimlane
from swimlane.core.search import EQ, NOT_EQ, CONTAINS, EXCLUDES, GT, GTE, LT, LTE
import ConfigParser
import re
import os


class Setup:
    def __init__(self, sw_config, sw_inputs):
        self.Config = ConfigParser.ConfigParser()
        self.Config.read("config-sample.ini")
        for k, v in sw_inputs.iteritems():
            #setattr(self, re.sub(r'([a-z])([A-Z])', r'\1_\2', k).lower(), v)
            setattr(self, k.lower(), v)
        for k, v in sw_config.iteritems():
            #setattr(self, re.sub(r'([a-z])([A-Z])', r'\1_\2', k).lower(), v)
            setattr(self, k.lower(), v)

    def ConfigSectionMap(self, section):
        dict1 = {}
        options = Config.options(section)
        for option in options:
            try:
                dict1[option] = Config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1


class Records(Setup):
    def __init__(self, sw_config, sw_inputs, proxySet=False):
        Setup.__init__(self, sw_config, sw_inputs)
        if proxySet:
            os.environ['HTTPS_PROXY'] = self.proxyurl
        self.swimlane = Swimlane(self.slhost, self.slapiuser, self.slapikey, verify_ssl=False)
        self.app = None
        self.appRaw = None
        self.records = None
        self.report = None

    def getApp(self, appId):
        self.app = self.swimlane.apps.get(id=appId)

    def getAppRaw(self, appId):
        self.app = self.swimlane.apps.get(id=appId)
        self.appRaw = self.app._raw

    def getRecord(self, appId, recordId):
        self.getApp(appId)
        self.records = self.app.records.get(id=recordId)

    def getReport(self, appId, reportName, filters=None, limit=50):
        self.getApp(appId)
        self.report = self.app.reports.build(reportName, limit=limit)
        if filters is not None:
            for f in filters:
                self.report.filter(f[0], f[1], f[2])

    def pullFieldsFromRecords(self, appId, recordId, fields=None):
        self.getRecord(appId, recordId)
        if fields is not None:
            oldFields = self.records
            newFields = {}
            for r in oldFields:
                for f in fields:
                    if f in r:
                        newFields[f] = oldFields[f]
            return newFields
        else:
            return self.records