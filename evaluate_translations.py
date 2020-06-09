import json
with open('similarities.txt', 'r') as f:
    results = {
        'zh': {'_count':0},
        'ms': {'_count':0},
        'ta': {'_count':0}
    }
    for line in f.readlines():
        split_line = line.split(' ')
        svc1, svc2, lang, simil = split_line[1:]
        simil = float(simil)
        lang_dict = results[lang]
        lang_dict['_count'] += 1
        lang_dict[svc1] = lang_dict.get(svc1, 0) + simil
        lang_dict[svc2] = lang_dict.get(svc2, 0) + simil

for lang_dict in results.values():
    num_svcs = len(lang_dict.keys()) - 1
    if num_svcs == 0:
        continue
    lang_dict['_count'] /= num_svcs * (num_svcs - 1)
    quotient = lang_dict['_count'] * ((num_svcs - 1) * 2)
    for svc in lang_dict.keys():
        if svc == '_count':
            continue
        lang_dict[svc] /= quotient

print(json.dumps(results, indent=2))
