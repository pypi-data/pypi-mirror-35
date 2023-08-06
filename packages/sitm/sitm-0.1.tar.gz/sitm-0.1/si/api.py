import requests
from si.errors import handle_error

class Client:
    def __init__(self, access_token, url='https://app.simpleintelligence.com/_api/'):
        self.url = url
        self._access_token = access_token
        self.__auth = self._access_token
        self.headers = {
            'Authorization': 'apiKey %s' % (self._access_token)
        }

    def __create(self, image, sources=["all"], niceCodes=[]):
        headers = self.headers
        files = {'0': (open(image, 'rb'))}
        sourcesStr = ', '.join('"{0}"'.format(w) for w in sources)
        niceCodesStr = ', '.join('"{0}"'.format(w) for w in niceCodes)

        dataOperations = '{"operationName":"createSearch","variables":{"name":"default","image":null,"sources":[%s],"niceCodes":[%s]},"query":"mutation createSearch($name: String!, $sources: [String!]!, $niceCodes: [String!]!, $image: Upload!) { createSearch(name: $name, sources: $sources, niceCodes: $niceCodes, image: $image) { id __typename }}"}' % (sourcesStr, niceCodesStr)
        dataMap = '{"0":["variables.image"]}'

        response = requests.post(self.url, data={'operations': dataOperations, 'map': dataMap}, files=files, headers=headers)

        if response.status_code == 200:
            return response.json()

        exc = handle_error(response)
        exc.__cause__ = None
        raise exc

        # if request.status_code == 200:
        #     return request.json()
        
        # if request.status_code == 401:
        #     raise SimpleIntelligenceAuthError()

        # raise SimpleIntelligenceError(request.status_code)

    def __search(self, id):
        headers = self.headers

        request = requests.post(self.url, json={
            'operationName': "searchQuery",
            'variables': {'id': id},
            'query': "query searchQuery($id: ID!) {search(id: $id) {  id  name  sources  niceCodes  image {    name    base64    __typename  }  owner {    name    email    __typename  }  results {    data {      id      index      name      date      status      models {        id        name        score        rawScore        __typename      }      source {        name        __typename      }      holder {        name        __typename      }      brand {        name        __typename      }      industries {        id        source {          id          __typename        }        __typename      }      image {        name        src        base64        __typename      }      __typename    }    __typename  }  __typename}\n}\n"
        }, headers=headers)

        if request.status_code == 200:
            return request.json()
        
        if request.status_code == 401:
            raise SimpleIntelligenceAuthError()

        raise SimpleIntelligenceError(request.status_code)

    def search(self, image, sources=['all'], niceCodes=[]):
        createResponse = self.__create(image, sources, niceCodes)
        searchId = createResponse['data']['createSearch']['id']

        searchResponse = self.__search(searchId)
        return searchResponse['data']['search']