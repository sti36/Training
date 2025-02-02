/*Задание
Занести из таблицы supply в таблицу book только те книги, авторов которых нет в  book.*/

INSERT INTO book (title, author, price, amount) 
SELECT title, author, price, amount 
FROM supply
WHERE author NOT IN (
        SELECT author 
        FROM book
<<<<<<< HEAD
    ) 
=======
    )
>>>>>>> 7744352a3d982482660b9dfa2d809d7b4af5d963
