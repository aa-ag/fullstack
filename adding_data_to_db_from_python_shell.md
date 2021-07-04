```
>>> from sqlalchemy import create_engine
>>> from sqlalchemy.orm import sessionmaker
>>> from dbsetup import Base, Restaurant, Menu
>>> engine = create_engine('sqlite:///restaurantmenu.db')
>>> Base.metadata.bind = engine
>>> DBSession = sessionmaker(bind = engine)
>>> session = DBSession()
>>> FirstRestaurant = Restaurant(name="Pizza Palace")
>>> session.add(FirstRestaurant)
>>> session.commit()
>>> session.query(Restaurant).all()
[<dbsetup.Restaurant object at 0x7f9205348100>]
>>> cheesepizza = Menu(name="Cheese Pizza", description = "All natural ingredient with mozzarella", course="Entree", price="$9.99", restaurant=FirstRestaurant)
>>> session.add(cheesepizza)
>>> session.query(Menu).all()
[<dbsetup.Menu object at 0x7f9208d96280>]
```