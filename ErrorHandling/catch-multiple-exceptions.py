# catch multiple exceptions
try:
  something.stupid()
except (TypeError, AttributeError) as e:
    print "failed, because:", e
    
