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

    const userTasks  = {}
    const tasks = JSON.parse(body);

    for (let i = 0; i < tasks.length; i++) {
        const task = tasks[i];
        if (task.completed === true) {
            if (userTasks[task.userId]) {
                userTasks[task.userId]++;
            } else {
                userTasks[task.userId] = 1;
            }
        }
    }
    const result = {};
    for (const userId in userTasks) {
        result[userId] = userTasks[userId];
    }
    console.log(result);
});