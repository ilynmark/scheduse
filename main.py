from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for

if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SchedUse'

    from pages import page

    app.register_blueprint(page, url_prefix='/')

    app.run(debug=True)
