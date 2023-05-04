#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const characters = JSON.parse(body).characters;
  const promises = characters.map((character) => {
    return new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        if (err) {
          reject(err);
        }
        resolve(JSON.parse(body).name);
      });
    });
  }
  );
  Promise.all(promises).then((names) => {
    names.forEach((name) => {
      console.log(name);
    });
  }
  );
});
