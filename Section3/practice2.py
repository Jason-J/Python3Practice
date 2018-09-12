class Property:
    def __init__(self, square_feets = '', beds = '', baths = '', **kwargs):
        super(object, self).__init__(**kwargs)
        self.square_feets = square_feets
        self.num_bedrooms = beds
        self.num.baths = baths

    def display(self):
        print ('PROPERTY  DETALLS')
        print ('=================')
        print ()
