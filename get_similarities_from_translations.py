with open('translations.txt', 'r', encoding='utf-8') as f:
    with open('similarities.txt', 'w') as f2:
        for line in f.readlines():
            if line[0:12] != '$@similarity':
                continue
            f2.write(line)
