# -*- coding: utf-8 -*-

dh.define_table('content_para',
                    Field('para', type='text',
                                        length=8000,
                                        default=None,
                                        required=True,
                                        requires=IS_NOT_EMPTY(),
                                        notnull=True,
                                        unique=False,
                                        label='Content',
                                        #comment=None,
                                        writable=True,
                                        readable=True,
                                        update=None),
                    migrate=True)



