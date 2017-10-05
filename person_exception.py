class Person(object):
    def __init__(self, first_name=None, last_name=None):
        if None in [first_name, last_name]:
            raise Exception('Both first & last name must have values')
        self.first_name = first_name
        self.last_name = last_name
        print('Initialize')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


try:
    p = Person(first_name='Colby', last_name='Gatte')
    print(p)
except Exception as e:
    print(e)