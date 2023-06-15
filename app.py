# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('./index.html')
    
from flask import Flask
from config import API_KEY

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    # Get the parameters from the request
    serviceKey = API_KEY
    LAWD_CD = request.args.get('LAWD_CD', default=11110)
    DEAL_YMD = request.args.get('DEAL_YMD', default=202201)
    # 사용법
    #GET /api?param1=value1&param2=value2
    #GET /api?param1=value1
    #GET /api?param2=value2
    api_url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent?serviceKey={serviceKey}&LAWD_CD={LAWD_CD}&DEAL_YMD={DEAL_YMD}'
    response = requests.get(api_url)
    data = response.json()
    items = data['response']['body']['items']['item']
    return {'data': items}

if __name__ == '__main__':
    app.run()