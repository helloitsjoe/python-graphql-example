from graphene import ObjectType, Schema
import graphql_jwt
import json

import users.schema
import links.schema
import links.schema_relay


class Query(
    users.schema.Query, links.schema.Query, links.schema_relay.RelayQuery, ObjectType
):
    pass


class Mutation(
    users.schema.Mutation,
    links.schema.Mutation,
    links.schema_relay.RelayMutation,
    ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = Schema(query=Query, mutation=Mutation)

# TEST:

# result = schema.execute(
#     '''
#     { links { description votes { user { username } } } }
#     '''
# )

# if result and result.errors:
#     print('Errors', json.dumps(result.errors[0].message, indent=2))

# print('Data', json.dumps(result.data, indent=2))

# QUERIES FROM PLAYGROUND:

# query {
#   links(first: 5) {
#     description
#     url
#     votes {
#       user {
#         username
#       }
#     }
#     postedBy{
#       username
#     }
#   }
# }

# query {
#   me {
#     username
#   }
# }

# mutation {
#   createVote(linkId: 5) {
#     link {
#       description
#       votes {
#         user {
#           username
#         }
#       }
#     }
#   }
# }

# mutation {
#   tokenAuth(username:"flyntflossy69", password:"poopybutt") {
#     token
#   }
# }

# mutation {
#   verifyToken(token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3Rlcm9vbmkiLCJleHAiOjE1ODY2MDM0ODIsIm9yaWdfaWF0IjoxNTg2NjAzMTgyfQ.3WoiYRUwXEOS0FYAwc4Gruh2Bu1UA0Ij0X42xgpWTuc") {
#     payload
#   }
# }


# mutation {
#   createUser(email:"A@b.com", username:"testerooni", password:"lalala") {
#     user {
#       username
#       id
#     }
#   }
# }

# query {
# 	# relayLinks(first: 1, after: "YXJyYXljb25uZWN0aW9uOjE=") {
#   relayLinks {
#     pageInfo{
#       startCursor
#       endCursor
#       hasNextPage
#     }
#     edges {
#       node {
#         url
#         description
#         votes {
#           edges {
#             node {
#               user {
#                 id
#                 username
#               }
#             }
#           }
#         }
#       }
#     }
#   }
# }

# mutation {
#   relayCreateLink(input:
#     {url: "foo.fartz", description: "Fartz for Foos"}
#   ) {
#     link {
#       id
#       postedBy {
#         username
#       }
#     }
#   }
# }
