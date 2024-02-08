86% of storage used … If you run out, you won't have enough storage to create, edit, and upload files. Get 100 GB of storage for ₦950.00 ₦240.00/month for 3 months.
#!/usr/bin/python3
"""This module creates a Place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class for managing place objects"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
