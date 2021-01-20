# for making exception just make subclass of Exception
class isMajor(Exception):
   pass
 
def check(age):
   if int(age) < 18:
       raise isMajor
   else:
       print('Age: '+str(age))
 
#don't raise
check(23) 
#raises an Exception
check(17)