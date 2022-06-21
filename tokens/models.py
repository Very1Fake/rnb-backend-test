from django.db import models


# Model to store information about users tokens
class Token(models.Model):
    # Unique id in our database
    id = models.AutoField(primary_key=True)
    # Unique string generated in `tokens_create()` view
    unique_hash = models.TextField(max_length=20, unique=True)
    # Transaction id returned from web3
    tx_hash = models.TextField(unique=True)
    # URL of the token image
    media_url = models.URLField()
    # Eth address of the owner of the token
    owner = models.TextField()

    def __str__(self):
        return f"Token(id={self.id}, tx={self.tx_hash})"
