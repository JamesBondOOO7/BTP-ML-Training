import makedata.getCryotherapyData

XT, xt, yT, yt = makedata.getCryotherapyData.load_data()
print(XT.shape, xt.shape, yT.shape, yt.shape)
