dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
sentence = input().split()
not_found = [word for word in sentence if word not in dictionary]
if not_found:
    print(*not_found, sep="\n")
else:
    print("OK")