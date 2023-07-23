from exts import  db


"""

class Recipe
id:int primary_key
title:String
decription:str(text)
date_added



"""


class Recipe(db.Model):
   id = db.Column(db.Integer(),primary_key=True)
   title = db.Column(db.String(), nullable=False)
   description=db.Column(db.Text(), nullable=False)
   
   
   
   def __repr__(self):
       return f"<Recipe {self.title}>"
#method to return title



#methods to perform crud operations

def save(self):
    db.session.add(self)
    db.session.commit()
    
    
#deleting method  
def delete(self):
    db.session.delete(self)
    db.session.commit()
    
    
    
#updating message
def update(self,title,description):
    self.title=title
    self.description=description
    
   
        