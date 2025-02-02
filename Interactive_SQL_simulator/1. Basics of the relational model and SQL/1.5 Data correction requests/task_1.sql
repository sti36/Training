/*Задание
Создать таблицу поставок (supply), которая имеет ту же структуру, что и таблиц book.

Поле	    Тип, описание
supply_id	INT PRIMARY KEY AUTO_INCREMENT
title	    VARCHAR(50)
author	    VARCHAR(30)
price	    DECIMAL(8, 2)
<<<<<<< HEAD
amount	    INT */ 
=======
amount	    INT */
>>>>>>> 7744352a3d982482660b9dfa2d809d7b4af5d963

CREATE TABLE supply (
     supply_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50),
    author VARCHAR(30),
    price DECIMAL(8, 2),
    amount INT
)