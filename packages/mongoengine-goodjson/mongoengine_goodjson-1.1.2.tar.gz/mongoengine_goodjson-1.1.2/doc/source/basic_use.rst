Basic Use
=========

Document Inheritance
---------------------
First of all, let's see the usual ODM:

.. code:: python

  import mongoengine as db


  class Address(db.EmbeddedDocument):
    """Address schema."""

    street = db.StringField()
    city = db.StringField()
    state = db.StringField()


  class User(db.Document):
    """User data schema."""

    name = db.StringField()
    email = db.EmailField()
    address = db.EmbeddedDocumentListField(Address)

As you can see the code, this code has nothing special. And, when you
serialize the instance into JSON, you will get:

.. code:: json

  {
    "id": { "$oid": "5700c32a1cbd5856815051ce" },
    "name": "Example Man",
    "email": "test@example.com",
    "address": [
      {
        "street": "Hello Street",
        "city": "Hello City",
        "state": "Hello State"
      }, {
        "street": "World Street",
        "city": "World City",
        "state": "World State"
      }
    ]
  }

And yes, we want to replace :code:`$oid` object with :code:`str` that shows
:code:`5700c32a1cbd5856815051ce`. MongoEngine enables to you do it very easily.
Let's just inherit :code:`mongoengine_goodjson.Document` like this:

.. code:: python

  import mongoengine_goodjson as gj
  import mongoengine as db


  class Address(gj.EmbeddedDocument):
      """Address schema."""

      street = db.StringField()
      city = db.StringField()
      state = db.StringField()


  class User(gj.Document):
      """User data schema."""

      name = db.StringField()
      email = db.EmailField()
      address = db.EmbeddedDocumentListField(Address)


Then, running :code:`user.to_json` (:code:`user` is the instance object of User),
you will get the JSON code like this:

.. code:: json

  {
    "id": "5700c32a1cbd5856815051ce",
    "name": "Example Man",
    "email": "test@example.com",
    "address": [
      {
        "street": "Hello Street",
        "city": "Hello City",
        "state": "Hello State"
      }, {
        "street": "World Street",
        "city": "World City",
        "state": "World State"
      }
    ]
  }

Follow Reference
----------------
Let's see ODM using :code:`ReferenceField`.

.. code:: python

  import mongoengine as db
  import mongoengine_goodjson as gj


  class Book(gj.Document):
    """Book information model."""

    name = db.StringField(required=True)
    isbn = db.StringField(required=True)
    author = db.StringField(required=True)
    publisher = db.StringField(required=True)
    publish_date = db.DateTimeField(required=True)


  class User(gj.Document):
    firstname = db.StringField(required=True)
    lastname = db.StringField(required=True)
    books_bought = db.ListField(db.ReferenceField(Book))
    favorite_one = db.ReferenceField(Book)


And here is the JSON data:

.. code:: json

  {
    "id": "570ee9d1fec55e755db82129",
    "firstname": "James",
    "lastname": "Smith",
    "books_bought": [
      "570eea0afec55e755db8212a",
      "570eea0bfec55e755db8212b",
      "570eea0bfec55e755db8212c"
    ],
    "favorite_one": "570eea0bfec55e755db8212b"
  }

This seems to be good deal for :code:`Reference Field`, but sometimes you might
want to generate the Document with Referenced Document like Embedded Document
like this:

.. code:: json

  {
    "id": "570ee9d1fec55e755db82129",
    "firstname": "James",
    "lastname": "Smith",
    "books_bought": [
      {
        "id": "570eea0afec55e755db8212a",
        "name": "ドグラ・マグラ (上)",
        "author": "夢野 久作",
        "publisher": "角川文庫",
        "publish_date": "1976-10-01",
        "isbn": "978-4041366035"
      },
      {
        "id": "570eea0bfec55e755db8212b",
        "name": "ドグラ・マグラ (下)",
        "author": "夢野 久作",
        "publisher": "角川文庫",
        "publish_date": "1976-10-01",
        "isbn": "978-4041366042"
      },
      {
        "id": "570eea0bfec55e755db8212c",
        "name": "The Voynich Manuscript: Full Color Photographic Edition",
        "author": "Unknown",
        "publisher": "FQ Publishing",
        "publish_date": "2015-01-17",
        "isbn": "978-1599865553"
      }
    ],
    "favorite_one": {
      "id": "570eea0bfec55e755db8212b",
      "name": "ドグラ・マグラ (下)",
      "author": "夢野 久作",
      "publisher": "角川文庫",
      "publish_date": "1976-10-01",
      "isbn": "978-4041366042"
    }
  }

Of course, you can generate the json document by calling :code:`to_json()`
many times like this:

.. code:: python

  def output_references():
    user = User.objects(pk=ObjectId("570ee9d1fec55e755db82129")).get()
    user_dct = json.loads(user.to_json())
    user_dct["books"] = [
      json.loads(book.to_json()) for book in user.books_bought
    ]
    user_dct["favorite_one"] = json.loads(user.favorite_one.to_json())
    return jsonify(user_dct)
    # ...And what if there are references in the referenced document??

However, as you can see, that code is messy and it has a problem that causes
code-bloat. To avoid the problem, this script has a function called
:code:`Follow Reference` since version 0.9. To use it, you can just pass
:code:`follow_reference=True` to :code:`to_json` function like this:

.. code:: python

  def output_references():
    user = User.objects(pk=ObjectId("570ee9d1fec55e755db82129")).get()
    return jsonify(json.loads(user.to_json(follow_reference=True)))

Note that setting :code:`follow_reference=True`, :code:`Document.to_json`
checks the reference recursively until the depth reaches 3rd depth. To change
the maximum recursion depth, you can set the value you want to :code:`max_depth`:

.. code:: python

  def output_references():
    user = User.objects(pk=ObjectId("570ee9d1fec55e755db82129")).get()
    return jsonify(json.loads(user.to_json(follow_reference=True, max_depth=5)))
