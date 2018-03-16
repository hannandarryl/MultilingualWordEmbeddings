# Tokenize All 6 Files

import sentencepiece as spm

spm.SentencePieceTrainer.Train('--input=../data/UNv1.0.6way.train --model_prefix=enfr --vocabsize=8000')