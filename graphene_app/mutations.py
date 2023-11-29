import secrets

import graphene
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from graphene import Mutation, ID
from graphql_auth import mutations


class AuthMutation(graphene.ObjectType):
    verify_account = mutations.VerifyAccount.Field()