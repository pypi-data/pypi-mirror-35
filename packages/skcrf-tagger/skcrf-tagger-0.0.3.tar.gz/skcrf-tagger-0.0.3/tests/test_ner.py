# -*- coding: utf-8 -*-

import os
import pickle

from skcrf_tagger import Tagger
from skcrf_tagger.utils import text_reader


def train_ner():
    x_data, y_data = text_reader('/tmp/train.txt')
    tag = Tagger()
    tag.fit(x_data, y_data)

    with open('/tmp/test_ner_skcrf.pkl', 'wb') as fp:
        pickle.dump(tag, fp)

    tag = None
    tag = pickle.load(open('/tmp/test_ner_skcrf.pkl', 'rb'))

    score = tag.score(x_data, y_data, verbose=1)
    print('train score', score)
    pred = tag.predict(x_data[:32])
    print('truth')
    print(y_data[0])
    print('predict')
    print(pred[0])
    # assert str(y_data[0]) == str(pred[0]), 'predict should equal to training data'

def test_ner():
    x_data, y_data = text_reader('/tmp/test.txt')
    tag = pickle.load(open('/tmp/test_ner_skcrf.pkl', 'rb'))

    score = tag.score(x_data, y_data, verbose=1)
    print('test score', score)
    pred = tag.predict(x_data[:32])
    print('truth')
    print(y_data[0])
    print('predict')
    print(pred[0])
    # assert str(y_data[0]) == str(pred[0]), 'predict should equal to training data'

if __name__ == '__main__':
    train_ner()
    test_ner()
