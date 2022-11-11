import makedata.getBreastCancerData
import makedata.getCryotherapyData


def load_data(name="breastCancer"):
    if name == "breastCancer":
        return makedata.getBreastCancerData.load_data()
    elif name == "cryotherapy":
        return makedata.getCryotherapyData.load_data()

    return None
