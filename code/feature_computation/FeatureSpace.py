
class FeatureSpace:
    def __init__(self):
        self.dFeatureToIndex = {};
        self.dIndexToFeature = {};
        # svm light requires feature indexes to start at 1
        self.iIndex = 1;

    def FeatureIndex(self, sFeature):
        if sFeature in self.dFeatureToIndex:
            return self.dFeatureToIndex[sFeature];
        else:
            self.dFeatureToIndex[sFeature] = self.iIndex;
            self.dIndexToFeature[self.iIndex] = sFeature;
            self.iIndex += 1;
            return self.iIndex-1;

fs = FeatureSpace();

def FeatureIndex(sFeature):
    return fs.FeatureIndex(sFeature);

def FeatureString(iIndex):
    return fs.dIndexToFeature[iIndex];

def MaxIndex():
    return fs.iIndex;

