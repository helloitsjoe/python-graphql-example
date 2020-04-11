from graphene import ObjectType, Schema
import graphql_jwt
import json

import links.schema
import users.schema


class Query(users.schema.Query, links.schema.Query, ObjectType):
    pass

class Mutation(users.schema.Mutation, links.schema.Mutation, ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = Schema(query=Query, mutation=Mutation)

result = schema.execute(
    '''
    { links { description votes { user { username } } } }
    '''
)

if result and result.errors:
    print('Errors', json.dumps(result.errors[0].message, indent=2))

print('Data', json.dumps(result.data, indent=2))

