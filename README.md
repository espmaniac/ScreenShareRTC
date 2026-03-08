<p align="center">
  <img src="ico.png" alt="ShareScreenRTC logo" width="128" height="128">
</p>

<h1 align="center">ShareScreenRTC</h1>

ShareScreenRTC is a serverless WebRTC screen sharing page.

- Start broadcast on computer (the link appears only after broadcast+QR start, and that link is a generated `data:text/html` mobile viewer page).
- Scan QR on phone to join.
- Phone generates two things for broadcaster:
  - short response code (6 chars),
  - compact response token (compressed answer payload).
- On computer, type response code (6–8 chars allowed) and enter the compact token.

No Python signaling server is required. The page builds its role/state from URL code parameters (`mode`, `code`, `offer`).

## Flow

1. Broadcaster clicks **Start Broadcast**.
2. Broadcaster shows offer QR to phone.
3. Phone opens viewer mode automatically from the QR URL (which includes mode/code in URL parameters) and generates a short code + compact token.
4. Broadcaster manually enters short code and compact token, then clicks **Apply Response**.

## Run options

### Option A: Local file
Open `index.html` directly.

### Option B: Static host URL
Host the files on any static site.

Both devices should be on the same Wi‑Fi/local network.

## Notes

- Uses `RTCPeerConnection({ iceServers: [] })` for local network behavior.
- The 6–8 character code is only a verifier; WebRTC still requires a compact answer token to complete connection.
- `server.py` is not needed in this workflow.

- If QR image does not appear (for example, CDN blocked), use the shown Broadcast URL code text directly.
- To keep QR payloads small, SDP is reduced to minimal LAN candidates before encoding into URL/token.
- The phone page opened from QR is intentionally minimal: just the video stream and answer output (code + token).
- The shared link is a generated `data:text/html` mobile page (not the broadcaster page URL).
