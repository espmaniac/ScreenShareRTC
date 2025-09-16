<p align="center">
  <img src="ico.png" alt="ShareScreenRTC logo" width="128" height="128">
</p>

<h1 align="center">ShareScreenRTC</h1>

ShareScreenRTC is a web application for sharing and viewing live video streams using WebRTC technology.

The app allows you to broadcast your screen or view a broadcast using a modern browser. A Python server is used to automate the signaling process, so you don't need to manually copy and paste the WebRTC offer and answer. With the server, you can simply scan a QR code on your phone and instantly join the stream.

## Features

- Live screen sharing and viewing via WebRTC
- Signaling automation using a simple Python server
- QR code support for easy connection from mobile devices
- No manual copying of SDP offer/answer required when using the server

## How to run the Python server

The signaling server is implemented in pure Python using only standard libraries. You do not need to install any dependencies or use pip.

To start the server, run:

```sh
python3 server.py
```

or, on Windows:

```sh
python server.py
```

The server will listen on port 5000 by default, and you can open the web interface in your browser.