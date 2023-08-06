import requests
import responses
import sys
import os
import unittest

path = os.path.abspath('../')
sys.path.append(path)
from piomart import EnsembleClient as pio

# resp = requests.get('http://twitter.com/api/1/foobar')
# response.add('http://rest.ensembl.org')
# #Too Many Requests
# if resp.status_code == 429:
#     if 'Retry-After' in resp.headers:
#         retry = resp['Retry-After']
#         time.sleep(float(retry))
#         self.perform_rest_action()
# #Gateway Timeout
# elif resp.status_code == 504

# else:
#     self.r.raise_for_status()
#     sys.exit()
    
# r = requests.get('http://github.com')
# print(r.headers)

@responses.activate
def test_simple():
    responses.add(responses.GET, 'http://rest.ensembl.org',
                  json={'Retry-After': 1.0232}, status=429)

    resp = requests.get('http://rest.ensembl.org')
    server = "https://rest.ensembl.org"
    ext = "/lookup/id/ENSG00000157764?expand=1"
    header =  { "Content-Type" : "application/json"}
    pio().rest_request(ext,header,["ENST"],responses.calls[0], resp.json())

    # self.r = requests.post(query, headers=headers, data=gene_json)    
    # print(responses.call[0])

    # assert resp.json() == {"error": "not found"}
    # print(responses.calls[0].response.text)

    # assert len(responses.calls) == 1
    # assert responses.calls[0].request.url == 'http://rest.ensembl.org'
    # assert responses.calls[0].response.text == '{"error": "not found"}'
test_simple()
