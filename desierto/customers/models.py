from django.db import models

class DocumentType(models.Model):
    """
    Represent a document type
    Atributes:
        code: The code of the document type
        name: The name of the document type
    """

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'document_type'
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documentos'

class Customer(models.Model):
    """
    Represent a customer
    Atributes:
        doc_type: The document type of the customer
        doc_number: The document number of the customer
        first_name: The first name of the customer
        last_name: The last name of the customer
        email: The email of the customer
        phone: The phone number of the customer
        created_at: The date of creation of the customer

  
    """

    doc_type = models.ForeignKey(DocumentType, on_delete=models.PROTECT)
    doc_number = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'customer'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Purchase(models.Model):
    """
      Represent a purchase
      Atributes:
          client: The client of the purchase
          amount: The amount of the purchase
          date: The date of the purchase
          description: The description of the purchase

    """
    
    
    client = models.ForeignKey(Customer, related_name="purchases", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.client} - {self.amount}'
    class Meta:
        db_table = 'purchase'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'