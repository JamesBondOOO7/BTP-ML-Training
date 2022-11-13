import makedata.getAuditRiskData

XT, xt, yT, yt = makedata.getAuditRiskData.load_data()
print(XT.shape, xt.shape, yT.shape, yt.shape)
