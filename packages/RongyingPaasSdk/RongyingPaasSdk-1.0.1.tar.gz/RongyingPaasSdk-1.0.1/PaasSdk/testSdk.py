import json

from PaasSdk.CreateRequestClient import CreateRequestClient as Client
from PaasSdk.Config import Config as Config
from PaasSdk import RequestModel as models
from PaasSdk import ResponseModel as responseModels

request = models.CreateApplicationsRequestModel(AppName="python测试")

config = Config(AppId="d5007cb3e2554d28996be7c8bc97afdd",
                AppIdToken="5f3739ac98da4f308e802806920006ad",
                AccountSid="00000000521547df5j41k45f8629801f",
                AccountToken="201181216269332252a816unz3h8la01")
client = Client(config)
dayRequest = models.AccountsAppIdDayRequestModel(Type=1,
                                                 StartTime="2022-12-01",
                                                 EndTime="2022-12-29")


def AppRechargeRecovery():
    rechargeRecoveryRequestModel = models.RechargeRecoveryRequestModel(Banlance=3,
                                                                       Type=1)
    info = client.AppRechargeRecovery(rechargeRecoveryRequestModel)
    print(info.Msg)
    print(info.Flag)


def QueryAccountAppInfo() -> object:
    info = client.QueryAccountAppInfo()
    print(info.Msg)
    print(info.Flag)
    print(info.Total)
    for k in info.Data:
        print(k.CompanyName + "   " + str(k.Banlance))


def QueryAppIdInfo() -> object:
    info = client.QueryAppIdInfo()
    print(info.Msg)
    print(info.Flag)
    print(info.Total)
    for k in info.Data:
        print(k.CompanyName + "   " + str(k.Banlance))


# AppRechargeRecovery()
QueryAccountAppInfo()
# QueryAppIdInfo()

# if info["Flag"] == 200:
#     print(info["Data"])
# else:
#     print(info["Msg"])
