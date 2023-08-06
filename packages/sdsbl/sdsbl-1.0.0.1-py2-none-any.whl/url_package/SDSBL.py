# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api
from gglsbl.client import SafeBrowsingList
from collections import OrderedDict
import json
import time
import sys
import ctypes
import os

OutputDebugStringW = ctypes.windll.kernel32.OutputDebugStringW
OutputDebugStringA = ctypes.windll.kernel32.OutputDebugStringA

app = Flask(__name__)
api = Api(app)

apikey = 'AIzaSyCFrElrbJydAhutM3POgQCZyHMmRV8S6rY'      # Google Safe Browsing API Key
dbpath = 'SDUrl.db'                                     # Local database name
HOST = '0.0.0.0'                                        # Http host info
PORT = '8087'                                           # Http port info

# All threat list parsing
def parsingArray(threat):
    threatlist = OrderedDict()

    threatlist['threatType'] = threat.threat_type
    threatlist['platformType'] = threat.platform_type
    threatlist['threatEntryType'] = threat.threat_entry_type

    if threat.malware_threat_type:
        threatlist['malwareThreatType'] = threat.malware_threat_type
    else:
        threatlist['malwareThreatType'] = 'None'

    return threatlist

# update hash prefix cache
def runSync(sbl):
    try:
        sbl.update_hash_prefix_cache()
        result = 'update success'
    except (KeyboardInterrupt, SystemExit):
        result = 'shutting down'
        sys.exit(0)
    except Exception as e:
        result = str(e)
    except:
        result = 'Failed to synchronize with Google Safe Browsing service'
        time.sleep(3)

    return result

class CheckUrl(Resource):
    def post(self):
        try:
            # JSON Data 유효성 검사
            result = OrderedDict()
            data = request.get_json(force=True)
            OutputDebugStringA('CheckUrl request json = ' + json.dumps(data))

            if 'url' not in data:
                result['error'] = 'There is no "url" key value.'
                OutputDebugStringA('CheckUrl Failed. response json = ' + json.dumps(result))
                return result

            # 요청 전문으로부터 url 파싱하여 Google Safe browsing Api 호출
            url = data['url']
            current_dir = os.path.dirname(sys.argv[0])        
            OutputDebugStringA('Current Dir Path = {}'.format(current_dir))

            real_dbpath = current_dir + '\\' + dbpath
    
            sbl = SafeBrowsingList(apikey, real_dbpath)
            bl = sbl.lookup_url(url)

            # Json Data 생성
            result['url'] = url
            result['threatlist'] = []

            # URL Check 리스트 Json data로 Parsing
            if bl is None:
                OutputDebugStringA('Clean Url')
                result['threatlist'] = 'None'
            else:
                OutputDebugStringA('Malware Url')
                for threat in bl:			
                    threatlist = parsingArray(threat)
                    result['threatlist'].append(threatlist)

            # response
            OutputDebugStringA('CheckUrl response json = ' + json.dumps(result))
            return result

        except Exception as e:
            exceptionResult = OrderedDict()
            exceptionResult['error'] = str(e)
            OutputDebugStringA('google safe browsing exception = ' + json.dumps(exceptionResult))
            return exceptionResult

class UpdateUrl(Resource):
    def post(self):
        # Local Database의 cashed threat list Update
        current_dir = os.path.dirname(sys.argv[0])        
        OutputDebugStringA('Current Dir Path = {}'.format(current_dir))

        real_dbpath = current_dir + '\\' + dbpath
        sbl = SafeBrowsingList(apikey, real_dbpath)

        result = OrderedDict()
        data = runSync(sbl)
        result['result'] = data
        OutputDebugStringA('Update Url Response json = ' + json.dumps(result))

        return result

# URL Router에 mapping (Rest URL 정의)
api.add_resource(CheckUrl, '/CheckUrl')
api.add_resource(UpdateUrl, '/UpdateUrl')

def main():
    app.run(debug = False, host = HOST, port = PORT, threaded=True)

if __name__ == '__main__':
    main()