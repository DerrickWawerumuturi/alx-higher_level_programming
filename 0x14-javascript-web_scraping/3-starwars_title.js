#!/usr/bin/node
import request from "request";
import { argv } from "process";

let id = argv[2];
let url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, ( error, response, body) => {
    if (error) {
        console.error("Error: ", error);
        return;
    }
    const film = JSON.parse(body);
    console.log(film.title);
;})
