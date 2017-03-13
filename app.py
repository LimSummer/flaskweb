import sys,logging
import utils.log
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def show_entries():
    return redirect('/static/index.html')

if __name__ == "__main__":
    logger = logging.getLogger('timerotating')
    app.run(debug=False)
    logger.info("app.py")