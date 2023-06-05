from flask import Flask, render_template, url_for, request, redirect
from matplotlib import pyplot as plt
import fastf1.plotting as ff1Plot
from io import BytesIO
import fastf1 as ff1
import base64

app = Flask(__name__)

ff1.Cache.enable_cache("cache")

def sOnD(listOfDriver, year, event, ses):
    ff1Plot.setup_mpl()
    session = ff1.get_session(year, event, ses)
    session.load()

    fig, ax = plt.subplots()
    for driver in listOfDriver:
        PilotData = session.laps.pick_driver(driver).pick_fastest()
        PilotTel = PilotData.get_car_data().add_distance()
        ax.plot(PilotTel['Distance'], PilotTel['Speed'], color=ff1Plot.team_color(PilotData["Team"]), label=driver)

    ax.set_xlabel('Distance in m')
    ax.set_ylabel('Speed in km/h')

    ax.legend()
    plt.suptitle(f"Fastest Lap \n {session.event['EventName']} {session.event.year} {ses}")

    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    html = "data:image/png;base64,{}".format(encoded)

    return html

def dOnT(listOfDriver, year, event, ses):
    ff1Plot.setup_mpl()
    session = ff1.get_session(year, event, ses)
    session.load()

    fig, ax = plt.subplots()
    for driver in listOfDriver:
        PilotData = session.laps.pick_driver(driver).pick_fastest()
        PilotTel = PilotData.get_car_data().add_distance()
        ax.plot(PilotTel['Time'], PilotTel['Distance'], color=ff1Plot.team_color(PilotData["Team"]), label=driver)

    ax.set_xlabel('Time in s')
    ax.set_ylabel('Distance in m')

    ax.legend()
    plt.suptitle(f"Fastest Lap \n {session.event['EventName']} {session.event.year} {ses}")

    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    html = "data:image/png;base64,{}".format(encoded)

    return html

def sOnT(listOfDriver, year, event, ses):
    ff1Plot.setup_mpl()
    session = ff1.get_session(year, event, ses)
    session.load()

    fig, ax = plt.subplots()
    for driver in listOfDriver:
        PilotData = session.laps.pick_driver(driver).pick_fastest()
        PilotTel = PilotData.get_car_data().add_distance()
        ax.plot(PilotTel['Time'], PilotTel['Speed'], color=ff1Plot.team_color(PilotData["Team"]), label=driver)

    ax.set_xlabel('Time in s')
    ax.set_ylabel('Speed in km/h')

    ax.legend()
    plt.suptitle(f"Fastest Lap \n {session.event['EventName']} {session.event.year} {ses}")

    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    html = "data:image/png;base64,{}".format(encoded)

    return html

def tOnD(listOfDriver, year, event, ses):
    ff1Plot.setup_mpl()
    session = ff1.get_session(year, event, ses)
    session.load()

    fig, ax = plt.subplots()
    for driver in listOfDriver:
        PilotData = session.laps.pick_driver(driver).pick_fastest()
        PilotTel = PilotData.get_car_data().add_distance()
        ax.plot(PilotTel['Distance'], PilotTel['Time'], color=ff1Plot.team_color(PilotData["Team"]), label=driver)

    ax.set_xlabel('Distance in m')
    ax.set_ylabel('Time in s')

    ax.legend()
    plt.suptitle(f"Fastest Lap \n {session.event['EventName']} {session.event.year} {ses}")

    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    html = "data:image/png;base64,{}".format(encoded)

    return html

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/choose-round', methods=["GET", "POST"])
def chooseRound():
    if request.method == "POST":
        select = int(request.form.get("year"))

        events = ff1.get_event_schedule(select)

        countryList = []
        countryList.extend(events['EventName'].tolist())

        return render_template("chooseRound.html", countryList=countryList, year=select)
    else:
        return redirect(url_for("home"))

@app.route('/result', methods=["GET", "POST"])
def result():
    if request.method == "POST":
        year = int(request.form["year"])
        event = request.form["round"]
        ses = request.form["session"]
        graphics = request.form["graphics"]
        listOfDriver = request.form.getlist("driver")

        if graphics == "sOnD":
            html = sOnD(listOfDriver, year, event, ses)
            return render_template("result.html", html=html)
        elif graphics == "dOnT":
            html = dOnT(listOfDriver, year, event, ses)
            return render_template("result.html", html=html)
        elif graphics == "sOnT":
            html = sOnT(listOfDriver, year, event, ses)
            return render_template("result.html", html=html)
        elif graphics == "tOnD":
            html = tOnD(listOfDriver, year, event, ses)
            return render_template("result.html", html=html)
        else:
            return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

@app.route('/choose-graphics', methods=['GET', 'POST'])
def graphicsChoose():
    if request.method == "POST":
        year = int(request.form["year"])
        event = request.form["round"]
        ses = request.form["session"]

        session = ff1.get_session(year, event, ses)

        try :
            session.load()

            drivers = session.laps["Driver"]

            listOfDriver = []

            for driver in drivers:
                if driver in listOfDriver:
                    listOfDriver = listOfDriver
                else:
                    listOfDriver.append(driver)

            return render_template("chooseGraphic.html", year=year, event=event, ses=ses, listOfDriver=listOfDriver)
        except :
            return render_template("sessionNotAccessible.html")
    else:
        return redirect(url_for("home"))