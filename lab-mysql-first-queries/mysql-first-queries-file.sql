-- 1
SELECT prime_genre FROM data
GROUP BY prime_genre;

-- 2
SELECT COUNT(track_name), prime_genre FROM data
WHERE user_rating > 0
GROUP BY prime_genre
ORDER BY COUNT(track_name) DESC;

-- 3
SELECT COUNT(track_name), prime_genre FROM data
GROUP BY prime_genre
ORDER BY COUNT(track_name) DESC;

-- 4
SELECT COUNT(track_name), prime_genre FROM data
GROUP BY prime_genre
ORDER BY COUNT(track_name) ASC;

-- 5
SELECT track_name, rating_count_tot FROM data
ORDER BY rating_count_tot DESC
LIMIT 10;

-- 6
SELECT track_name, rating_count_tot, user_rating FROM data
WHERE user_rating = 5
ORDER BY rating_count_tot DESC
LIMIT 10;

-- 10
SELECT track_name, rating_count_tot, price FROM data
ORDER BY rating_count_tot DESC
LIMIT 50;

