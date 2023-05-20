import requests
from bs4 import BeautifulSoup
import flask
from gpt import GPTClient


app = flask.Flask(__name__)
HEADERS = ({
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5"
})

def _parse_content():
    url = str(flask.request.args.get("url"))
    html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(html, "html.parser")
    return " ".join([paragraph.get_text() for paragraph in soup.find_all("p")])

@app.route("/summarize", methods=["GET"])
def summarize_policy():
    gpt_client = GPTClient()
    policy_content = _parse_content()
    gpt_answer = gpt_client.answer(policy_content, "What types of data are being collected from users?")
    response = flask.jsonify(
        {"data": gpt_answer}
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    app.run(port=9000)
