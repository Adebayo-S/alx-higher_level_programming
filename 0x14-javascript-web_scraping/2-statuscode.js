#!/usr/bin/node

let url = process.argv[2]
const request = require('request')

request.get(url).on('response', (response) => {
  console.log(`code: ${response.statusCode}`)
})
