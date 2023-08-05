# -*- coding: utf-8 -*-
import time
from PaasSdk import Config
from PaasSdk.RonyingCommon import RongyingCommon as RongyingCommon
from PaasSdk import RequestModel as models
import PaasSdk.DeveloperCenterConfig as urlConfig


def HttpRequestAppId(config: Config, url: str, body: dict()):
    dt = time.strftime("%Y%m%d%H%M%S", time.localtime())
    sig = RongyingCommon.getmd5string(config.AccountSid + ':' + config.AppId + ':' + dt)
    auth = RongyingCommon.getbase64string((config.AppId + ":" + config.AppIdToken + ":" + dt).encode('utf-8'))
    return RongyingCommon.sendpost(url + sig, body, auth)


def HttpRequestAccount(config: Config, url: str, body: dict()):
    dt = time.strftime("%Y%m%d%H%M%S", time.localtime())
    sig = RongyingCommon.getmd5string(config.AccountSid + ':' + config.AccountToken + ':' + dt)
    auth = RongyingCommon.getbase64string((config.AccountSid + ":" + config.AccountToken + ":" + dt).encode('utf-8'))
    url = url + sig
    return RongyingCommon.sendpost(url, body, auth)


class PaasSendExampleApi:
    def __init__(self):
        pass

    '''
    创建应用
    '''
    def CreateApplications(self, request: models.CreateApplicationsRequestModel) -> dict:
        return HttpRequestAccount(self.config, urlConfig.Host + urlConfig.AppCreateAppCodeUrl, request.to_map())

    def QueryAppidCostRecordDay(self, request: models.AccountsAppIdDayRequestModel):
        url = urlConfig.Host + urlConfig.AppCostDayCodeUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def QueryAppidInfo(self) -> dict:
        url = urlConfig.Host + urlConfig.AppQueryAppDetailCodeUrl
        return HttpRequestAppId(self.config, url, None)

    def QueryAccountAppInfo(self) -> dict:
        url = urlConfig.Host + urlConfig.AppQueryAccountAppCodeUrl
        return HttpRequestAccount(self.config, url, None)

    def AppRechargeRecovery(self, request: models.RechargeRecoveryRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.AppRechargeRecoveryUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def QueryAppidRechargeRecord(self, request: models.RechargeRecoveryRecordRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.AppRechargeLogCodeUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def QueryAppidNumber(self) -> dict:
        url = urlConfig.Host + urlConfig.AppQueryNumberCodeUrl
        return HttpRequestAppId(self.config, url, None)

    def QueryAppidNumber(self) -> dict:
        url = urlConfig.Host + urlConfig.AppQueryNumberCodeUrl
        return HttpRequestAppId(self.config, url, None)

    def AppGoOnline(self) -> dict:
        url = urlConfig.Host + urlConfig.AppGoOnlineUrl
        return HttpRequestAppId(self.config, url, None)

    def AppPause(self) -> dict:
        url = urlConfig.Host + urlConfig.AppPauseUrl
        return HttpRequestAppId(self.config, url, None)

    def AppMontyPackageModel(self,  request: models.AppMontyPackageRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.AppMontyPackageUrl
        return HttpRequestAppId(self.config, url,  request.to_map())

    def AppChangeCallbackUrl(self, request: models.AppChangeCallbackUrlRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.AppChangeCallbackUrlUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def CreateSeatAccount(self, request:  models.CreateSeatAccountRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.SeatCreateUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def ChangeBindNumberSeatAccount(self, request: models.ChangeBindNumberRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.SeatUpdateUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def DeleteBatchSeatAccount(self, request: models.BatchDeleteSeatAccountRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.SeatBatchDeleteUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def DeleteSeatAccount(self, request: models.DeleteSeatAccountRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.SeatDeleteUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def QuerySeatAccountDetail(self, request: models.SeatDetailRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.SeatQueryAcountDetailUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def  QueryAccountSeat(self, request: models.AccountSeatRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.SeatQueryCompanysUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def SeatVerifySmsIssue(self, request: models.SeatVerifyIssueRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.SeatVerifySmsIssueUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def SeatVerifySmsUpStream(self, request: models.SeatVerifyUpstreamRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.SeatVerifySmsUpStreamUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def SeatTransfer(self, request: models.SeatTransferRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.SeatTransferUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def SeatAddPackageRecord(self, request: models.SeatAddPackageRecordRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.SeatAddPackageRecordUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def SeatUnBondSmsIssued(self, request: models.SeatUnBondSmsIssuedCodeRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.SeatUnBondSmsIssuedUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def SeatUnBondSmsUnstream(self, request: models.SeatUnBondSmsCodeUpRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.SeatUnBondSmsUpstreamUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def SeatTrafficStatistics(self, request: models.SeatTrafficStatisticsRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.SeatTrafficStatisticsUrl
        return HttpRequestAppId(self.config, url, request.to_map())

    def SeatTrafficStatisticsTotal(self, request: models.SeatTrafficStatisticsRequestModel) -> dict:
        url = urlConfig.Host + urlConfig.SeatTrafficTotalUrl
        return HttpRequestAppId(self.config, url, request.to_map())
