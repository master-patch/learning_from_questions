import nltk.classify.maxent as maxent
import FeatureSpace
import Sample
import config

def dummy_joint_features(lFeatureTups, sLabel):
    if sLabel == '-1':
        return map(lambda (iIndex, iValue):(iIndex+FeatureSpace.MaxIndex(), iValue), lFeatureTups);
    else:
        return lFeatureTups;


def Train(lTrain):
    lTrainFeatureTups = Sample.SamplesToFeatureTups(lTrain);
    encoder = maxent.FunctionBackedMaxentFeatureEncoding(dummy_joint_features,
                                                         FeatureSpace.MaxIndex()*2,
                                                         ['-1','1']);
    classifier = maxent.MaxentClassifier.train(lTrainFeatureTups, 
                                               encoding = encoder,
                                               algorithm = 'CG');
    return classifier;
    

def Test(classifier, lTest):
    lPreds = [];
    for sample in lTest:
        lFeatures = sample.GetFeatureTupList();
        fProb = classifier.prob_classify(lFeatures).prob('1');
        sample.fPred = fProb;
        lPreds.append(fProb);



def TrainAndTest(lTrain, lTest):
    classifier = Train(lTrain);
    Test(classifier, lTest);
    lAllFeatureWeights = classifier.weights();
    dFeatureWeights = dict(zip(range(len(lAllFeatureWeights)), lAllFeatureWeights));
    return dFeatureWeights;

def TrainAndTestFromGranular(lTrainGranular, lTestGranular):
    if config.get_bool('COLLAPSE_FIRST'):
        assert not config.get_bool('TEST_AND_TRAIN_ON_BOTH_HALVES');
        lTrainCollapsed = Sample.CollapseSamples(lTrainGranular);
        lTestCollapsed = Sample.CollapseSamples(lTestGranular);
        dFeatureWeights = TrainAndTest(lTrainCollapsed, lTestCollapsed);
    else:
        if config.get_bool('TEST_AND_TRAIN_ON_BOTH_HALVES'):
            dFeatureWeights = TrainAndTest(lTrainGranular, lTestGranular);
            TrainAndTest(lTestGranular, lTrainGranular);
            lTestCollapsed = Sample.CollapseSamples(lTrainGranular+lTestGranular);
        else:
            dFeatureWeights = TrainAndTest(lTrainGranular, lTestGranular);
            lTestCollapsed = Sample.CollapseSamples(lTestGranular);
    return lTestCollapsed, dFeatureWeights;

