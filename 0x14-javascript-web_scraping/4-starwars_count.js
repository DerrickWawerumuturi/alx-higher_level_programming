#!/usr/bin/node
import request from "request";
import { argv, exit } from "process";

let base_url = argv[2];
if (argv.length !== 3) {
    console.error('Usage: node app.js <film_id>');
    exit(1)
}
const id = 18;
request(base_url + "/", (error, response, body) => {
    if (error) {
        console.error("Error is: ", error);
        return;
    }

    const films = JSON.parse(body).results;
    const ch_Url = `https://swapi-api.alx-tools.com/api/people/${id}/`; 

    const films_with_wedge = films.filter(film => film.characters.includes(ch_Url));
    console.log(films_with_wedge.length);
})