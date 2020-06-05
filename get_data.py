import requests
from pdb import set_trace
import json
import re

URL_GET_JOB_IDS = 'https://api.mycareersfuture.sg/v2/jobs?limit={limit}&page={page}&sortBy=new_posting_date&omitCountWithSchemes=true'
URL_GET_JOB_DESC = 'https://api.mycareersfuture.sg/v2/jobs/{job_id}'

responses = []

for i in range(6):
    # 100 is the max we are allowed to request for at once.
    formatted_url = URL_GET_JOB_IDS.format(limit=100,page=i)
    responses.extend(
        requests.get(
            url=formatted_url
        ).json()['results']
    )

skip_count = 0

for i, response in enumerate(responses):
    # some chars cannot be written? gives a UnicodeEncodeError. we just ignore those.
    # rationale: there's no reason to believe there's a significant difference between the descriptions
    # of jobs with such chars, and jobs without. thus it doesn't influence the investigation.
    try:
        job_id = response['uuid']
        job_json = requests.get(
            url=URL_GET_JOB_DESC.format(job_id=job_id)
        ).json()
        job_desc = job_json['description']

        html_tag_regex = re.compile(r'<.*?>')
        job_desc = re.sub(html_tag_regex, '', job_desc)
        job_desc = job_desc.replace('&nbsp;', ' ')

        with open(f'./job_descs/jd{str(i)}', 'w') as f:
            f.write(job_desc)
    except:
        skip_count += 1
        continue

print(f'{skip_count} skipped')
