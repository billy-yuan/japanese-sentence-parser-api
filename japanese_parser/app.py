
from flask import Flask, request
from flask_restful import Resource, Api
from japanese_parser import get_words_from_sentence


app = Flask(__name__)
api = Api(app)


class JapaneseSentenceParser(Resource):
    def post(self):
        sentence = request.json["sentence"]
        words = get_words_from_sentence(sentence)

        return {"sentence": sentence, "words": words}


api.add_resource(JapaneseSentenceParser, '/japanese_sentence_parser')

if __name__ == "__main__":
    app.run()
