from pythonosc.udp_client import SimpleUDPClient
import time

client = SimpleUDPClient("127.0.0.1", 9000)
print("Running... You may now return to VRChat")
print("\n\nOpen VS Code (or other editor of your choice) to change your message")
print("\n(must rerun the .py file after changes are made)")
print("\n\nNot working? Make sure you have OSC enabled")
print("\n\ngithub.com/August-WW/VRC-OSC-Status")
print("\n\n[august wolf]")
while True:
    client.send_message("/chatbox/input", ["(your message)", True, False])
    time.sleep(5)   # Very important - could cause rate limits and other issues without it


# [august wolf]
