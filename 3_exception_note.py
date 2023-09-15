try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some notes')
    raise