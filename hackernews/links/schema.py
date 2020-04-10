from graphene import ObjectType, List, Int, String, Field, Mutation
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q

from .models import Link, Vote
from users.schema import UserType

class LinkType(DjangoObjectType):
    class Meta:
        model = Link

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class Query(ObjectType):
    links = List(LinkType, search=String())
    votes = List(VoteType)

    def resolve_links(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(url__icontains=search) |
                Q(description__icontains=search)
            )
            return Link.objects.filter(filter)

        return Link.objects.all()

    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()

class CreateLink(Mutation):
    id = Int()
    url = String()
    description = String()
    posted_by = Field(UserType)

    class Arguments:
        url = String()
        description = String()

    def mutate(self, info, url, description):
        user = info.context.user or None

        link = Link(
            url=url,
            description=description,
            posted_by=user
        )
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
            posted_by=link.posted_by,
        )

class CreateVote(Mutation):
    user = Field(UserType)
    link = Field(LinkType)

    class Arguments:
        link_id = Int()

    def mutate(self, info, link_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('You must be logged in to vote!')

        link = Link.objects.filter(id=link_id).first()
        if not link:
            raise Exception('Invalid link!')

        Vote.objects.create(
            user=user,
            link=link,
        )

        return CreateVote(user=user, link=link)


class Mutation(ObjectType):
    create_link = CreateLink.Field()
    create_vote = CreateVote.Field()
