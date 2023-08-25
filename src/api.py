import requests
from bs4 import BeautifulSoup
import flask
from flask_restful import Api, Resource
from flask_cors import CORS
from gpt import GPTClient


HEADERS = ({
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5"
})

app = flask.Flask(__name__)
api = Api(app)
cors = CORS(app)

class PPExtensionApi(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.gpt_client = GPTClient()

    def _parse_content_from_url(self, url):
        html = requests.get(url, headers=HEADERS).text
        soup = BeautifulSoup(html, "html.parser")
        return " ".join([paragraph.get_text() for paragraph in soup.find_all("p")])

    def post(self):
        request_body = flask.request.json
        url = request_body.get("url")
        api_key = request_body.get("apiKey")
        organization_id = request_body.get("orgId")
        policy_content = self._parse_content_from_url(url)
        if not self.gpt_client.validate_privacy_policy(policy_content, api_key, organization_id):
            response = flask.Response("The webpage does not contain a privacy policy", 404)
            return response
        gpt_answer = self.gpt_client.summarize_policy(policy_content, api_key, organization_id)
        response = flask.jsonify(
            {"data": gpt_answer}
        )
        return response

api.add_resource(PPExtensionApi, "/summarize")

if __name__ == "__main__":
    app.run(port=80)
