#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./completedTasks.js <API_URL>');
  process.exit(1);
}

request.get(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasksCompleted = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });

  for (const userId in tasksCompleted) {
    if (Object.prototype.hasOwnProperty.call(tasksCompleted, userId)) {
      console.log(`User ${userId} has completed ${tasksCompleted[userId]} tasks`);
    }
  }
});
