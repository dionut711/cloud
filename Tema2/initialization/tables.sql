DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS topics;

PRAGMA foreign_keys = ON;

CREATE TABLE users (
    username TINYTEXT NOT NULL PRIMARY KEY,
    first_name TINYTEXT NOT NULL,
    last_name TINYTEXT NOT NULL
);

CREATE TABLE topics (
    id INTEGER NOT NULL PRIMARY KEY,
    name TINYTEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE reviews (
    id INTEGER NOT NULL PRIMARY KEY,
    user TINYTEXT NOT NULL,
    subject_id INTEGER NOT NULL,
    score SMALLINT NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY(user) REFERENCES users(username) ON DELETE CASCADE,
    FOREIGN KEY(subject_id) REFERENCES topics(id) ON DELETE CASCADE
);
