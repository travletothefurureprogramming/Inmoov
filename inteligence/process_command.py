import json
from audio import tts
from tools import ik, uart
from vision import tracker

L1 = 15.0
L2 = 15.0
PING_PONG_W = 4.0

f = 650


def proccess(command_input):
  if isinstance(command_input, str):
    try:
      command = json.loads(command_input)
    except json.JSONDecodeError:
      print("Error: Invalid JSON string received from LLM")
      return
  else:
    command = command_input  

  if "grab" in command:
    object_ = command.get("grab").lower()

    x_center, y_center, pixel_w = tracker.find_object(object_)

    if x_center is not None:
      print(f"Cordinates: X={x_center}, Y={y_center}, Width={pixel_w}")
    else:
      print("The object was not found.")

    if pixel_w is not None:
      Z = ik.z(f, PING_PONG_W, pixel_w)
      X, Y = ik.x_y([640, 480], x_center, y_center, Z, f)

      shoulder_degrees, elbow_degrees = ik.ik(X, Y, L1, L2)
      print(
          "shoulder_degrees: ",
          shoulder_degrees,
          "elbow_degrees: ",
          elbow_degrees,
      )

      uart.send_command(
          f"shoulder_degrees: {round(shoulder_degrees, 2)}"
          f" elbow_degrees: {round(elbow_degrees, 2)}"
      )

  if "coordinates" in command:
    object_ = command.get("coordinates").lower()

    x_center, y_center, pixel_w = tracker.find_object(object_)

    if x_center is not None:
      print(f"Cordinates: X={x_center}, Y={y_center}, Width={pixel_w}")
    else:
      print("The object was not found.")

    if pixel_w is not None:
      Z = ik.z(f, PING_PONG_W, pixel_w)
      X, Y = ik.x_y([640, 480], x_center, y_center, Z, f)

      tts.speak(
          f"I found the {object_} in: X:{round(X)}, Y:{round(Y)}, Z:{round(Z)}"
      )

  if "speak" in command:
    text_ = command.get("speak")
    tts.speak(text_)