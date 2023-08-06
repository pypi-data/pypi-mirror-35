# webcraft

Async python framework for creating beautiful REST APIs using `aiohttp`.

## How to use it

```py
from aiohttp import web
# SQLAlchemy core imports
from sqlalchemy import (
    Table, Text, MetaData, String, Integer, Column, Boolean,
    DateTime
)
# Marshmallow to define and validate schema
from marshmallow import Schema, fields

# To get nice working OpenAPI (Swagger) UI
from aiohttp_apispec import docs, use_kwargs, marshal_with
from webcraft import ItemView, ListView

# Now lets define database
message = Table(
    'message', meta,
    Column('id', Integer(), primary_key=True),
    Column('created_at', DateTime(), nullable=True),
    Column('to_user', String(), index=True, nullable=False),
    Column('from_user', String(), index=True, nullable=False),
    Column('text', Text(), nullable=True),
    Column('is_sent', Boolean(), nullable=True),
)

# Then define Schema 
class MessageSchema(Schema):
    from_user = fields.Str()
    to_user = fields.Str()
    text = fields.Raw()
    is_sent = fields.Bool()


class MessageItemSchema(MessageSchema):
    id = fields.Int()
    created_at = fields.DateTime()


# And class based views

class MessageListView(ListView):
    model = message

    @docs(
        tags=['Messages'],
        summary='List messages',
        description='List all messages',
    )
    @marshal_with(schema.MessageItemSchema(many=True), 200)
    async def get(self):
        return await super().get()


class MessageItemView(ItemView):
    model = message
    match_name = 'message_id'

    @docs(
        tags=['Messages'],
        summary='Get one message item',
        description='Get full message information',
    )
    @marshal_with(schema.MessageSchema(), 200)
    @marshal_with(schema.ErrorSchema(), 404)
    async def get(self):
        return await super().get()

class SendView(web.View):
    @docs(
        tags=['Messenger'],
        summary='Process messenger actions ',
        description='Send message to user',
    )
    @marshal_with(MessageSchema(many=True), 200)
    async def post(self):
        await sendmessage(
            to="m@xen.ru",
            subject="Test",
            template="envelope.html",
            request=self.request,
            context={}
        )
        return web.json_response(
            {'msg': 'Done',
             #  'data': {'id': item[self.table_id]}
             }
        )

async def hello(request):
    return web.Response(text="Hello, world")

app = web.Application()
app.add_routes([web.get('/', hello)])

# messages API
app.router.add_view('/api/messages', MessageListView)
app.router.add_view(
    '/api/messages/{message_id:\d+}', MessageItemView)

# process API
app.router.add_view('/api/send', SendView)



```