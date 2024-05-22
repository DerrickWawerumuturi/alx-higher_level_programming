#!/usr/bin/node
import request from 'request';

const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';

const movieId = process.argv[2];

if (!movieId) {
    console.error('Usage: node <script> <movie_id>');
    process.exit(1);
}

const movieUrl = `${baseUrl}${movieId}/`;

request(movieUrl, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        return;
    }

    if (response.statusCode !== 200) {
        console.error(`Failed to fetch movie details. Status code: ${response.statusCode}`);
        return;
    }

    let movie;
    try {
        movie = JSON.parse(body);
    } catch (e) {
        console.error('Error parsing JSON:', e);
        return;
    }

    const characters = movie.characters;

    characters.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
            if (error) {
                console.error('Error:', error);
                return;
            }

            if (response.statusCode !== 200) {
                console.error(`Failed to fetch character details. Status code: ${response.statusCode}`);
                return;
            }

            let character;
            try {
                character = JSON.parse(body);
            } catch (e) {
                console.error('Error parsing JSON:', e);
                return;
            }

            console.log(character.name);
        });
    });
});