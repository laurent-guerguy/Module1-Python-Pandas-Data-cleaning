-- Challenge 1
SELECT au_id AS Author_ID, au_lname AS Last_Name, au_fname AS First_Name, title AS Title, pub_name AS Publisher FROM titles
JOIN publishers USING(pub_id)
JOIN titleauthor USING(title_id)
JOIN authors USING(au_id)
GROUP BY title, au_id, au_lname, au_fname, pub_name
ORDER BY au_lname;

-- Challenge 2
SELECT au_id AS Author_ID, au_lname AS Last_Name, au_fname AS First_Name, pub_name AS Publisher, COUNT(Title) AS Title_Count FROM titles
JOIN publishers USING(pub_id)
JOIN titleauthor USING(title_id)
JOIN authors USING(au_id)
GROUP BY au_ID, au_lname, au_fname, pub_name
ORDER BY Title_Count DESC, au_lname;

-- Challenge 3
SELECT au_id AS Author_ID, au_lname AS Last_Name, au_fname AS First_Name, SUM(qty) AS TOTAL
FROM authors
LEFT JOIN titleauthor USING(au_id)
LEFT JOIN sales USING(title_id)
GROUP BY au_id
ORDER BY TOTAL DESC
LIMIT 3;

-- Challenge 4
SELECT au_id AS Author_ID, au_lname AS Last_Name, au_fname AS First_Name, IFNULL(SUM(qty),0) AS TOTAL
FROM authors
LEFT JOIN titleauthor USING(au_id)
LEFT JOIN sales USING(title_id)
GROUP BY au_id
ORDER BY TOTAL DESC;