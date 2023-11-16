#!/usr/bin/node

const axios = require('axios');
const movieID = process.argv[2];

if (!movieID || isNaN(movieID)) {
  console.log('Please provide a valid movie ID as an argument');
  process.emit(1);
}

const base_url = 'https://swapi-api.alx-tools.com/api';
const films_endpoint = '/films/'

axios.get (`${base_url}${films_endpoint}${movieID}`)
  .then(response => {
    const characters = response.data.characters;
    return Promise.all(characters.map(characterURL => axios.get(characterURL)));
  })
  .then(charactersData => {
    const characterName = charactersData.map(character => character.data.name);
    characterName.forEach(name => 
      console.log(name)
      );
  })
  .catch(error => {
    console.error('Error fetching data:', error.message);
  });
