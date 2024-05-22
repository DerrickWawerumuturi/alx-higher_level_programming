#!/usr/bin/node
import request from "request";
import { argv } from "process";
import { url } from "inspector";
import { error } from "console";

id = argv[2];
let url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, ( error, response, body) => {
    if (error) {
        console.error("Error: ", error);
        return;
    }
    console.log(body);
})