use geek_text;

CREATE TABLE Users (
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    created_at DATE,
    deleted_at DATE,
    PRIMARY KEY (id)
);

INSERT INTO Users (name, created_at, deleted_at)
VALUES ('Bill', '2023-06-06', NULL);