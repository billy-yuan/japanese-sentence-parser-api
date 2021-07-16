from flask import Flask, request
from flask_restful import Resource, Api
from japanese_parser import get_words_from_sentence


app = Flask(__name__)
api = Api(app)


@api.resource('/japanese_sentence_parser')
class JapaneseSentenceParser(Resource):
    def post(self):
        request_data = request.get_json()
        sentence = request_data["sentence"]
        words = get_words_from_sentence(sentence)

        return {"sentence": sentence, "words": words}


if __name__ == "__main__":
    app.run()
