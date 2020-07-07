from flask import Flask, render_template, request
from views import *


app = Flask(__name__)


if __name__ == '__main__':
    app.run()
