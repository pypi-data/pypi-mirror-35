#!/usr/bin/env python
from google.protobuf.empty_pb2 import Empty
import grpc

from kama.acl import DEFAULT_ACLS
from kama import kama_pb2
from kama import kama_pb2_grpc
import kama.env
import kama.log

import collections
import argparse


log = kama.log.get_logger('kama.client')


KamaClientConfig = collections.namedtuple('KamaConfig', 'server ca_cert client_key client_cert')


DEFAULT_CONFIG = KamaClientConfig(
        server='127.0.0.1:8443',
        ca_cert='ca-cert.pem',
        client_key='client.key',
        client_cert='client.cert')


ENV_CONFIG = KamaClientConfig(
        server=kama.env.get(['KAMA_SERVER'], DEFAULT_CONFIG.server),
        ca_cert=kama.env.get(['KAMA_CA_CERT'], DEFAULT_CONFIG.ca_cert),
        client_key=kama.env.get(['KAMA_CLIENT_KEY'], DEFAULT_CONFIG.client_key),
        client_cert=kama.env.get(['KAMA_CLIENT_CERT'], DEFAULT_CONFIG.client_cert))


class KamaDatabaseClient(object):
    '''
    This is a thin wrapper around the raw GRPC protobuf interface to Kama
    '''
    def __init__(self, args):
        log.debug(args)
        if args.ca_cert is not None:
            root_pem = open(args.ca_cert, 'r').read()
            client_private_pem = open(args.client_key, 'r').read()
            client_public_pem = open(args.client_cert, 'r').read()

            creds = grpc.ssl_channel_credentials(root_pem, client_private_pem, client_public_pem)
            channel = grpc.secure_channel(args.server, creds)
        else:
            log.warning('Connecting database client over insecure channel')
            channel = grpc.insecure_channel(args.server)
        
        self.stub = kama_pb2_grpc.KamaDatabaseStub(channel)

    def list_entities(self, kind=None):
        '''
        Returns an iterable of Entities, optionally filtered by kind.
        '''
        query = kama_pb2.Entity()
        if kind:
            query.kind = kind
        return self.stub.ListEntities(query)

    def get_entity(self, kind, name):
        '''
        Queries kama for an Entity with the given kind and name

        Required permissions:
            entity.read_attribute
            entity.read_link
            entity.read_permission
        '''
        entity = kama_pb2.Entity()
        entity.kind = kind
        entity.name = name
        return self.stub.GetEntity(entity)
    
    def get_entity_by_uuid(self, uuid):
        '''
        Queries kama for an Entity with the given UUID

        Required permissions:
            entity.read_attribute
            entity.read_link
            entity.read_permission
        '''
        entity = kama_pb2.Entity()
        entity.uuid = uuid
        return self.stub.GetEntity(entity)

    def create_entity(self, kind, name, owner_role_name):
        '''
        Create a new Entity.
        
        `owner_role_name` must be the name of an existing Entity with the kind
        `role` that has a link to your user Entity. If you're working from a
        newly initialized database, the `root` role and user are guaranteed to
        exist.

        You must be a member of the owner role in order to create new Entities
        owned by it.

        Required permissions (on the owner role):
            entity.read_attribute
            entity.read_link
            entity.read_permission
            entity.add_link
        '''
        request = kama_pb2.CreateEntityRequest()
        request.entity.kind = kind
        request.entity.name = name

        owner_role = self.get_entity('role', owner_role_name)
        request.owner_role.uuid = owner_role.uuid
        return self.stub.CreateEntity(request)
    
    def delete_entity(self, uuid):
        '''
        Delete an Entity

        Required permissions:
            entity.delete
        '''
        entity = kama_pb2.Entity()
        entity.uuid = uuid
        return self.stub.DeleteEntity(entity)

    def update_entity(self, uuid, name):
        '''
        Rename an existing Entity

        Required permissions:
            entity.set_name
        '''
        entity = kama_pb2.Entity()
        entity.uuid = uuid
        entity.name = name
        new_entity = self.stub.UpdateEntity(entity)
        return new_entity

    def add_attribute(self, entity_uuid, key, value):
        '''
        Add an attribute to the Entity with the given UUID

        Required permissions:
            entity.add_attribute
        '''
        attribute = kama_pb2.Attribute()
        attribute.entity.uuid = entity_uuid
        attribute.key = key
        attribute.value = value
        return self.stub.AddAttribute(attribute)

    def delete_attributes(self, entity_uuid, key):
        '''
        Delete all attributes with the given key from an Entity

        Required permissions:
            entity.delete_attribute
        '''
        attribute = kama_pb2.Attribute()
        attribute.entity.uuid = entity_uuid
        attribute.key = key
        return self.stub.DeleteAttributes(attribute)

    def add_link(self, from_uuid, to_uuid):
        '''
        Add a link from an Entity to another Entity

        Required permissions:
            entity.add_link
        '''
        link = kama_pb2.Link()
        link.from_entity.uuid = from_uuid
        link.to_entity.uuid = to_uuid
        return self.stub.AddLink(link)

    def delete_link(self, from_uuid, to_uuid):
        '''
        Delete a link from an Entity to another Entity

        Required permissions:
            entity.delete_link
        '''
        link = kama_pb2.Link()
        link.from_entity.uuid = from_uuid
        link.to_entity.uuid = to_uuid
        return self.stub.DeleteLink(link)

    def add_permission(self, entity_uuid, role_uuid, name):
        '''
        Add a permission for all members of a role on an Entity

        Required permissions:
            entity.add_permission
        '''
        permission = kama_pb2.Permission()
        permission.entity.uuid = entity_uuid
        permission.role.uuid = role_uuid
        permission.name = name
        return self.stub.AddPermission(permission)

    def delete_permission(self, entity_uuid, role_uuid, name):
        '''
        Delete a permission from a role

        Required permissions:
            entity.delete_permission
        '''
        permission = kama_pb2.Permission()
        permission.entity.uuid = entity_uuid
        permission.role.uuid = role_uuid
        permission.name = name
        return self.stub.DeletePermission(permission)

    def pb_to_human(self, entity):
        '''
        Format an Entity protobuf object into a human readable string
        '''
        out = '''name:    {entity.name}
kind:    {entity.kind}
uuid:    {entity.uuid}
attributes:\n'''.format(entity=entity)

        for attribute in entity.attributes:
            out += '    {attribute.key} = {attribute.value}\n'.format(attribute=attribute)

        out += 'links:\n'
        for link in entity.links_from:
            out += '    -> %s %s\n' % (link.to_entity.kind, link.to_entity.name)

        for link in entity.links_to:
            out += '    <- %s %s\n' % (link.from_entity.kind, link.from_entity.name)

        out += 'permissions:\n'
        for permission in entity.permissions:
            out += '    %s %s\n' % (permission.role.name, permission.name)

        return out


def list_entities(args):
    client = KamaDatabaseClient(args)
    for entity in client.list_entities(kind=args.kind):
        print('%s %s' % (entity.kind, entity.name))

def get_entity(args):
    client = KamaDatabaseClient(args)
    print(client.pb_to_human(client.get_entity(args.kind, args.name)))

def create_entity(args):
    client = KamaDatabaseClient(args)
    entity = client.create_entity(args.kind, args.name, args.owner_role)
    print(client.pb_to_human(entity))

def delete_entity(args):
    client = KamaDatabaseClient(args)
    entity = client.get_entity(args.kind, args.name)
    client.delete_entity(entity.uuid)

def rename_entity(args):
    client = KamaDatabaseClient(args)
    entity = client.get_entity(args.kind, args.old_name)
    entity = client.update_entity(entity.uuid, args.new_name)
    print(client.pb_to_human(entity))


def attribute_add(args):
    client = KamaDatabaseClient(args)
    entity = client.get_entity(args.entity_kind, args.entity_name)
    client.add_attribute(entity.uuid, args.key, args.value)

def attribute_delete(args):
    client = KamaDatabaseClient(args)
    entity = client.get_entity(args.entity_kind, args.entity_name)
    client.delete_attributes(entity.uuid, args.key)

def attribute_list(args):
    client = KamaDatabaseClient(args)
    entity = client.get_entity(args.entity_kind, args.entity_name)

    if args.key is not None:
        attributes = [x for x in entity.attributes if x.key == args.key]
    else:
        attributes = entity.attributes

    for attribute in attributes:
        print('%s=%s' % (attribute.key, attribute.value.encode('utf-8')))


def link_add(args):
    client = KamaDatabaseClient(args)
    from_entity = client.get_entity(args.entity_from_kind, args.entity_from_name)
    to_entity = client.get_entity(args.entity_to_kind, args.entity_to_name)
    client.add_link(from_entity.uuid, to_entity.uuid)

def link_delete(args):
    client = KamaDatabaseClient(args)
    from_entity = client.get_entity(args.entity_from_kind, args.entity_from_name)
    to_entity = client.get_entity(args.entity_to_kind, args.entity_to_name)
    client.delete_link(from_entity.uuid, to_entity.uuid)


def _traverse_links(client, entity, parents=False, children=False, recursive=False, seen=None):
    results = []

    if seen is None:
        seen = set()

    if entity.uuid in seen:
        # Loop detected, short circuit
        return []

    seen.add(entity.uuid)

    if parents:
        results += [client.get_entity_by_uuid(x.from_entity.uuid) for x in entity.links_to]

    if children:
        results += [client.get_entity_by_uuid(x.to_entity.uuid) for x in entity.links_from]

    if recursive:
        for result in list(results):
            result = client.get_entity_by_uuid(result.uuid)
            results += _traverse_links(client, result, parents, children, recursive, seen)

    return results

def link_get(args):
    client = KamaDatabaseClient(args)
    entity = client.get_entity(args.entity_kind, args.entity_name)

    for result in _traverse_links(client, entity, args.parents, args.children, args.recursive):
        print('%s %s' % (result.kind, result.name))


def permission_add(args):
    client = KamaDatabaseClient(args)
    entity = client.get_entity(args.entity_kind, args.entity_name)
    role = client.get_entity('role', args.role_name)

    if args.permission_name.startswith('acl:'):
        permissions = DEFAULT_ACLS[args.permission_name.split(':', 1)[1]]
    else:
        permissions = [args.permission_name]

    for permission in permissions:
        client.add_permission(entity.uuid, role.uuid, permission)

def permission_delete(args):
    client = KamaDatabaseClient(args)
    entity = client.get_entity(args.entity_kind, args.entity_name)
    role = client.get_entity('role', args.role_name)

    if args.permission_name.startswith('acl:'):
        permissions = DEFAULT_ACLS[args.permission_name.split(':', 1)[1]]
    else:
        permissions = [args.permission_name]

    for permission in permissions:
        client.delete_permission(entity.uuid, role.uuid, permission)


def setup_arguments(parser):
    parser.add_argument('--server', default=ENV_CONFIG.server)
    parser.add_argument('--ca-cert', default=ENV_CONFIG.ca_cert)
    parser.add_argument('--client-key', default=ENV_CONFIG.client_key)
    parser.add_argument('--client-cert', default=ENV_CONFIG.client_cert)
    sp = parser.add_subparsers()

    # kama dbclient entity ...
    entity_parser = sp.add_parser('entity')
    subparsers = entity_parser.add_subparsers()

    parser_entity_list = subparsers.add_parser('list')
    parser_entity_list.add_argument('--kind', default=None)
    parser_entity_list.set_defaults(func=list_entities)

    parser_entity_get = subparsers.add_parser('get')
    parser_entity_get.add_argument('kind')
    parser_entity_get.add_argument('name')
    parser_entity_get.set_defaults(func=get_entity)

    parser_entity_create = subparsers.add_parser('create')
    parser_entity_create.add_argument('kind')
    parser_entity_create.add_argument('name')
    parser_entity_create.add_argument('owner_role')
    parser_entity_create.set_defaults(func=create_entity)

    parser_entity_delete = subparsers.add_parser('delete')
    parser_entity_delete.add_argument('kind')
    parser_entity_delete.add_argument('name')
    parser_entity_delete.set_defaults(func=delete_entity)
    
    parser_entity_rename = subparsers.add_parser('rename')
    parser_entity_rename.add_argument('kind')
    parser_entity_rename.add_argument('old_name')
    parser_entity_rename.add_argument('new_name')
    parser_entity_rename.set_defaults(func=rename_entity)

    # kama dbclient attribute ...
    attribute_parser = sp.add_parser('attribute')
    subparsers = attribute_parser.add_subparsers()

    parser_attribute_add = subparsers.add_parser('add')
    parser_attribute_add.add_argument('entity_kind')
    parser_attribute_add.add_argument('entity_name')
    parser_attribute_add.add_argument('key')
    parser_attribute_add.add_argument('value')
    parser_attribute_add.set_defaults(func=attribute_add)

    parser_attribute_delete = subparsers.add_parser('delete')
    parser_attribute_delete.add_argument('entity_kind')
    parser_attribute_delete.add_argument('entity_name')
    parser_attribute_delete.add_argument('key')
    parser_attribute_delete.set_defaults(func=attribute_delete)

    parser_attribute_list = subparsers.add_parser('list')
    parser_attribute_list.add_argument('entity_kind')
    parser_attribute_list.add_argument('entity_name')
    parser_attribute_list.add_argument('--key', action='store', default=None)
    parser_attribute_list.set_defaults(func=attribute_list)

    # kama dbclient link ...
    link_parser = sp.add_parser('link')
    subparsers = link_parser.add_subparsers()
    parser_link_add = subparsers.add_parser('add')
    parser_link_add.add_argument('entity_from_kind')
    parser_link_add.add_argument('entity_from_name')
    parser_link_add.add_argument('entity_to_kind')
    parser_link_add.add_argument('entity_to_name')
    parser_link_add.set_defaults(func=link_add)

    parser_link_delete = subparsers.add_parser('delete')
    parser_link_delete.add_argument('entity_from_kind')
    parser_link_delete.add_argument('entity_from_name')
    parser_link_delete.add_argument('entity_to_kind')
    parser_link_delete.add_argument('entity_to_name')
    parser_link_delete.set_defaults(func=link_delete)

    parser_link_get = subparsers.add_parser('get')
    parser_link_get.add_argument('entity_kind')
    parser_link_get.add_argument('entity_name')
    parser_link_get.add_argument('--parents', action='store_true',
            help='List entities that link to this entity')
    parser_link_get.add_argument('--children', action='store_true',
            help='List entities that this entity links to')
    parser_link_get.add_argument('--recursive', action='store_true',
            help='Recursively traverse parents or children if either of those options is set')
    parser_link_get.set_defaults(func=link_get)

    # kama dbclient permission ...
    permission_parser = sp.add_parser('permission')
    subparsers = permission_parser.add_subparsers()
    parser_permission_add = subparsers.add_parser('add')
    parser_permission_add.add_argument('entity_kind')
    parser_permission_add.add_argument('entity_name')
    parser_permission_add.add_argument('role_name')
    parser_permission_add.add_argument('permission_name')
    parser_permission_add.set_defaults(func=permission_add)

    parser_permission_delete = subparsers.add_parser('delete')
    parser_permission_delete.add_argument('entity_kind')
    parser_permission_delete.add_argument('entity_name')
    parser_permission_delete.add_argument('role_name')
    parser_permission_delete.add_argument('permission_name')
    parser_permission_delete.set_defaults(func=permission_delete)


def connect(server=None, ca_cert=None, client_key=None, client_cert=None):
    '''
    Use this method to get an instantiated KamaDatabaseClient instance for use
    in other scripts
    '''
    if server is None:
        server = ENV_CONFIG.server
    if ca_cert is None:
        ca_cert = ENV_CONFIG.ca_cert
    if client_key is None:
        client_key = ENV_CONFIG.client_key
    if client_cert is None:
        client_cert = ENV_CONFIG.client_cert

    config = KamaClientConfig(server, ca_cert, client_key, client_cert)
    return KamaDatabaseClient(config)


def main():
    parser = argparse.ArgumentParser()
    setup_arguments(parser)
    
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
