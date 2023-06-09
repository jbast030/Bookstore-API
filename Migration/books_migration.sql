use geek_text;

CREATE TABLE books (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name TINYTEXT,
  created_at DATE,
  deleted_at DATE
);
