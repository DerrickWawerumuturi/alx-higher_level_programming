#!/usr/bin/node
import request from "request";
import { argv, exit } from "process";

const url = process.argv[2];

if (!url) {
    console.error('Usage: node 6-completed_tasks.js <url>');
    process.exit(1);
}

request(url, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        return;
    }

    let tasks;
    try {
        tasks = JSON.parse(body);
    } catch (e) {
        console.error('Error parsing JSON:', e);
        return;
    }

    const userTasks = {};

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

    for (const userId in userTasks) {
        console.log(`${userId} : ${userTasks[userId]}`);
    }
});