from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for

page = Blueprint('page', __name__)


@page.route('/', methods=['GET', 'POST'])  # homepage
def home():

    return render_template("page1.html")


@page.route('/page2.html', methods=['GET', 'POST'])  # user page
def userinfo():
    if request.method == 'GET':
        return render_template("page2.html")
    if request.method == 'POST':
        passdata = {'name':request.form.get('name'), 'sleepfrom': request.form.get('sleepfrom'), 'sleepuntil': request.form.get('sleepuntil')}
        return redirect(url_for('.tasks', messages=passdata))
        # return '<p>' + repr(passdata) + '</p>'
        # return render_template("page3.html")
    # else: return render_template("page2.html")

@page.route('/page3.html', methods=['GET', 'POST'])  # user page
def tasks():
    # return '<p>' + repr(request.args.get('messages')) + '</p>'
    return render_template("page3.html")


@page.route('/page4.html', methods=['GET', 'POST'])  # graph page
def graph():
    if request.method == 'POST':
        return

    return render_template("page4.html")
