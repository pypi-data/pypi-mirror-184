# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import List


class CreateApplicationsRequestModel:
    def __init__(self,
                 AppName: str = None,
                 CallbackUrl: str = None,
                 SeatStatusUrl: str = None,
                 StatusUrl: str = None):
        self.AppName = AppName
        self.CallbackUrl = CallbackUrl
        self.SeatStatusUrl = SeatStatusUrl
        self.StatusUrl = StatusUrl

    def to_map(self):
        result = dict()
        if self.AppName is not None:
            result['AppName'] = self.AppName
        if self.CallbackUrl is not None:
            result['CallbackUrl'] = self.CallbackUrl
        if self.SeatStatusUrl is not None:
            result['SeatStatusUrl'] = self.SeatStatusUrl
        if self.StatusUrl is not None:
            result['StatusUrl'] = self.StatusUrl
        return result


class AccountsAppIdDayRequestModel:
    def __init__(self,
                 Type: int = None,
                 StartTime: str = None,
                 EndTime: str = None):
        self.Type = Type
        self.StartTime = StartTime
        self.EndTime = EndTime

    def to_map(self):
        result = dict()
        if self.Type is not None:
            result['Type'] = self.Type
        if self.StartTime is not None:
            result['StartTime'] = self.StartTime
        if self.EndTime is not None:
            result['EndTime'] = self.EndTime
        return result

class RechargeRecoveryRequestModel:
    def __init__(self,
                 Banlance: int = None,
                 Type: int = None):
        self.Banlance = Banlance
        self.Type = Type

    def to_map(self):
        result = dict()
        if self.Banlance is not None:
            result['Banlance'] = self.Banlance
        if self.Type is not None:
            result['Type'] = self.Type
        return result

class RechargeRecoveryRecordRequestModel:
    def __init__(self,
                 StartTime: str = None,
                 EndTime: str = None):
        self.StartTime = StartTime
        self.EndTime = EndTime

    def to_map(self):
        result = dict()
        if self.StartTime is not None:
            result['StartTime'] = self.StartTime
        if self.EndTime is not None:
            result['EndTime'] = self.EndTime
        return result

class AppMontyPackageRequestModel:
    def __init__(self,
                 StartDate: str = None,
                 EndDate: str = None):
        self.StartDate = StartDate
        self.EndDate = EndDate

    def to_map(self):
        result = dict()
        if self.StartDate is not None:
            result['StartDate'] = self.StartDate
        if self.EndDate is not None:
            result['EndDate'] = self.EndDate
        return result

class AppChangeCallbackUrlRequestModel:
    def __init__(self,
                 callbackUrl: str = None,
                 stateUrl: str = None,
                 seatStatusUrl: str = None):
        self.callbackUrl = callbackUrl
        self.stateUrl = stateUrl
        self.seatStatusUrl = seatStatusUrl

    def to_map(self):
        result = dict()
        if self.callbackUrl is not None:
            result['callbackUrl'] = self.callbackUrl
        if self.stateUrl is not None:
            result['stateUrl'] = self.stateUrl
        if self.seatStatusUrl is not None:
            result['seatStatusUrl'] = self.seatStatusUrl
        return result
class CreateSeatAccountRequestModel:
    def __init__(self,
                 BindNumber: str = None,
                 Name: str = None,
                 Tsid: int = 0,
                 Type: int = None):
        self.BindNumber = BindNumber
        self.Name = Name
        self.Tsid = Tsid
        self.Type = Type

    def to_map(self):
        result = dict()
        if self.BindNumber is not None:
            result['BindNumber'] = self.BindNumber
        if self.Name is not None:
            result['Name'] = self.Name
        if self.Tsid is not None:
            result['Tsid'] = self.Tsid
        if self.Type is not None:
            result['Type'] = self.Type
        return result

class ChangeBindNumberRequestModel:
    def __init__(self,
                 OldNumber: str = None,
                 Name: str = None,
                 Tsid: int = None,
                 Type: int = 0,
                 NewNumber: str = None):
        self.OldNumber = OldNumber
        self.Name = Name
        self.Tsid = Tsid
        self.Type = Type
        self.NewNumber = NewNumber

    def to_map(self):
        result = dict()
        if self.OldNumber is not None:
            result['OldNumber'] = self.OldNumber
        if self.Name is not None:
            result['Name'] = self.Name
        if self.Tsid is not None:
            result['Tsid'] = self.Tsid
        if self.Type is not None:
            result['Type'] = self.Type
        if self.NewNumber is not None:
            result['NewNumber'] = self.NewNumber
        return result

class BatchDeleteSeatAccountRequestModel:
    def __init__(self,
                 SeatAccount: List[str] = None):
        self.SeatAccount = SeatAccount

    def to_map(self):
        result = dict()
        result['SeatAccount'] = []
        if self.SeatAccount is not None:
            for k in self.SeatAccount:
                result['SeatAccount'].append(k if k else None)
        return result

class DeleteSeatAccountRequestModel:
    def __init__(self,
                 SeatAccount: str = None):
        self.SeatAccount = SeatAccount

    def to_map(self):
        result = dict()
        if self.SeatAccount is not None:
            result['SeatAccount'] = self.SeatAccount
        return result

class SeatDetailRequestModel:
    def __init__(self,
                 SeatAccount: str = None,
                 Mobile: str = None):
        self.SeatAccount = SeatAccount
        self.Mobile = Mobile

    def to_map(self):
        result = dict()
        if self.SeatAccount is not None:
            result['SeatAccount'] = self.SeatAccount
        if self.Mobile is not None:
            result['Mobile'] = self.Mobile
        return result

class AccountSeatRequestModel:
    def __init__(self,
                 Page: int = 1):
        self.Page = Page

    def to_map(self):
        result = dict()
        if self.Page is not None:
            result['Page'] = self.Page
        return result

class SeatVerifyIssueRequestModel:
    def __init__(self,
                 Type: int = 1,
                 Caller: str = None):
        self.Type = Type
        self.Caller = Caller

    def to_map(self):
        result = dict()
        if self.Type is not None:
            result['Type'] = self.Type
        if self.Caller is not None:
            result['Caller'] = self.Caller
        return result

class SeatVerifyUpstreamRequestModel:
    def __init__(self,
                 Code: str = None,
                 Caller: str = None):
        self.Code = Code
        self.Caller = Caller

    def to_map(self):
        result = dict()
        if self.Code is not None:
            result['Code'] = self.Code
        if self.Caller is not None:
            result['Caller'] = self.Caller
        return result

class SeatTransferRequestModel:
    def __init__(self,
                 Appid: str = None,
                 Caller: str = None,
                 Tsid: int = None):
        self.Appid = Appid
        self.Caller = Caller
        self.Tsid = Tsid

    def to_map(self):
        result = dict()
        if self.Appid is not None:
            result['Appid'] = self.Appid
        if self.Caller is not None:
            result['Caller'] = self.Caller
        if self.Tsid is not None:
            result['Tsid'] = self.Tsid
        return result

class SeatAddPackageRecordRequestModel:
    def __init__(self,
                 StartDate: str = None,
                 EndDate: str = None):
        self.StartDate = StartDate
        self.EndDate = EndDate

    def to_map(self):
        result = dict()
        if self.StartDate is not None:
            result['StartDate'] = self.StartDate
        if self.EndDate is not None:
            result['EndDate'] = self.EndDate
        return result

class SeatUnBondSmsIssuedCodeRequestModel:
    def __init__(self,
                 Caller: str = None):
        self.Caller = Caller

    def to_map(self):
        result = dict()
        if self.Caller is not None:
            result['Caller'] = self.Caller
        return result

class SeatUnBondSmsCodeUpRequestModel:
    def __init__(self,
                 Caller: str = None,
                 Code: str = None):
        self.Caller = Caller
        self.Code = Code

    def to_map(self):
        result = dict()
        if self.Caller is not None:
            result['Caller'] = self.Caller
        if self.Code is not None:
            result['Code'] = self.Code
        return result

class SeatTrafficStatisticsRequestModel:
    def __init__(self,
                 SeatAccount: str = None,
                 StartDate: str = None,
                 EndDate: str = None,
                 Page: int = 1):
        self.SeatAccount = SeatAccount
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.Page = Page

    def to_map(self):
        result = dict()
        if self.SeatAccount is not None:
            result['SeatAccount'] = self.SeatAccount
        if self.StartDate is not None:
            result['StartDate'] = self.StartDate
        if self.EndDate is not None:
            result['EndDate'] = self.EndDate
        if self.Page is not None:
            result['Page'] = self.Page
        return result
