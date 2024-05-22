#!/usr/bin/node
import {readFile} from "fs/promises";
import { argv } from "process";

if (argv.length < 3) {
    console.log('Usage: node read_file.js <file_path>');
    process.exit(1);
}

const file_path = argv[2];

async function readFileContent() {
    try {
        const data = await readFile(file_path, 'utf-8');
        console.log(data);
    } catch (err) {
        console.error(err);
    }
}

readFileContent();