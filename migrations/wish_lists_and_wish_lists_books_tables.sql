use geek_text;

create table wish_lists (
  id int AUTO_INCREMENT PRIMARY KEY,
  user_id int,
  FOREIGN KEY (user_id) references users(id)
);

create table wish_lists_books (
  id int AUTO_INCREMENT PRIMARY KEY,
  wish_list_id int,
  book_id int,
  created_at date,
  deleted_at date,
  FOREIGN KEY (wish_list_id) REFERENCES wish_lists(id),
  FOREIGN KEY (book_id) REFERENCES books(id)
);