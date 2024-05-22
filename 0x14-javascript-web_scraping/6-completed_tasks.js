#!/usr/bin/node
import request from "request"
import { argv, exit } from "process"

const base_url = argv[2];
if (argv.length < 2) {
    console.log(`Usage: <filename> <api_url>`);
    exit(1);
}

request(base_url, (error, res, body) => {
    if (error) {
        console.error("Error is: ", error);
    }

    const tasks = JSON.parse(body);
    console.log(typeof tasks);
})