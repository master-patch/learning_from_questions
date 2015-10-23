import codecs;
import string;
import os;
import gzip;
import json;
import jsonpickle;
import copy;
import csv;
import unicodedata;
import random

#this defines all the object types which we expect to put in files
jsonpickle.set_encoder_options('simplejson',indent=4);
jsonpickle.set_encoder_options('json',indent=4);

def obj_to_file(obj, sFileName):
    #fOut = open(sFileName, 'w');
    #json.dump(obj = json.loads(jsonpickle.encode(obj)), fp=fOut, indent=4);
    #json pickle version 4 fixes the problems so we can get indention without
    # playing games
    obj_to_file_fast(obj, sFileName);

def obj_to_file_gz(obj, sFileName):
    #fOut = gzip.open(sFileName, 'w');
    #json.dump(obj = json.loads(jsonpickle.encode(obj)), fp=fOut, indent=4);
    obj_to_file_gz_fast(obj, sFileName);

def obj_to_file_gz_fast(obj, sFileName):
    gzip.open(sFileName, 'w').write(jsonpickle.encode(obj));

def obj_to_file_fast(obj, sFileName):
    open(sFileName, 'w').write(jsonpickle.encode(obj));

def print_obj(obj):
    print obj_to_string(obj);

def obj_to_string(obj):
    return json.dumps(json.loads(jsonpickle.encode(obj)), indent=4);

def obj_to_compact_string(obj):
    return json.dumps(json.loads(jsonpickle.encode(obj)));
    #return jsonpickle.encode(obj);

dFileCache = {};

def file_to_obj(sFileName):
    try:
        timeLastMod = os.stat(sFileName)[8];
        if sFileName in dFileCache:
            timeLastRead, oRead = dFileCache[sFileName];
            if timeLastRead == timeLastMod:
                return oRead;
        oRead = jsonpickle.decode(open(sFileName).read());
        dFileCache[sFileName] = (timeLastMod, oRead);
    except:
        print "FAILED TO OPEN/READ/PARSE FILE:", sFileName
        raise
    return oRead;

def RemoveComments(sLine):
    lSplit = sLine.split('#');
    if len(lSplit) != 1:
        return lSplit[0]+'\n';
    else:
        return sLine;

def file_to_obj_with_comments(sFileName):
    lInputLines = open(sFileName).readlines();
    #lInputLinesNoComments = map(lambda x:x.split('#')[0], lInputLines);
    lInputLinesNoComments = map(lambda x:RemoveComments(x), lInputLines);
    sInput = ''.join(lInputLinesNoComments);
    return jsonpickle.decode(sInput);


def file_to_obj_gz(sFileName):
    return jsonpickle.decode(gzip.open(sFileName).read());

def pretty_print(sFileName):
    print_obj(file_to_obj_gz(sFileName));


