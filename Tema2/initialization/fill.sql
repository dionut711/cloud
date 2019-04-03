PRAGMA foreign_keys = ON;

DELETE FROM users;

INSERT INTO users VALUES('jimboy', 'Jimmy', 'Boy');
INSERT INTO users VALUES('johnr', 'John', 'Russo');
INSERT INTO users VALUES('bill32', 'Bill', 'Smith');
INSERT INTO users VALUES('DaveB', 'David', 'Brown');
INSERT INTO users VALUES('Ana94', 'Ana', 'Johnson');
INSERT INTO users VALUES('miller_b', 'Brad', 'Miller');
INSERT INTO users VALUES('GeoBush', 'George', 'Bush');
INSERT INTO users VALUES('TheObama', 'Barack', 'Obama');
INSERT INTO users VALUES('Batman', 'Bruce', 'Wayne');


DELETE FROM topics;

INSERT INTO topics (id, name, description) VALUES (1, 'The Lord of the Rings: The Fellowship of the Ring', 'The first movie in the Lord of the Rings trilogy');
INSERT INTO topics (id, name, description) VALUES (2, 'The Lord of the Rings: The Two Towers', 'The second movie in the Lord of the Rings trilogy');
INSERT INTO topics (id, name, description) VALUES (3, 'The Lord of the Rings: The Return of the King', 'The third movie in the Lord of the Rings trilogy');
INSERT INTO topics (id, name, description) VALUES (4, 'Fight Club', 'First rule of fight club');
INSERT INTO topics (id, name, description) VALUES (5, 'Pulp Fiction', 'English mother');
INSERT INTO topics (id, name, description) VALUES (6, 'Inception', 'Dreams in dreams');
INSERT INTO topics (id, name, description) VALUES (7, 'Spider-man', 'Spider-man, Spider-man');
INSERT INTO topics (id, name, description) VALUES (8, 'Spider-man 2', 'Spider-man, Spider-man the sequel');
INSERT INTO topics (id, name, description) VALUES (9, 'Spider-man 3', 'Spider-man, Spider-man the sequel sequel');
INSERT INTO topics (id, name, description) VALUES (10, 'Forest Gump', 'Run Forest, run!');
INSERT INTO topics (id, name, description) VALUES (11, 'Lion King', 'Long live the king');
INSERT INTO topics (id, name, description) VALUES (12, 'Lion King 2', 'Deception, disgrace');
INSERT INTO topics (id, name, description) VALUES (13, 'Good Will Hunting', "It's not your fault");
INSERT INTO topics (id, name, description) VALUES (14, 'John Wick', "No shaky cam");

DELETE FROM reviews;

INSERT INTO reviews VALUES (1, 'jimboy', 1, '9', 'Masterpiece');
INSERT INTO reviews VALUES (2, 'jimboy', 2, '9', 'Another masterpiece');
INSERT INTO reviews VALUES (3, 'johnr', 11, '1', 'I do not have a heart');
INSERT INTO reviews VALUES (4, 'Ana94', 6, '10', 'My favorite');
INSERT INTO reviews VALUES (5, 'miller_b', 11, '9', 'A classic');
INSERT INTO reviews VALUES (6, 'DaveB', 14, '7', 'It was ok');

