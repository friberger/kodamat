from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
))

def getApp():
    return app

@app.route('/')
def hello_world():
    # Render the Template
    return render_template('cluster-test.html')