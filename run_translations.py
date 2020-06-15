from pdb import set_trace
import spacy
import os
import random

import wrappers.google_translate, wrappers.mymemory, wrappers.systran_io, wrappers.ibm_watson, wrappers.microsoft, wrappers.nlp_gofitech

services = [
    wrappers.google_translate,
    wrappers.systran_io,
    wrappers.mymemory,
    wrappers.ibm_watson,
    wrappers.microsoft,
    wrappers.nlp_gofitech
]

def run():
    nlp = spacy.load('en_core_web_lg')
    for file in os.listdir('./job_descs')[:1]:
        with open(os.path.join('./job_descs', file), 'r') as f:
            job_desc_original = f.read()

        if len(job_desc_original.strip()) == 0:
            continue
        
        # this rly shldn't be here
        job_desc_original = 'We are looking for an Administrative Support Officer to join our team and support our daily office procedures.' # jd10

        write_to_output("$@filename " + file + '\n' + '$@original' + '\n' + job_desc_original)
        tokens_original = nlp(job_desc_original)
        target_lang = 'zh'#random.choice(['zh','ms','ta'])

        for svc1 in services:
            job_desc_zh = svc1.translate(job_desc_original, 'en', target_lang)
            write_to_output('$@translated ' + svc1.__name__ + '-' + target_lang + '\n' + job_desc_zh)
            similarities = []
            for svc2 in services:
                if svc2 == svc1:
                    continue
                try:
                    job_desc_en_2 = svc2.translate(job_desc_zh, target_lang, 'en')
                except Exception as e:
                    job_desc_en_2 = input('help needed: ' + str(e) + '   ' + svc2.__name__ + ' ' + job_desc_zh)
                write_to_output('$@translatedback ' + svc2.__name__ + '\n' + job_desc_en_2)
                tokens_double_trans = nlp(job_desc_en_2)
                simil = tokens_original.similarity(tokens_double_trans)
                write_to_output(f"$@similarity {svc1.__name__} {svc2.__name__} {target_lang} {str(simil)}")


def write_to_output(string):
    with open('translations.txt', "a", encoding="utf-8") as f:
        f.write(string + '\n')

if __name__ == '__main__':
    run()
