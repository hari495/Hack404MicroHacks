from flask import Flask, jsonify, render_template



app = Flask(__name__)


event_list = [
	{
		"name": "event 1",
		"time": "8pm",
		"location": "Room 1",
	},
	{
		"name": "event 2",
		"time": "9pm",
		"location": "Room 2"
	}
]

announcement_list = [
	{
		"title":"Announcement 1",
		"content": "this is the first announcement",

	},
	{
		"title":"Announcement 2",
		"content":"This is the second announcement"
	}
]

@app.route("/")
def index():
	return "Gurt Yo"

@app.route("/events", methods = ["GET"])
def events():
	return jsonify(event_list)

@app.route("/announcements", methods=["GET"])
def announcements():
	return jsonify(announcement_list)


@app.route("/dashboard", methods = ["GET"])
def dashboard():
	return render_template("dashboard.html", events=event_list, announcements=announcement_list)

if __name__== "__main__":
	app.run(debug = True, host="127.0.0.1", port=8000)
	