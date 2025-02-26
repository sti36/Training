--Вывести информацию (автора, название и цену) о тех книгах, цены которых превышают минимальную цену книги на складе не более чем на 150 рублей в отсортированном по возрастанию цены виде.

SELECT author, title, price
FROM book
WHERE (price - (SELECT MIN(price) FROM book)) <=150
ORDER BY price ASC