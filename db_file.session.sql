SELECT prod.name, prod.price, prod.description 
FROM bangazonapi_product as prod
WHERE prod.price > 1000;

SELECT ord.id as OrderId, pay.merchant_name as PaymentType, SUM(prod.price) as OrderTotal, user.first_name || " " || user.last_name as FullName
FROM bangazonapi_order as ord, bangazonapi_payment as pay, 
        bangazonapi_orderproduct as ordprod, bangazonapi_product as prod,
        auth_user as user
WHERE ord.payment_type_id = pay.id AND ord.id = ordprod.order_id
    AND ordprod.product_id = prod.id AND ord.customer_id = user.id
GROUP BY (ord.id);

SELECT ord.id as OrderId, SUM(prod.price) as OrderTotal, user.first_name || " " || user.last_name as FullName
FROM bangazonapi_order as ord, 
        bangazonapi_orderproduct as ordprod, bangazonapi_product as prod,
        auth_user as user
WHERE ord.payment_type_id IS NULL AND ord.id = ordprod.order_id AND ordprod.product_id = prod.id AND ord.customer_id = user.id
GROUP BY (ord.id);