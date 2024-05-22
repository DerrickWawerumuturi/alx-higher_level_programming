#!/usr/bin/node
import { error } from "console";
import request from "request";

if (process.argv.length !== 3) {
    console.error('Usage: node 2-statuscode.js <URL>');
    process.exit(1);
}

const url = process.argv[2];

request(url, (error, res) => {
    if (error) {
        console.log(`Error:`, error);
        process.exit(1);
    }
    console.log(`code: ${res.statusCode}`);
})