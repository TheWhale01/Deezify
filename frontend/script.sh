#!/bin/bash

npm install

# Prod server: https://stackoverflow.com/questions/73790956/cross-site-post-form-submissions-are-forbidden
# npm run build
# node build

# Dev server
npm run dev -- --port ${PORT} --host ${HOST}
