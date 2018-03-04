# -*- coding: utf-8 -*-

#import string
#from datetime import datetime
#from uuid import uuid4
#from random import sample

dh.define_table('author',
                    Field('author_uuid', type='string',
                                        length=36,
                                        #default=uuid4(),
                                        required=True,
                                        requires=IS_NOT_EMPTY(),
                                        notnull=True,
                                        unique=True,
                                        label='Author ID',
                                        #comment=None,
                                        writable=False,
                                        readable=True,
                                        update=None),
                    Field('username', type='string',
                                        length=36,
                                        #default=None,
                                        required=True,
                                        requires=[IS_NOT_EMPTY(),
                                                    IS_EMAIL()],
                                        notnull=True,
                                        unique=True,
                                        label='Email Address',
                                        #comment=None,
                                        writable=True,
                                        readable=True,
                                        update=None),
                    Field('secret', type='string',
                                        length=8,
                                        #default=''.join(sample(string.ascii_lowercase + string.digits, 8)),
                                        required=True,
                                        requires=[IS_NOT_EMPTY(),
                                                    IS_ALPHANUMERIC()],
                                        notnull=True,
                                        unique=True,
                                        label='Secret',
                                        #comment=None,
                                        writable=False,
                                        readable=False,
                                        update=None),
                    Field('passphrase', type='password',
                                        length=80,
                                        default=None,
                                        required=True,
                                        requires=[IS_STRONG(),
                                                    CRYPT()],
                                        notnull=True,
                                        unique=False,
                                        label='Password',
                                        #comment=None,
                                        writable=True,
                                        readable=False,
                                        update=None),
                    Field('author_alias', type='string',
                                        length=20,
                                        #default=None,
                                        required=False,
                                        #requires=IS_NOT_EMPTY(),
                                        notnull=False,
                                        unique=True,
                                        label='Alias',
                                        #comment=None,
                                        writable=True,
                                        readable=True,
                                        update=None),
                    Field('active_state', type='integer',
                                        length=None,
                                        default=1,
                                        required=True,
                                        requires=IS_INT_IN_RANGE(-1, 2),
                                        notnull=True,
                                        unique=False,
                                        label='Status',
                                        comment='-1:Blacklisted; 0:Inactive; 1:Active;',
                                        writable=True,
                                        readable=True,
                                        update=None),
                    Field('remarks', type='string',
                                        length=255,
                                        default=None,
                                        required=False,
                                        requires=IS_ALPHANUMERIC(),
                                        notnull=False,
                                        unique=False,
                                        label='Remarks',
                                        #comment=None,
                                        writable=True,
                                        readable=True,
                                        update=None),
                    Field('cdate', type='datetime',
                                        length=None,
                                        #default=datetime.utcnow(),
                                        required=True,
                                        requires=IS_NOT_EMPTY(),
                                        notnull=True,
                                        unique=False,
                                        label='Create Date',
                                        #comment=None,
                                        writable=False,
                                        readable=True,
                                        update=None),
                    Field('mdate', type='datetime',
                                        length=None,
                                        #default=datetime.utcnow(),
                                        required=True,
                                        requires=IS_NOT_EMPTY(),
                                        notnull=True,
                                        unique=False,
                                        label='Last Modified',
                                        #comment=None,
                                        writable=False,
                                        readable=False,
                                        #update=datetime.utcnow()),
                                        ),
                    Field('is_deleted', type='boolean',
                                        length=None,
                                        default=False,
                                        required=False,
                                        #requires=IS_NOT_EMPTY(),
                                        notnull=False,
                                        unique=False,
                                        #label='Deleted',
                                        #comment=None,
                                        writable=False,
                                        readable=False,
                                        update=None),
                    migrate=True)

dh.author.username.requires=IS_NOT_IN_DB(dh, 'author.username')


