# -*- coding: utf-8 -*-

dh.define_table('content_code',
                    Field('language', type='string',
                                        length=16,
                                        default=None,
                                        required=True,
                                        requires=[IS_NOT_EMPTY(),
                                                    IS_IN_SET('C#',
                                                                'JavaScript',
                                                                'Python',
                                                                'Java',
                                                                'SQL')],
                                        notnull=True,
                                        unique=False,
                                        label='Language',
                                        #comment=None,
                                        writable=True,
                                        readable=True,
                                        update=None),
                    Field('snippet', type='text',
                                        length=8000,
                                        default=None,
                                        required=True,
                                        requires=IS_NOT_EMPTY(),
                                        notnull=True,
                                        unique=False,
                                        label='Snippet',
                                        #comment=None,
                                        writable=True,
                                        readable=True,
                                        update=None),
                    migrate=True)


