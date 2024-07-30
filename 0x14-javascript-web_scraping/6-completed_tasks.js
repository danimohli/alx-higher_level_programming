#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./completedTasks.js <API_URL>');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasks = JSON.parse(body);
  const completedTasksByUser = {};

  tasks.forEach((task) => {
    if (task.completed) {
      if (!completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId] = 0;
      }
      completedTasksByUser[task.userId] += 1;
    }
  });

  for (const userId in completedTasksByUser) {
    if (completedTasksByUser.hasOwnProperty(userId)) {
      console.log(`User ${userId} has completed ${completedTasksByUser[userId]} tasks`);
    }
  }
});
