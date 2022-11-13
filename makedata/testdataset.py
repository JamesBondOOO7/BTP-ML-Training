import makedata.getForestFireData

XT, xt, yT, yt = makedata.getForestFireData.load_data()
print(XT.shape, xt.shape, yT.shape, yt.shape)
