SELECT users.first_name, users.last_name, users2.first_name AS friend_firstname, users2.last_name AS friend_lastname
FROM users
LEFT JOIN friendships
ON users.id = friendships.user_id
LEFT JOIN users as users2
ON friendships.friend_id = users2.id;

