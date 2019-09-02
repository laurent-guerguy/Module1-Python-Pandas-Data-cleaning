-- Challenge 1
-- Step1
SELECT title_id, au_id, t.price * s.qty * (t.royalty / 100) * (ta.royaltyper / 100) AS sales_royalty, 
au_lname, au_fname, royaltyper, title, price, advance, royalty, qty FROM authors AS a
LEFT JOIN titleauthor as ta
USING(au_id)
LEFT JOIN titles AS t
USING(title_id)
LEFT JOIN sales AS s
USING(title_id)
ORDER BY sales_royalty DESC;

-- Step 2
SELECT title_id, title, au_id, au_fname, au_lname, SUM(t.price * s.qty * (t.royalty / 100) * (ta.royaltyper / 100)) AS sales_royalty
FROM authors AS a
LEFT JOIN titleauthor as ta
USING(au_id)
LEFT JOIN titles AS t
USING(title_id)
LEFT JOIN sales AS s
USING(title_id)
GROUP BY au_id, title_id
ORDER BY sales_royalty DESC;

-- Step 3 
-- Note: We create the advance_prop variable which is the proportion of advance received by the author 
-- for each book (because in the case of having co-authors the advance for this title has to be shared 
-- between authors). The total profits are the sum of the sales_royalty with advance_prop.
-- 
SELECT au_id, au_fname, au_lname, sales_royalty + advance_prop AS Total_profits
FROM(
	SELECT au_id, au_fname, au_lname, sales_royalty, advance, advance * royaltyper / 100 AS advance_prop
		FROM(
		SELECT title_id, au_id, au_fname, au_lname, SUM(t.price * s.qty * (t.royalty / 100) * (ta.royaltyper / 100)) AS sales_royalty, advance, royaltyper
		FROM authors AS a
		LEFT JOIN titleauthor as ta
		USING(au_id)
		LEFT JOIN titles AS t
		USING(title_id)
		LEFT JOIN sales AS s
		USING(title_id)
		GROUP BY au_id, title_id
		ORDER BY sales_royalty DESC)
        table1)
	table2
LIMIT 3;


-- Challenge 2
-- We don't have the rights to use CREATE TEMPORARY TABLE

-- Challenge 3
-- We don't have the rights to use CREATE TABLE in the publications database