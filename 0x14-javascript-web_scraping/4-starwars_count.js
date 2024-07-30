#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

if (!apiUrl) {
  console.error('Usage: ./countWedgeAntilles.js <API_URL>');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;

  films.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.includes(characterId)) {
        count++;
      }
    });
  });

  console.log(count);
});
