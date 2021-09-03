SELECT prod.name, prod.price, prod.description 
FROM bangazonapi_product as prod
WHERE prod.price > 1000;

SELECT user.first_name || " " || user.last_name as CustomerName, seller.first_name || " " || seller.last_name as SellerName
FROM bangazonapi_favorite as fav, auth_user as user, auth_user as seller
WHERE fav.customer_id = user.id AND fav.seller_id = seller.id;