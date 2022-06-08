from enum import auto
import scrollphathd, threading
from queue import Queue, Empty
from flask import Blueprint, render_template, abort, request, jsonify, Flask

from lib.action import Action
from lib.autoscroll import Autoscroll
from lib.stoppablethread import StoppableThread


app = Flask(__name__)
port = 5000
api_queue = Queue()

@app.route("/")
def index():
    return jsonify({
        "status": "ok",
    })

@app.route("/write", methods=["POST"])
def write():
    data = request.get_json()
    api_queue.put(Action("write", data["text"]))
    return jsonify({"message": "ok"}), 200

@app.route("/clear", methods=["POST"])
def clear():
    api_queue.put(Action("clear"))

    return jsonify({"message": "ok"}), 200


def cleanup():
    autoscroll.disable()
    scrollphathd.clear()

def run():
    while True:
        action = api_queue.get(block=True)

        if action.action_type == "write":
            cleanup()
            autoscroll.enable()
            scrollphathd.write_string(action.data)

        if action.action_type == "clear":
            cleanup()

        scrollphathd.show()

def start_background_thread():
    api_thread = StoppableThread(target=run)
    api_thread.start()

autoscroll = Autoscroll()

def main():
    start_background_thread()
    scrollphathd.set_clear_on_exit(False)
    app.run(port=port, host="192.168.0.146", debug=True)

if __name__ == "__main__":
    main()