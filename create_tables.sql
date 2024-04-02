CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE
);

CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    status_id INTEGER REFERENCES status(id),
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);

CREATE UNIQUE INDEX IF NOT EXISTS unique_email ON users(email);
CREATE UNIQUE INDEX IF NOT EXISTS unique_status_name ON status(name);

ALTER TABLE tasks
ADD CONSTRAINT fk_status
FOREIGN KEY (status_id)
REFERENCES status(id);

ALTER TABLE tasks
ADD CONSTRAINT fk_users
FOREIGN KEY (user_id)
REFERENCES users(id)
ON DELETE CASCADE;
