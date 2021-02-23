def cities_to_use_1():
    return ['amsterdam', 
            'antwerp', 
            'asheville', 
            'athens', 
            'austin', 
            'bangkok', 
            'barcelona', 
            'barossa valley',
            'barwon south west', 
            'beijing', 
            'belize', 
            'bergamo', 
            'berlin', 
            'bologna', 
            'bordeaux', 
            'boston', 
            'bristol', 
            'broward county', 
            'brussels', 
            'buenos aires'
            'shanghai']

def cities_to_use_2():
    return ['amsterdam', 
            'antwerp', 
            'asheville', 
            'athens', 
            'austin', 
            'bangkok', 
            'barcelona', 
            'barossa valley',
            'barwon south west', 
            'beijing', 
            'belize', 
            'bergamo', 
            'berlin', 
            'bologna', 
            'bordeaux', 
            'boston', 
            'bristol', 
            'broward county', 
            'brussels', 
            'buenos aires', 
            'cambridge MA', 
            'cape town',
            'chicago',
            'clark county',
            'sevilla', 
            'copenhagen', 
            'denver', 
            'dublin', 
            'edinburgh', 
            'euskadi',
            'shanghai']

def columns_to_use():
    return ['host_id', 
            'host_response_rate', 
            'host_acceptance_rate', 
            'latitude', 
            'longitude', 
            'accommodates', 
            'price', 
            'number_of_reviews', 
            'reviews_per_month', 
            'neighbourhood_cleansed',
            'host_response_time', 
            'host_is_superhost', 
            'host_total_listings_count', 
            'host_has_profile_pic',
            'host_identity_verified', 
            'property_type',
            'room_type', 
            'bathrooms', 
            'bedrooms', 
            'beds',  
            'number_of_reviews_ltm', 
            'minimum_nights', 
            'maximum_nights', 
            'availability_30', 
            'availability_90', 
            'availability_365',
            'review_scores_rating', 
            'review_scores_accuracy', 
            'review_scores_cleanliness', 
            'review_scores_checkin', 
            'review_scores_communication', 
            'review_scores_location', 
            'review_scores_value',
            'instant_bookable']

# Columnas comentadas se han retirado por empeorar el resultado
def columns_to_fit():
    return [ 
#            'host_id', 
#            'host_response_rate', 
#            'host_acceptance_rate', 
#            'northing', 
#            'easting', 
            'accommodates', 
#            'number_of_reviews', 
            'reviews_per_month', 
            'neighbourhood_cleansed',
            'host_response_time', 
            'host_is_superhost', 
#            'host_total_listings_count', 
            'host_has_profile_pic',
            'host_identity_verified',
            'property_type',
            'room_type', 
            'bathrooms', 
            'bedrooms', 
            'beds', 
            'minimum_nights', 
#            'maximum_nights', 
            'availability_30', 
            'availability_90', 
#            'availability_365',
            'number_of_reviews_ltm',
            'review_scores_rating', 
            'review_scores_accuracy', 
            'review_scores_cleanliness', 
            'review_scores_checkin', 
            'review_scores_communication', 
            'review_scores_location', 
            'review_scores_value', 
            'instant_bookable']
