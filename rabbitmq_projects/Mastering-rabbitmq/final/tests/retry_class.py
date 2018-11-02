class Retry:
    def __init__(self, retries=3):
    
    # for demo, let's add a list to store the exceptions caught as well
      self.errors = []
      self.retries=retries
      self.attempts=0

    def __enter__(self):
      for _ in range(self.retries):
         try:
             return resource  # replace this with real code
         except Exception as e:
            self.attempts += 1
            self.errors.append(e)

# this needs to return True to suppress propagation, as others have said
    def __exit__(self, exc_type, exc_val, traceback):
       print 'Attempts', self.attempts
       for e in self.errors:
         print e  # as demo, print them out for good measure!
       return True


with Retry(retries=3) as resource:
    print("I got {}".format(resource))
