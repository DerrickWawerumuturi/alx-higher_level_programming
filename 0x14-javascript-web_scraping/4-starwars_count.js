#!/usr/bin/node
import request from "request";
import { argv } from "process";
import { error } from "console";

let base_url = argv[2];
const id = 18
request(base_url, (error, response, body) => {
    if (error) {
        console.error("Error: ", error);
        return;
    }

    const film = JSON.parse(body);
    const charactersUrls = film.characters;

    const wedgeAntiles =  charactersUrls.find(`https://swapi-api.alx-tools.com/api/people/${id}`);

    request(wedgeAntiles, (error, response, body) => {
        if (error) {
            console.error("Error: ", error);
        }
        const films = JSON.parse(body);
        const number_films =  films.length;

        console.log(number_films);
    })

})