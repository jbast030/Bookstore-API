use geek_text;

CREATE TABLE book_ratings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT,
    score TINYINT,
    FOREIGN KEY (book_id) REFERENCES books (id)
);

CREATE TABLE book_comments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    book_id INT,
    comment TINYINT
    FOREIGN KEY (user_id) REFERENCES users (id), 
    FOREIGN KEY (book_id) REFERENCES books (id)
);