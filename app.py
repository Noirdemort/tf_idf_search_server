from flask import Flask, render_template, redirect, request
from flask_caching import Cache
from tf_idf import results
cache = Cache(config={"CACHE_TYPE": "simple"})

app = Flask(__name__)
cache.init_app(app)


@app.route("/")
def search_page():
    return render_template("index.html")


@app.route("/find/<query>",methods=["GET","POST"])
def find_string(query):
    expansion = list(query.split(" "))
    if len(expansion)<32:
        final_links = results(expansion)
        return str(final_links)
    else:
        return "Too many search words; use under 32 words."
    return "search results"


@app.route("/images", methods=["GET", "POST"])
def search_images():
    data = request.json
    return "media stack"


def subs(data):
    pass # insert into


@app.route("/video", methods=["GET", "POST"])
def serve_video():
    return redirect("/static/real_you.mp4")


@app.route("/txt", methods=["GET", "POST"])
def serve_txt():
    return redirect("/static/fibonacci.py")


@app.route("/pdf", methods=["GET", "POST"])
def serve_pdf():
    return redirect("/static/hack.pdf")


@app.route("/subscribe", methods=["GET", "POST"])
def subscribe():
    data = request.data
    data = data.to_dict()
    my_dict = {
        "mail": data["mail"],
        "subscription": data["pack_type"]
    }
    subs(my_dict)
    return


if __name__ == "__main__":
    app.run(debug=True)
