#!/usr/bin/node
import {writeFile} from "fs/promises"
import { argv } from "process";

if (argv.length < 4) {
    console.log('Usage: node read_file.js <file> <string>');
    process.exit(1);
}

let file = argv[2];
let data = argv[3];

async function write_file() {
    try {
        writeFile(file, data, (err) => {
            if (err) console.error(err);
        })
    } catch (err) {
        console.log(err);
    }
}
write_file();
