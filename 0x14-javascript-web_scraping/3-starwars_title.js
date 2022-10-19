#!/usr/bin/node

const axios = require('axios');
const id = process.argv[2];
const url = 'http://swapi.co/api/films/' + id + '/';

axios
  .get(url)
  .then((response) => {
    console.log(response.data.title);
  })
  .catch((err) => {
    console.log('code: ' + err.response.status);
  });
