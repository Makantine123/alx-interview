#!/usr/bin/node
/* Star Wars API */

const request = require('request');

function getMovieCharacters(movieId) {
  return new Promise((resolve, reject) => {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

    request(url, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        reject(error || new Error(`Failed to fetch data from API. Status code: ${response.statusCode}`));
        return;
      }

      const film = JSON.parse(body);
      const characterPromises = film.characters.map(characterUrl => {
        return new Promise((resolve, reject) => {
          request(characterUrl, (error, response, body) => {
            if (error || response.statusCode !== 200) {
              reject(error || new Error(`Failed to fetch character data. Status code: ${response.statusCode}`));
              return;
            }

            resolve(JSON.parse(body).name);
          });
        });
      });

      Promise.all(characterPromises)
        .then(characters => resolve(characters))
        .catch(reject);
    });
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId)
  .then(characters => characters.forEach(character => console.log(character)))
  .catch(error => console.error('Error:', error.message));
