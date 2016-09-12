SELECT * FROM languages;
SELECT * FROM cities;
SELECT * FROM countries;

SELECT countries.name, languages.language, languages.percentage
FROM countries
LEFT JOIN languages ON countries.id = languages.country_id
WHERE languages.language = "Slovene"
ORDER BY languages.percentage DESC;

SELECT countries.name, COUNT(cities.id) AS cities_num
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY cities_num DESC;


SELECT cities.name, cities.population
FROM countries
LEFT JOIN cities ON countries.id = cities.country_id
WHERE cities.population > 500000 AND countries.name = "Mexico"
ORDER BY cities.population DESC;

SELECT countries.name, languages.language, languages.percentage
FROM countries
LEFT JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

SELECT countries.name, countries.surface_area,  countries.population
FROM countries
WHERE countries.population > 100000 AND countries.surface_area < 501;

SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE countries.government_form = "Constitutional Monarchy" AND countries.capital > 200 AND countries.life_expectancy > 75;

SELECT countries.name, cities.name, cities.district, cities.population 
FROM countries
LEFT JOIN cities ON countries.id = cities.country_id
WHERE countries.name = "Argentina" AND cities.district = "Buenos Aires" AND cities.population > 500000;

SELECT countries.region, COUNT(countries.id) as Total_Countries
FROM countries
GROUP BY countries.region
ORDER BY Total_Countries DESC;












