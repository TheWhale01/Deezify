# Deezify
Deezify is a project to create a common queue between the spotify and deezer services.
It's made with FastAPI, SvelteJS and PostgreSQL. Hope you'll enjoy it.

> **_NOTE:_** It's a preview: meaning only Spotify and Deezer are supported and no clients
other than web client are neither supported

A hosted instance can be found at: [https://deezify.thewhale.duckdns.org](https://deezify.thewhale.duckdns.org)

## Installation
1. create `.env` directory in the root of the project
2. create the following files:
    - `backend.env`
    - `frontend.env`
    - `db.env`
    - `pgadmin.env` *_Optional_*
3. Fill in the necessary variables:
    > **_NOTE:_** TODO
4. Run the `docker compose up --buil -d` command

## Usage
Frontend will be accessible at `http://localhost:8080` and backend at `http://localhost:3000`
