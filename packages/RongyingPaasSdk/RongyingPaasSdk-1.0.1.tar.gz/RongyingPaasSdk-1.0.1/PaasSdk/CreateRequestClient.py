from PaasSdk import Config as Config
from PaasSdk.PaasSendExampleApi import PaasSendExampleApi as PaasSendExampleApi
from PaasSdk import RequestModel as models
from PaasSdk import ResponseModel as responseModels


class CreateRequestClient:
    def __init__(
            self,
            config: Config):
        self.config = config

    def CreateApplications(self,
                           request: models.CreateApplicationsRequestModel
                           ) -> responseModels.CreateApplicationsResponseModel:
        data = PaasSendExampleApi.CreateApplications(self, request)
        return responseModels.CreateApplicationsResponseModel.from_map(self, data)

    def QueryAppIdCostRecordDay(self,
                                request: models.AccountsAppIdDayRequestModel
                                ) -> responseModels.AccountsAppIdDayResponseModel:
        data = PaasSendExampleApi.QueryAppidCostRecordDay(self, request)
        return responseModels.AccountsAppIdDayResponseModel.from_map(self, data)

    def QueryAppIdInfo(self) -> responseModels.AppIdInfoResponseModel:
        data = PaasSendExampleApi.QueryAppidInfo(self)
        return responseModels.AppIdInfoResponseModel.from_map(self, data)

    def QueryAccountAppInfo(self) -> responseModels.AppIdInfoResponseModel:
        data = PaasSendExampleApi.QueryAccountAppInfo(self)
        return responseModels.AppIdInfoResponseModel.from_map(self, data)

    def AppRechargeRecovery(self, request: models.RechargeRecoveryRequestModel) -> responseModels.BaseResponseModel:
        data = PaasSendExampleApi.AppRechargeRecovery(self, request)
        return responseModels.BaseResponseModel.from_map(self, data)

    def QueryAppIdRechargeRecord(self,
                                 request: models.RechargeRecoveryRecordRequestModel
                                 ) -> responseModels.RechargeRecoveryRecordResponseModel:
        data = PaasSendExampleApi.AppRechargeRecovery(self, request)
        return responseModels.RechargeRecoveryRecordResponseModel.from_map(self, data)

    def QueryAppIdNumber(self) -> responseModels.AppIdNumberResponseModel:
        data = PaasSendExampleApi.QueryAppidNumber(self)
        return responseModels.AppIdNumberResponseModel.from_map(self, data)

    def AppGoOnline(self) -> responseModels.BaseResponseModel:
        data = PaasSendExampleApi.AppGoOnline(self)
        return responseModels.BaseResponseModel.from_map(self, data)

    def AppPause(self) -> responseModels.BaseResponseModel:
        data = PaasSendExampleApi.AppPause(self)
        return responseModels.BaseResponseModel.from_map(self, data)

    def AppMontyPackageModel(self,
                             request: models.AppMontyPackageRequestModel
                             ) -> responseModels.AppMontyPackageResponseModel:
        data = PaasSendExampleApi.AppMontyPackageModel(self, request)
        return responseModels.AppMontyPackageResponseModel.from_map(self, data)

    def AppChangeCallbackUrl(self,
                             request: models.AppChangeCallbackUrlRequestModel
                             ) -> responseModels.BaseResponseModel:
        data = PaasSendExampleApi.AppChangeCallbackUrl(self, request)
        return responseModels.BaseResponseModel.from_map(self, data)

    def CreateSeatAccount(self,
                          request: models.CreateSeatAccountRequestModel
                          ) -> responseModels.CreateSeatAccountResponseModel:
        data = PaasSendExampleApi.CreateSeatAccount(self, request)
        return responseModels.CreateSeatAccountResponseModel(self, data)

    def ChangeBindNumberSeatAccount(self,
                                    request: models.ChangeBindNumberRequestModel
                                    ) -> responseModels.BaseResponseModel:
        data = PaasSendExampleApi.ChangeBindNumberSeatAccount(self, request)
        return responseModels.BaseResponseModel(self, data)

    def DeleteBatchSeatAccount(self,
                               request: models.BatchDeleteSeatAccountRequestModel
                               ) -> responseModels.BaseResponseModel:
        data = PaasSendExampleApi.DeleteBatchSeatAccount(self, request)
        return responseModels.BaseResponseModel(self, data)

    def DeleteSeatAccount(self,
                          request: models.DeleteSeatAccountRequestModel
                          ) -> responseModels.BaseResponseModel:
        data = PaasSendExampleApi.DeleteSeatAccount(self, request)
        return responseModels.BaseResponseModel(self, data)

    def QuerySeatAccountDetail(self,
                               request: models.SeatDetailRequestModel
                               ) -> responseModels.SeatDetailResponseModel:
        data = PaasSendExampleApi.QuerySeatAccountDetail(self, request)
        return responseModels.SeatDetailResponseModel(self, data)

    def QueryAccountSeat(self,
                         request: models.AccountSeatRequestModel
                         ) -> responseModels.SeatDetailResponseModel:
        data = PaasSendExampleApi.QueryAccountSeat(self, request)
        return responseModels.SeatDetailResponseModel(self, data)

    def SeatVerifySmsIssue(self,
                           request: models.SeatVerifyIssueRequestModel
                           ) -> responseModels.BaseResponseModel:
        data = PaasSendExampleApi.SeatVerifySmsIssue(self, request)
        return responseModels.BaseResponseModel(self, data)

    def SeatVerifySmsUpStream(self,
                              request: models.SeatVerifyUpstreamRequestModel
                              ) -> responseModels.BaseResponseModel:
        data = PaasSendExampleApi.SeatVerifySmsUpStream(self, request)
        return responseModels.BaseResponseModel(self, data)

    def SeatTransfer(self,
                     request: models.SeatTransferRequestModel
                     ) -> responseModels.BaseResponseModel:
        data = PaasSendExampleApi.SeatTransfer(self, request)
        return responseModels.BaseResponseModel(self, data)

    def SeatUnBondSmsIssued(self,
                            request: models.SeatUnBondSmsIssuedCodeRequestModel
                            ) -> responseModels.BaseResponseModel:
        data = PaasSendExampleApi.SeatUnBondSmsIssued(self, request)
        return responseModels.BaseResponseModel(self, data)

    def SeatUnBondSmsUnstream(self,
                              request: models.SeatUnBondSmsCodeUpRequestModel
                              ) -> responseModels.BaseResponseModel:
        data = PaasSendExampleApi.SeatUnBondSmsUnstream(self, request)
        return responseModels.BaseResponseModel(self, data)

    def SeatTrafficStatistics(self,
                              request: models.SeatTrafficStatisticsRequestModel
                              ) -> responseModels.SeatTrafficStatisticsResponseModel:
        data = PaasSendExampleApi.SeatTrafficStatistics(self, request)
        return responseModels.SeatTrafficStatisticsResponseModel(self, data)

    def SeatTrafficStatisticsTotal(self,
                                   request: models.SeatTrafficStatisticsRequestModel
                                   ) -> responseModels.SeatTrafficStatisticsTotalResponseModel:
        data = PaasSendExampleApi.SeatTrafficStatisticsTotal(self, request)
        return responseModels.SeatTrafficStatisticsTotalResponseModel(self, data)
