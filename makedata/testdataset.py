import makedata.getLiverPatientData

XT, xt, yT, yt = makedata.getLiverPatientData.load_data()
print(XT.shape, xt.shape, yT.shape, yt.shape)
