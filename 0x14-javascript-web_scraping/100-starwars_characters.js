#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.error('Usage: ./printCharacters.js <Movie_ID>');
  process.exit(1);
}

request.get(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
    return;
  }

  const characters = body.characters;

  characters.forEach((characterUrl) => {
    request.get(characterUrl, { json: true }, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }
      if (charResponse.statusCode !== 200) {
        console.error(`Failed to retrieve character data. Status code: ${charResponse.statusCode}`);
        return;
      }

      console.log(charBody.name);
    });
  });
});
