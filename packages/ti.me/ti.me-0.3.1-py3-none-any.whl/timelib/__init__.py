"""Provides models and management api for tasks and plans.

You can use timelib library for embedding ti.me capabilities in your own app.

Examples:
    Creating Manager instance::

        from datetime import datetime

        from timelib import Manager, create_session


        manager = Manager(
            session=create_session('sqlite://'),
            default_user='stranger',
        )

    Creating new tasks::

        with manager.save_after():
            lab3task = manager.create_task(
                text='Pass tas lab #3',
                from_time=datetime(2018, 08, 24),
                labels=['labs.tas'],
                priority='important',
            )
        with manager.save_after():
            lab4task = manager.create_task(
                text='Pass tas lab #4',
                from_time=datetime(2018, 08, 24),
                labels=['labs.tas'],
                priority='important',
                blocking_task_ids=[lab3task],
            )
        with manager.save_after():
            examtask = manager.create_task(
                text='Pass tas exam',
                from_time=datetime(2018, 09, 08),
                labels=['edu.tas'],
                priority='critical',
                blocking_task_ids=[lab3task, lab4task],
            )

    Completing task::

        with manager.save_after():
            manager.complete_task(id=lab3task.id)

    Filtering tasks::

        manager.get_tasks(labels=['labs'])

    Also you can find other use cases in tests.
"""

__author__ = 'Vladimir Sernatsky <byport1112@gmail.com>'
__license__ = 'MIT'
__version__ = __import__('pkg_resources').get_distribution('ti.me').version
__status__ = 'Development'

from timelib.management import (
    Manager,
    create_session,
)

__all__ = ['Manager', 'create_session']
