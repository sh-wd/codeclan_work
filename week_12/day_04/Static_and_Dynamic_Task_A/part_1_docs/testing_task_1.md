### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):  #self does not need to be passed as a parameter to any of the methods
    if card.value = 1:            #'=' should be '=='
      return True 
    else                          #missing ':'
      return False
   

  dif highest_card(self, card1 card2): #def misspelled and comma missing between parameters
  if card1.value > card2.value:        #should have indentation for this and all following lines
    return card                        #variable name should be card1
  else:
    return card2
  


def cards_total(self, cards):             #incorrect indentation
  total                                   #total variable should be set at 0 to begin
  for card in cards:
    total += card.value
    return "You have a total of" + total  #incorrect indentation and variable total needs to be converted
                                          #to a string
  
```
