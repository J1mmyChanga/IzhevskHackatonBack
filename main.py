from flask import Flask, render_template, request

from api import ApiWrapper, Route, Photo

app = Flask(__name__)
api = ApiWrapper("https://backend.cube-hackaton.ru")


@app.route("/")
def index():
    params = {'request': request, 'title': 'Главная'}
    return render_template("index.html", **params)


@app.route("/tours", methods=['GET', 'POST'])
def tours():
    res = []
    flag = True
    dict = {}
    tours = api.user.get_all(Route)
    for i in tours:
        dict[i.id] = api.photo.get(i.id)
    if request.method == 'POST':
        checkboxes = request.form.getlist('tours')
        if checkboxes:
            if len(checkboxes) != 2:
                if 'us' in checkboxes:
                    flag = False
                for i in tours:
                    if i.activated == flag:
                        res.append(i)
                tours = res
    tours = [tours[i:i + 3] for i in range(0, len(tours), 3)]
    params = {'request': request, 'title': 'Туры', 'tours': tours, 'dict': dict}
    return render_template("tours.html", **params)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
