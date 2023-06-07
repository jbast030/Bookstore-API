use geek_text;

CREATE TABLE shopping_carts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE shopping_cart_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    shopping_cart_id INT,
    book_id INT,
    created_at DATE,
    deleted_at DATE,
    FOREIGN KEY (shopping_cart_id) REFERENCES shopping_carts(id)
);