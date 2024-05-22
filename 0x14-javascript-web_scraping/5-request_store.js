#!/usr/bin/node
import request from "request";
import { argv, exit } from "process";
import {writeFile} from "fs/promises";

if (argv.length < 3) {
    console.log(`Usage 5-request_store.js <url> <file_path>`);
    exit(1);
}

const url = argv[2];
const file_path = argv[3];

async function write_file() {
    request(url, (error, response, body) => {
        if (error) {
            console.log('Error: ', error);
        } 
        try {
            writeFile(file_path, body, {encoding: 'utf-8'});
            console.log(`Content saved to ${file_path}`);
        } catch (error) {
            console.error(error);
    }});
};
write_file();