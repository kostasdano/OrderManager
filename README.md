# OrderManager

OrderManager is a simple organiser for Customers, Products and Orders. The SuperUser can add Orders between Customers and Products
while every Customer has Discount Coupons

# Apps

### Customers

* **customers/models.py:** contains CustomerModel and CouponModel with all the basic fields (for more info see code)

* **customers/views.py:** contains all the views for Customer and Coupon models. CreateViews, ListViews, UpdateViews and
DeleteViews for both models. ListView for CouponModel not implemented, included in CustomerProducts View. Activation/DeactivationViews included

* **customers/urls.py:** contains all the urls for Customer and Coupon models (for more info see code)

* **customers/templates:** contains all the templates for Customer and Coupon models. CreateFormTemplates, DetailsTemplates (Customer Profile), CustomerListTemplates, UpdateFormTemplates and DeletionOptionsTemplate (Deletion or Deactivation Confirmation)


### Products

* **products/models.py:** contains ProductModel with all the basic fields (for more info see code)

* **products/views.py:** contains all the views for Product Model. CreateViews, ListViews, UpdateViews and
DeleteViews for Product Model. Activation/DeactivationViews included

* **products/urls.py:** contains all the urls for Product Model (for more info see code)

* **products/templates:** contains all the templates for Product Model. CreateFormTemplates, DetailsTemplates (Product Info), ProductsListTemplates, UpdateFormTemplates and DeletionOptionsTemplate (Deletion or Deactivation Confirmation)


### Orders

* **orders/models.py:** contains OrderModel with all the basic fields (for more info see code)

* **orders/views.py:** contains all the views for Order Model. CreateViews, ListViews, UpdateViews and
DeleteViews for Product Model. Activation/DeactivationViews included

* **orders/urls.py:** contains all the urls for Order Model (for more info see code)

* **orders/templates:** contains all the templates for Order Model. CreateFormTemplates, DetailsTemplates (Order Details), OrdersListTemplates, UpdateFormTemplates and DeletionOptionsTemplate (Deletion or Deactivation Confirmation)


# Deployment
Deployed in Heroku - 
[(Click Here)](https://kostasdano-ordermanager.herokuapp.com/)

# Authors

* **Konstantinos Danochristos** - [Github](https://github.com/kostasdano)

