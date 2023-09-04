CREATE DATABASE chat;

USE chat;

CREATE TABLE chat_messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(255)
);