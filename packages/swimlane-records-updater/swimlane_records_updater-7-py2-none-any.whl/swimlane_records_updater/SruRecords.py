from swimlane import Swimlane
from swimlane.core.search import EQ, NOT_EQ, CONTAINS, EXCLUDES, GT, GTE, LT, LTE
import re


class Setup:
    def __init__(self, sw_config, sw_inputs):
        for k, v in sw_inputs.iteritems():
            setattr(self, re.sub(r'([a-z])([A-Z])', r'\1_\2', k).lower(), v)
        for k, v in sw_config.iteritems():
            setattr(self, re.sub(r'([a-z])([A-Z])', r'\1_\2', k).lower(), v)


class Records(Setup):
    def __init__(self, sw_config, sw_inputs):
        Setup.__init__(self, sw_config, sw_inputs)
        self.swimlane = Swimlane(self.host, self.api_user, self.api_key, verify_ssl=False)
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
            oldRecords = self.records
            newRecords = {}
            for r in oldRecords:
                for f in fields:
                    if f in r:
                        newRecords[f] = oldRecords[f]
            return newRecords
        else:
            return self.records
